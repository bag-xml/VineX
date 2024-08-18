# dependencies
import config

import mysql.connector
import bcrypt
import uuid

from typing import Union
from flask import Flask, request, jsonify, make_response

# start mysql connection
cnx = mysql.connector.connect(user=config.USERNAME, password=config.PASSWORD,host=config.DBHOST,database=config.DATABASE)


def create_user():
    print("[Registration] Registration segment initiated")
    # specified data
    authBool = request.form.get('authenticate')
    email = request.form.get('email')
    passwd = request.form.get('password')
    username = request.form.get('username')
    
    salt = bcrypt.gensalt(rounds=15)
    securepasswd = bcrypt.hashpw(bytes(passwd, 'UTF-8'), salt)

    # database segment
    cursor = cnx.cursor()

    #checkers for exustubg email and username
    cursor.execute("SELECT COUNT(*) FROM users WHERE username = %s", (username,))
    username_overlap = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM users WHERE email = %s", (email,))
    email_overlap = cursor.fetchone()[0]
    
    if username_overlap > 0:
        print("[Registration] User specified an already existent username. Aborting account creation.")
        response = {
        "code": "",
        "data": [],
        "success": False,
        "error": "An account with that username already exists. Please choose another username to continue."
        }

        return make_response(jsonify(response), 401)

    elif email_overlap > 0:
        print("[Registration] User specified an already existent e-mail. Aborting account creation.")
        response = {
        "code": "",
        "data": [],
        "success": False,
        "error": "An account with that Email address already exists. Please choose another Email to continue."
        }

        return make_response(jsonify(response), 401)
    else:
        print(f"[Registration] Filing database entry for a NEW USER. Given data is: {username} {email} {securepasswd}")
        cursor.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)", (username, securepasswd.decode('UTF-8'), email))
        cnx.commit()
        # get user id
        user_id = cursor.lastrowid
        # special key
        key = uuid.uuid4()

        cursor.close()
        print(f"[Registration] User creation successful, welcome {username} aka. ID {user_id}!")
    # end of database segment

    # Success response
    response = {
    "code": "",
    "data": {
        "username": username,
        "userId": user_id,
        "key": key
    },
    "success": True,
    "error": ""
    }

    return jsonify(response)


def login():
    print("[Login] User wants to log in")
    # specified data
    email = request.form.get('username')
    raw_password = request.form.get('password')

    plain_password = bytes(raw_password, 'UTF-8')
    # database
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT COUNT(*) FROM users WHERE email = %s", (email,))
    row = cursor.fetchone()
    print(row[0])

    if(row[0] > 0):
        cnx.commit()
        cursor.execute("SELECT password FROM users WHERE email = %s", (email,))
        row = cursor.fetchone()
        pybyte = bytes(row[0], 'UTF-8')
        if (bcrypt.checkpw(password=plain_password, hashed_password=pybyte)):
            
            # get user id and "key"
            cnx.commit()
            cursor.execute("SELECT username, id FROM users WHERE email = %s", (email,))
            row = cursor.fetchone()
            key = uuid.uuid4()
            # prep response
            response = {
            "code": "",
            "data": {
                "username": row[0],
                "userId": row[1],
                "key": key
            },
            "success": True,
            "error": ""
            }

            return jsonify(response)
        else:
            response = {
            "code": "",
            "data": [],
            "success": False,
            "error": "Incorrect password. If you forgot it, you can always reset your password."
            }

            return make_response(jsonify(response), 401)
    else:
        response = {
        "code": "",
        "data": [],
        "success": False,
        "error": "An account with that Email address does not exist."
        }

        return make_response(jsonify(response), 401)


def logout():
    response = {
    "code": "",
    "data": {},
    "success": True,
    "error": ""
    }
    return jsonify(response)