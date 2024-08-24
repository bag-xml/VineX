from typing import Union
from flask import Flask, request, jsonify, make_response
import mysql.connector
import config
import json

from modules import notificationsManager


# mayyybe redo this some time later in development idk???????????????????????????????????????????
def followUser(user_id):
    cnx = mysql.connector.connect(user=config.USERNAME, password=config.PASSWORD,host=config.DBHOST,database=config.DATABASE)
    likerIdentifier = request.headers.get('vine-session-id')
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
    print(f'[User Actions Manager] User {liker_ID} wants to follow {user_id}.')
    
    print(f'[User Actions Manager] Initiating database entry segment.')
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
            cursor.execute("UPDATE users SET following = %s, followingCount = followingCount + 1 WHERE id = %s", (updated_following_json, liker_ID))
            cnx.commit()

    # call the notifications manager
    notificationsManager.sendNotification(liker_ID, user_id, type="FOLLOW")
    print(f'[User Actions Manager] Done adding follower')

    successFeedback = {
    "code": "",
    "data": [],
    "success": True,
    "error": ""
    }
    return jsonify(successFeedback)


    

def unfollowUser(user_id): #unfollower_id = user, user_id = target
    cnx = mysql.connector.connect(user=config.USERNAME, password=config.PASSWORD,host=config.DBHOST,database=config.DATABASE)
    likerIdentifier = request.headers.get('vine-session-id')
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT id FROM users WHERE uniqueIdentifier = %s", (likerIdentifier,))
    row = cursor.fetchone()

    if row is None:
        print("[User Action] User failed unfollowing, most likely wrong app version or corrupt session.")
        response = {
            "code": "",
            "data": [],
            "success": False,
            "error": "An unexpected error has occurred"
        }
        return make_response(jsonify(response), 401)

    unfollower_id = row[0]
    print(f'[User Actions Manager] User {unfollower_id} wants to unfollow {user_id}.')

    print(f'[User Actions Manager] Initiating database entry segment.')

    cursor.execute("SELECT following FROM users WHERE id = %s", (unfollower_id,))
    following_row = cursor.fetchone()
    followlist_json = following_row[0]
    followed_list = json.loads(followlist_json)['following']
    
    if user_id in followed_list:
        followed_list.remove(user_id)
    final_followed_list_json = json.dumps({"following": followed_list})

    cursor.execute("UPDATE users SET following = %s, followingCount = followingCount - 1 WHERE id = %s", (final_followed_list_json, unfollower_id))
    cnx.commit()

    cursor.execute("SELECT followers FROM users WHERE id = %s", (user_id,))
    followers_row = cursor.fetchone()
    followersList_json = followers_row[0]
    follower_list = json.loads(followersList_json)['followers']
    
    if unfollower_id in follower_list:
        follower_list.remove(unfollower_id)
    final_follower_list_json = json.dumps({"followers": follower_list})

    cursor.execute("UPDATE users SET followers = %s, followerCount = followerCount - 1 WHERE id = %s", (final_follower_list_json, user_id))
    cnx.commit()


    notificationsManager.sendNotification(unfollower_id, user_id, type="UNFOLLOW")
    print(f'[User Actions Manager] Done removing follower')

    successFeedback = {
    "code": "",
    "data": [],
    "success": True,
    "error": ""
    }
    return jsonify(successFeedback)


def blockUser(user_id, target_id):
    cnx = mysql.connector.connect(user=config.USERNAME, password=config.PASSWORD,host=config.DBHOST,database=config.DATABASE)
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT blocked FROM users WHERE id = %s", (user_id,))
    blocked_row = cursor.fetchone()
    if blocked_row:
        blocklist_json = blocked_row[0] if blocked_row[0] else '{"blocked": []}'
        blocked_data = json.loads(blocklist_json)

        if 'blocked' not in blocked_data or not isinstance(blocked_data['blocked'], list):
            blocked_data['blocked'] = []

        if target_id not in blocked_data['blocked']:
            blocked_data['blocked'].append(target_id)
            final_blocklist_json = json.dumps(blocked_data)
            cursor.execute("UPDATE users SET blocked = %s WHERE id = %s", (final_blocklist_json, user_id))
            cnx.commit()

    response = {
    "code": "",
    "data": [],
    "success": True,
    "error": ""
    }

    return make_response(jsonify(response), 201)


def unblockUser(user_id, target_id):
    cnx = mysql.connector.connect(user=config.USERNAME, password=config.PASSWORD,host=config.DBHOST,database=config.DATABASE)
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT blocked FROM users WHERE id = %s", (user_id,))
    blocked_row = cursor.fetchone()
    blocklist_json = blocked_row[0]
    blocked_list = json.loads(blocklist_json)['blocked']
    
    if target_id in blocked_list:
        blocked_list.remove(target_id)
    final_blocklist_json = json.dumps({"blocked": blocked_list})

    cursor.execute("UPDATE users SET blocked = %s WHERE id = %s", (final_blocklist_json, user_id))
    cnx.commit()

    response = {
    "code": "",
    "data": [],
    "success": True,
    "error": ""
    }

    return make_response(jsonify(response), 201)




def fileComplaint(user_id):
    cnx = mysql.connector.connect(user=config.USERNAME, password=config.PASSWORD,host=config.DBHOST,database=config.DATABASE)
    likerIdentifier = request.headers.get('vine-session-id')
    cursor = cnx.cursor(buffered=True)

    cursor.execute("SELECT username, id FROM users WHERE uniqueIdentifier = %s", (likerIdentifier,))
    sender_row = cursor.fetchone()

    cursor.execute("SELECT username, id FROM users WHERE id = %s", (user_id,))
    recipient_row = cursor.fetchone()

    print(f"[User Actions Manager] User {sender_row[0]} (User ID: {sender_row[1]}) filed a complaint against {recipient_row[0]} (User ID {recipient_row[1]})'s account. Please check later in the complaints pot!")

    #todo, better complaint system. tables in db, and once the count reaches 10, by all different users, the account should be banned
    with open("complaints.txt", "a") as file:
        file.write(f"Complaint by User: {sender_row[0]} (User ID: {sender_row[1]}) against "
                   f"User: {recipient_row[0]} (User ID: {recipient_row[1]})\n")

    response = {
    "code": "",
    "data": [],
    "success": True,
    "error": ""
    }

    return make_response(jsonify(response), 201)
