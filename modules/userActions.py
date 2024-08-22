from typing import Union
from flask import Flask, request, jsonify, make_response
import mysql.connector
import config
import json

from modules import notificationsManager

cnx = mysql.connector.connect(user=config.USERNAME, password=config.PASSWORD,host=config.DBHOST,database=config.DATABASE)

# mayyybe redo this some time later in development idk???????????????????????????????????????????
def followUser(user_id):
    likerIdentifier = request.headers.get('vine-session-id')
    print(f"{likerIdentifier} wants to follow user number {user_id}")
    cursor = cnx.cursor(buffered=True)
    
    # turn the session id into the user id
    cursor.execute("SELECT id FROM users WHERE uniqueIdentifier = %s", (likerIdentifier,))
    row = cursor.fetchone()

    if row is None:
        print("[User Action] User failed following, most likely wrong app version or corrupt session.")
        response = {
            "code": "",
            "data": [],
            "success": False,
            "error": "An unexpected error has occurred"
        }
        return make_response(jsonify(response), 401)

    liker_ID = row[0]
    print(f"yipee, new follower is {liker_ID}")

    # Follower segment of user_id aka the account that the user wants to follow
    cursor.execute("SELECT followers FROM users WHERE id = %s", (user_id,))
    follower_row = cursor.fetchone()

    if follower_row:
        followers_json = follower_row[0] if follower_row[0] else '{"followers": []}'
        followers_data = json.loads(followers_json)

        if 'followers' not in followers_data or not isinstance(followers_data['followers'], list):
            followers_data['followers'] = []

        if liker_ID not in followers_data['followers']:
            followers_data['followers'].append(liker_ID)
            updated_followers_json = json.dumps(followers_data)
            cursor.execute("UPDATE users SET followers = %s, followerCount = followerCount + 1 WHERE id = %s", (updated_followers_json, user_id))
            print("DONE adding follower")
            cnx.commit()

    # Segment that updates "following" of liker_ID aka the user itself
    cursor.execute("SELECT following FROM users WHERE id = %s", (liker_ID,))
    following_row = cursor.fetchone()

    if following_row:
        following_json = following_row[0] if following_row[0] else '{"following": []}'
        following_data = json.loads(following_json)

        if 'following' not in following_data or not isinstance(following_data['following'], list):
            following_data['following'] = []

        if user_id not in following_data['following']:
            following_data['following'].append(user_id) 
            updated_following_json = json.dumps(following_data)
            print("Adding account to following list")
            cursor.execute("UPDATE users SET following = %s, followingCount = followingCount + 1 WHERE id = %s", (updated_following_json, liker_ID))
            cnx.commit()
    
    # call the notifications manager
    notificationsManager.sendNotification(liker_ID, user_id, type="FOLLOW")

    successFeedback = {
    "code": "",
    "data": [],
    "success": True,
    "error": ""
    }
    return jsonify(successFeedback)


    

def unfollowUser(user_id):
    """likerIdentifier = request.headers.get('vine-session-id')
    print(f"{likerIdentifier} wants to follow user number {user_id}")
    cursor = cnx.cursor(buffered=True)
    cursor.execute("UPDATE users SET followerCount = followerCount + 1 WHERE id = %s", (user_id,))
    cnx.commit()
    cursor.close()"""
    # todo, identify the person who liked, then call the notification sender function which will specify that user.
    response = {
    "code": "",
    "data": 1,
    "success": True,
    "error": ""
    }
    return jsonify(response)

    #cursor.execute("UPDATE users SET followerCount = followerCount + 1 WHERE id = %s", (user_id,))