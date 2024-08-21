# dependencies
from typing import Union
from flask import Flask, request, jsonify, make_response
import mysql.connector

# own components
from modules import authenticate
from modules import find

from modules import timelineManager
from modules import userManager
import config

app = Flask(__name__)

# "init"
print(f'Welcome to {config.NAME} {config.VERSION}')






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



# User and Settings endpoints
# Profile
@app.route('/users/profiles/<user_id>', methods=['GET'])
def initHPF(user_id):
    return userManager.handleProfile(user_id)

# Userinfo Retrieval
@app.route('/users/me', methods=['GET'])
def initMeRequest():
    return userManager.handleMeRequest()

"""# Profile picture uploading
@app.route('/avatars<file>', methods=['PUT'])
def manage_user_upload(file):
    return userManager.setPFP(file)"""

# Preference Management
@app.route('/users/<user_id>', methods=['PUT'])
def manage_user_settings(user_id):
    return userManager.settings_management(user_id)

# Preference Management v2
@app.route('/users/<user_id>/preferences', methods=['PUT'])
def manage_advanced_settings(user_id):
    return userManager.furtherSettingsManagement(user_id)

@app.route('/users/<user_id>/following/suggested/contacts', methods=['PUT'])
def addressBookInitialization(user_id):
    return find.addressBookIntegration()
#Followers, and following, aswell as following


# timeline endpoints

# user specific
@app.route('/timelines/users/<user_id>/likes', methods=['GET'])
def callLikePageFunction(user_id):
    return timelineManager.userLikes(user_id)

@app.route('/timelines/users/<user_id>', methods=['GET'])
def callUserTimelineRetrieval(user_id):
    return timelineManager.userLikes(user_id)










# experiment
@app.route('/users/<user_id>/notifications', methods=['GET'])
def sampleNotif(user_id):
    response = {
    "code": "",
    "data": {
        "count": 1,
        "records": [
            {
                "body": "what the fuck",
                "verified": 0,
                "avatarUrl": "https://blog.bag-xml.com/assets/img/ios3.png",
                "notificationTypeId": 1,
                "created": "2024-08-12T14:29:1.2",
                "userId": 23,
                "notificationId": 492792423,
                "postId": 1
            },
            {
                "body": "some user is now following you!",
                "thumbnailUrl": "https://bag-xml.com/assets/img/discord.png", # Post thumbnail
                "verified": 0,
                "avatarUrl": "https://blog.bag-xml.com/assets/img/ios3.png", # User who triggered action
                "notificationTypeId": 2,
                "created": "2024-08-12T14:29:1.2",
                "userId": 23,
                "notificationId": 123456789,
                "postId": 1
            },
            {
                "body": "some user is now following you!",
                "thumbnailUrl": "https://bag-xml.com/assets/img/discord.png", #righthand image
                "verified": 0,
                "avatarUrl": "https://blog.bag-xml.com/assets/img/ios3.png",
                "notificationTypeId": 3,
                "created": "2024-08-12T14:29:1.2",
                "userId": 23,
                "notificationId": 123456789,
                "postId": 1
            }
        ],
        "nextPage": 1,
        "previousPage": None,
        "size": 250
    },
    "success": True,
    "error": ""
    }

    return jsonify(response)

@app.route('/users/<user_id>/pendingNotificationsCount', methods=['GET'])
def samplePendingNotif(user_id):
    response = {
    "code": "",
    "data": 1,
    "success": True,
    "error": ""
    }

    return jsonify(response)
# Host
if __name__ == '__main__':
    app.run(port=config.PORT, host="0.0.0.0", debug=False)