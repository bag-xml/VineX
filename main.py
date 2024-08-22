# dependencies
from typing import Union
from flask import Flask, request, jsonify, make_response
import mysql.connector

# own components
from modules import authenticate
from modules import find
from modules import userActions
from modules import notificationsManager
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

# Notifications
@app.route('/users/<user_id>/notifications', methods=['GET'])
def initiateLoadNotifs(user_id):
    return notificationsManager.loadNotifications(user_id)

@app.route('/users/<user_id>/pendingNotificationsCount', methods=['GET'])
def pendingNotifications(user_id):
    return notificationsManager.retrievePendingNotifications(user_id)

# User actions
# Follow
@app.route('/users/<user_id>/followers', methods=['POST'])
def initFollow(user_id):
    return userActions.followUser(user_id)

@app.route('/users/<user_id>/followers', methods=['DELETE'])
def initUnfollow(user_id):
    return userActions.unfollowUser(user_id)

# Following, and follower pages
@app.route('/users/<user_id>/following', methods=['GET'])
def initFollowingPage(user_id):
    return userManager.followingPage(user_id)


@app.route('/users/<user_id>/followers', methods=['GET'])
def initFollowerPage(user_id):
    return userManager.followerPage(user_id)




# experiment
@app.route('/explore', methods=['GET'])
def sendExplore():
    return app.send_static_file('index.html')





# Host
if __name__ == '__main__':
    app.run(port=config.PORT, host="0.0.0.0", debug=False)