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



# timeline endpoints

# user specific
@app.route('/timelines/users/<user_id>/likes', methods=['GET'])
def callLikePageFunction(user_id):
    return timelineManager.userLikes(user_id)

@app.route('/timelines/users/<user_id>', methods=['GET'])
def callUserTimelineRetrieval(user_id):
    return timelineManager.userLikes(user_id)

2
# experiment
# Preference Management v2
@app.route('/users/<user_id>/notifications', methods=['GET'])
def sampleNotif(user_id):
    response = {
    "code": "",
    "data": {
        "count": 2,
        "records": [
            {
                "body": "some user is now following you!",
                "displayUserId": 22,
                "label": "ahfewhfieufhifh",
                "thumbnailUrl": None,
                "verified": 1,
                "avatarUrl": "https://bag-xml.com/assets/img/itunes.png",
                "notificationTypeId": 1,
                "created": "now",
                "userId": 22,
                "displayAvatarUrl": "https://bag-xml.com/assets/img/mobilemali.png",
                "notificationId": 3312356542334,
                "postId": None
            },
            {
                "body": "some user is now following you!",
                "displayUserId": 22,
                "label": "ahfewhfieufhifh",
                "thumbnailUrl": None,
                "verified": 1,
                "avatarUrl": "https://bag-xml.com/assets/img/itunes.png",
                "notificationTypeId": 2,
                "created": "2013-01-29T12:16:06.000000",
                "userId": 22,
                "displayAvatarUrl": "https://bag-xml.com/assets/img/mobilemali.png",
                "notificationId": 123456789,
                "postId": None
            },
            {
                "body": "some user is now following you!",
                "displayUserId": user_id,
                "label": "ahfewhfieufhifh",
                "thumbnailUrl": None,
                "verified": 1,
                "avatarUrl": "https://bag-xml.com/assets/img/itunes.png",
                "notificationTypeId": 3,
                "created": "2013-01-29T12:16:06.000000",
                "userId": user_id,
                "displayAvatarUrl": "https://bag-xml.com/assets/img/mobilemali.png",
                "notificationId": 123456789,
                "postId": None
            },
            {
                "body": "some user is now following you!",
                "displayUserId": user_id,
                "label": "ahfewhfieufhifh",
                "thumbnailUrl": None,
                "verified": 1,
                "avatarUrl": "https://bag-xml.com/assets/img/itunes.png",
                "notificationTypeId": 4,
                "created": "2013-01-29T12:16:06.000000",
                "userId": user_id,
                "displayAvatarUrl": "https://bag-xml.com/assets/img/mobilemali.png",
                "notificationId": 123456789,
                "postId": None
            },
        ],
        "nextPage": None,
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