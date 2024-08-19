# dependencies
from typing import Union
from flask import Flask, request, jsonify, make_response
import mysql.connector
import bcrypt
import uuid

# own components
from modules import authenticate
from modules import find
import config


# "init"
print(f'Welcome to {config.NAME} {config.VERSION}')

app = Flask(__name__)
cnx = mysql.connector.connect(user=config.USERNAME, password=config.PASSWORD,host=config.DBHOST,database=config.DATABASE)




# Init-Authentication methods
# Register
@app.route('/users', methods=['POST'])
def initiate_usercreation():
    return authenticate.create_user()

# Login
@app.route('/users/authenticate', methods=['POST'])
def initiate_login():
    return authenticate.login()


# logout
@app.route('/users/authenticate', methods=['DELETE'])
def initiate_logout():
    return authenticate.logout()


#forgot password




@app.route('/users/profiles/<user_id>', methods=['GET'])
def handleProfile(user_id):
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT username, followingCount, followerCount, isVerified, description, pfp, likeCount, postCount, phoneNumber, location, email FROM users WHERE id = %s", (user_id,))
    row = cursor.fetchone()

    response = {
    "code": "",
    "data": {
        "username": row[0],
        "following": row[1],
        "followerCount": row[2],
        "verified": row[3],
        "description": row[4],
        "avatarUrl": row[5],
        "twitterId": 0,
        "userId": user_id,
        "twitterConnected": 0,
        "likeCount": row[6],
        "facebookConnected": 0,
        "postCount": row[7],
        "phoneNumber": row[8],
        "location": row[9],
        "followingCount": row[1],
        "email": row[10]
    },
    "success": True,
    "error": ""
    }

    return jsonify(response)

@app.route('/users/me', methods=['GET'])
def handleMeRequest():
    response = {
    "code": "",
    "data": {
        "username": "Bill",
        "following": 0,
        "followerCount": 1,
        "verified": 0,
        "description": "Vine.app example account",
        "avatarUrl": "https://vines.s3.amazonaws.com/avatars/123456789.jpg",
        "twitterId": 123456789,
        "userId": 123456789,
        "twitterConnected": 1,
        "likeCount": 0,
        "facebookConnected": 0,
        "postCount": 0,
        "phoneNumber": None,
        "location": "Paris, France",
        "followingCount": 0,
        "email": "xxx@example.com"
    },
    "success": True,
    "error": ""
    }
    return jsonify(response)





from flask import request, jsonify

@app.route('/users/<user_id>', methods=['PUT'])
def settings_management(user_id):
    form_data = request.form

    if 'username' in form_data:
        cursor = cnx.cursor(buffered=True)
        cursor.execute("UPDATE users SET username = %s WHERE id = %s", (form_data["username"], user_id))
        cnx.commit()
        cursor.close()
        print(f"[Settings management] User {user_id} has changed their username to {form_data['username']}")
        # success
        response = {
        "code": "",
        "data": [],
        "success": True,
        "error": ""
        }
        return make_response(jsonify(response), 201)

    elif 'description' in form_data:
        cursor = cnx.cursor(buffered=True)
        cursor.execute("UPDATE users SET description = %s WHERE id = %s", (form_data["description"], user_id))
        cnx.commit()
        cursor.close()
        print(f"[Settings management] User {user_id} has changed their description to {form_data['description']}")
        # success
        response = {
        "code": "",
        "data": [],
        "success": True,
        "error": ""
        }
        return make_response(jsonify(response), 201)

    elif 'location' in form_data:
        cursor = cnx.cursor(buffered=True)
        cursor.execute("UPDATE users SET location = %s WHERE id = %s", (form_data["location"], user_id))
        cnx.commit()
        cursor.close()
        print(f"[Settings management] User {user_id} has changed their location name.")
        # success
        response = {
        "code": "",
        "data": [],
        "success": True,
        "error": ""
        }
        return make_response(jsonify(response), 201)

    elif 'email' in form_data:
        cursor = cnx.cursor(buffered=True)
        cursor.execute("UPDATE users SET email = %s WHERE id = %s", (form_data["email"], user_id))
        cnx.commit()
        cursor.close()
        print(f"[Settings management] User {user_id} has changed their Email address to {form_data['email']}")
        # success
        response = {
        "code": "",
        "data": [],
        "success": True,
        "error": ""
        }
        return make_response(jsonify(response), 201)

    elif 'phoneNumber' in form_data:
        cursor = cnx.cursor(buffered=True)
        cursor.execute("UPDATE users SET phoneNumber = %s WHERE id = %s", (form_data["phoneNumber"], user_id))
        cnx.commit()
        cursor.close()
        print(f"[Settings management] User {user_id} has changed their phone number.")
        # success
        response = {
        "code": "",
        "data": [],
        "success": True,
        "error": ""
        }
        return make_response(jsonify(response), 201)
    elif 'private' in form_data:
        cursor = cnx.cursor(buffered=True)
        cursor.execute("UPDATE users SET isPrivate = %s WHERE id = %s", (form_data["private"], user_id))
        cnx.commit()
        cursor.close()
        print(f"[Settings management] User {user_id} has changed their account protection status to {form_data['private']}.")
        # success
        response = {
        "code": "",
        "data": [],
        "success": True,
        "error": ""
        }
        return make_response(jsonify(response), 201)
    elif 'twitterConnected' in form_data:
        print("a")
    else:
        response = {
        "code": "",
        "data": [],
        "success": False,
        "error": "An unexpected error has occured. Sorry for the inconvenience."
        }
        return make_response(jsonify(response), 401)
        # add twitter and facebook too but only to satisfy the users feedback, not actually add them hehe

    
# Host
if __name__ == '__main__':
    app.run(port=config.PORT, host="0.0.0.0", debug=False)