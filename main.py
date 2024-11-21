# dependencies
from typing import Union
from flask import Flask, request, jsonify, make_response

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


## Users Endpoints ##
# Profile
@app.route('/users/profiles/<user_id>', methods=['GET'])
def initHPF(user_id):
    return userManager.handleProfile(user_id)

# Userinfo Retrieval
@app.route('/users/me', methods=['GET'])
def initMeRequest():
    return userManager.handleMeRequest()


@app.route('/avatars/<path:filename>', methods=['PUT'])
def manage_user_upload(filename):
    file_data = request.data
    return userManager.setPFP(filename, file_data)

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
    return notificationsManager.displayNotifications(user_id)

@app.route('/users/<user_id>/pendingNotificationsCount', methods=['GET'])
def pendingNotifications(user_id):
    return notificationsManager.retrievePendingNotifications(user_id)


# User actions
@app.route('/users/<user_id>/followers', methods=['POST'])
def initFollow(user_id):
    return userActions.followUser(user_id)

@app.route('/users/<user_id>/followers', methods=['DELETE'])
def initUnfollow(user_id):
    return userActions.unfollowUser(user_id)

@app.route('/users/<user_id>/blocked/<target_id>', methods=['POST'])
def initBlock(user_id, target_id):
    return userActions.blockUser(user_id, target_id)

@app.route('/users/<user_id>/blocked/<target_id>', methods=['DELETE'])
def initUnblock(user_id, target_id):
    return userActions.unblockUser(user_id, target_id)

@app.route('/users/<user_id>/complaints', methods=['POST'])
def complaint(user_id):
    return userActions.fileComplaint(user_id)


# Following, and follower pages
@app.route('/users/<user_id>/following', methods=['GET'])
def initFollowingPage(user_id):
    return userManager.followingPage(user_id)

@app.route('/users/<user_id>/followers', methods=['GET'])
def initFollowerPage(user_id):
    return userManager.followerPage(user_id)


# Search
@app.route('/users/search/<query>', methods=['GET'])
def initUserSearch(query):
    return userManager.searchForUser(query)



## Explore page ##
@app.route('/explore', methods=['GET'])
def sendPage():
    return app.send_static_file('index.html'), 200


## Timeline endpoints ##
"""@app.route('/timelines/graph', methods=['GET'])
def retrieveFeedPage():
    return timelineManager.sampleRetrieve()"""
 
 
 #/timelines/users/1/likes
@app.route('/timelines/users/<user_id>', methods=['GET'])
def retrieveUserFeedPage(user_id):
    return timelineManager.userTimeline(user_id)

@app.route('/timelines/users/<user_id>/likes', methods=['GET'])
def retrieveUserLPosts(user_id):
    return timelineManager.userLikes(user_id)


@app.route('/timelines/posts/<post_id>', methods=['GET'])
def loadSingularPost(post_id):
    return timelineManager.loadSinglePost(post_id)



# user actions
# ::like
@app.route('/posts/<post_id>/likes', methods=['POST'])
def likeAPost(post_id):
    return userActions.likePost(post_id)

@app.route('/posts/<post_id>/likes', methods=['DELETE'])
def unlikeAPost(post_id):
    return userActions.unlikePost(post_id)

#::report
@app.route('/posts/<post_id>/complaints', methods=['POST'])
def reportAPost(post_id):
    return userActions.fileAPostComplaint(post_id)

# Host
if __name__ == '__main__':
    app.run(port=config.PORT, host="0.0.0.0", debug=False)