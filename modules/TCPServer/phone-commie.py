import os
import threading
import datetime
from flask import Flask, request, jsonify
import json
import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import sqlite3
import select
import time
import argparse

app = Flask(__name__)

TCP_HOST = '0.0.0.0'
TCP_PORT = 7373
DATABASE = 'server_data.db'
EXPECTED_KEYS = {'message', 'topic'}  # Removed 'sender' here
active_client_lock = threading.Lock()
active_client = None

# Use absolute paths for better compatibility
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CLIENT_PUBLIC_KEY_PATH = os.path.join(BASE_DIR, 'client_public_key.pem')
SERVER_PRIVATE_KEY_PATH = os.path.join(BASE_DIR, 'server_private_key.pem')

def init_db():
    db_path = os.path.join(BASE_DIR, DATABASE)
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS valid_uuids (
                            id INTEGER PRIMARY KEY,
                            uuid TEXT UNIQUE)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS unacknowledged_messages (
                            id INTEGER PRIMARY KEY,
                            message_id TEXT UNIQUE,
                            message TEXT)''')
        conn.commit()

def add_uuid_to_db(uuid):
    db_path = os.path.join(BASE_DIR, DATABASE)
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT OR IGNORE INTO valid_uuids (uuid) VALUES (?)', (uuid,))
        conn.commit()

def encrypt_with_public_key(data, public_key_path=CLIENT_PUBLIC_KEY_PATH):
    try:
        with open(public_key_path, 'rb') as file:
            public_key = RSA.import_key(file.read())
        cipher = PKCS1_OAEP.new(public_key)
        encrypted_data = cipher.encrypt(data.encode('utf-8'))
        return encrypted_data
    except FileNotFoundError:
        print(f"Public key file not found at {public_key_path}. Please check the path.")
        raise
    except Exception as e:
        print(f"Error encrypting data: {e}")
        raise

def decrypt_with_private_key(data, private_key_path=SERVER_PRIVATE_KEY_PATH):
    try:
        with open(private_key_path, 'rb') as file:
            private_key = RSA.import_key(file.read())
        cipher = PKCS1_OAEP.new(private_key)
        decrypted_data = cipher.decrypt(data)
        return decrypted_data.decode('utf-8')
    except FileNotFoundError:
        print(f"Private key file not found at {private_key_path}. Please check the path.")
        raise
    except Exception as e:
        print(f"Error decrypting data: {e}")
        raise

def is_valid_uuid(uuid):
    db_path = os.path.join(BASE_DIR, DATABASE)
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT 1 FROM valid_uuids WHERE uuid = ?', (uuid,))
        return cursor.fetchone() is not None

def get_unacknowledged_messages():
    db_path = os.path.join(BASE_DIR, DATABASE)
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT message_id, message FROM unacknowledged_messages')
        messages = cursor.fetchall()
        return messages

def handle_client(client_socket):
    global active_client
    with active_client_lock:
        if active_client is not None and active_client != client_socket:
            try:
                active_client.close()
            except Exception as e:
                print(f"Error closing previous client socket: {e}")
        active_client = client_socket

    client_socket.setblocking(0)
    print(f"Client connected: {client_socket.getpeername()}")

    try:
        while True:
            ready_to_read, _, _ = select.select([client_socket], [], [], 1)
            if ready_to_read:
                data = client_socket.recv(1024)
                if not data:
                    print("No data received, client may have disconnected.")
                    break
                try:
                    decrypted_data = decrypt_with_private_key(data)
                    print(f"Received decrypted data: {decrypted_data}")
                    if decrypted_data.startswith('ACK:'):
                        message_id = decrypted_data.split(':')[1]
                        db_path = os.path.join(BASE_DIR, DATABASE)
                        with sqlite3.connect(db_path) as conn:
                            cursor = conn.cursor()
                            cursor.execute('DELETE FROM unacknowledged_messages WHERE message_id = ?', (message_id,))
                            conn.commit()
                    else:
                        uuid = decrypted_data
                        if not is_valid_uuid(uuid):
                            print(f"Invalid UUID: {uuid}")
                            break
                        print(f"Valid UUID: {uuid}")
                        unacknowledged_messages = get_unacknowledged_messages()
                        sent_message_ids = set()
                        for message_id, message in unacknowledged_messages:
                            if message_id not in sent_message_ids:
                                encrypted_message = base64.b64decode(message)
                                base64_encoded_message = base64.b64encode(encrypted_message).decode('utf-8')
                                try:
                                    client_socket.sendall(base64_encoded_message.encode('utf-8'))
                                    sent_message_ids.add(message_id)
                                except Exception as e:
                                    print(f"Error sending message to client: {e}")
                                    break
                except Exception as e:
                    print(f"Error processing data: {e}")
                    break
    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        with active_client_lock:
            if client_socket == active_client:
                active_client = None
        try:
            client_socket.close()
        except Exception as e:
            print(f"Error closing client socket: {e}")

@app.route('/send_data', methods=['POST'])
def send_data():
    json_data = request.json
    if not all(key in json_data for key in EXPECTED_KEYS):
        return jsonify({"error": "Invalid input data."}), 400
    
    message_id = json_data.get('message_id', str(datetime.datetime.now().timestamp()))
    json_data['message_id'] = message_id

    encrypted_data = encrypt_with_public_key(json.dumps(json_data))
    encrypted_data_base64 = base64.b64encode(encrypted_data).decode('utf-8')

    def db_operation():
        db_path = os.path.join(BASE_DIR, DATABASE)
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT OR REPLACE INTO unacknowledged_messages (message_id, message) VALUES (?, ?)',
                           (message_id, encrypted_data_base64))
            conn.commit()

    global active_client
    with active_client_lock:
        if active_client:
            try:
                base64_encoded_message = base64.b64encode(encrypted_data).decode('utf-8')
                active_client.sendall(base64_encoded_message.encode('utf-8'))
                time.sleep(2)
                if not is_acknowledged(message_id):
                    db_operation()
            except Exception as e:
                print(f"Error sending message {message_id} to active client: {e}")
                db_operation()
        else:
            db_operation()

    return jsonify({"message": "Data sent successfully"}), 200

def is_acknowledged(message_id):
    db_path = os.path.join(BASE_DIR, DATABASE)
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT 1 FROM unacknowledged_messages WHERE message_id = ?', (message_id,))
        return cursor.fetchone() is None

def tcp_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((TCP_HOST, TCP_PORT))
        server_socket.listen()
        print(" * TCP Server listening")
        while True:
            client_socket, _ = server_socket.accept()
            threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Start the server with optional UUID.")
    parser.add_argument('--uuid', type=str, help='UUID to add to the valid UUIDs database')
    args = parser.parse_args()

    init_db()

    if args.uuid:
        add_uuid_to_db(args.uuid)
        print(f"Added UUID to the database: {args.uuid}")

    threading.Thread(target=tcp_server, daemon=True).start()
    app.run(host='0.0.0.0', port=7878)
