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

# device token
@app.route('/users/<user_id>', methods=['PUT'])
def deviceTokenSynchronization(user_id):
    response = {
    "code": "",
    "data": {},
    "success": True,
    "error": ""
    }
    return make_response(jsonify(response), 201)


# Suggested
@app.route('/users/<user_id>/following/suggested/twitter', methods=['GET'])
def twitterInit(user_id):
    return find.twitterRecommendations()

@app.route('/users/<user_id>/following/suggested/contacts', methods=['PUT'])
def addressBookInitialization(user_id):
    return find.addressBookIntegration()

# Host
if __name__ == '__main__':
    app.run(port=config.PORT, host="0.0.0.0", debug=False)