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










# ::post actions

def likePost(post_id):
    userIdentifier = request.headers.get('vine-session-id')
    cnx = mysql.connector.connect(user=config.USERNAME, password=config.PASSWORD,host=config.DBHOST,database=config.DATABASE)
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT likedPosts, id FROM users WHERE uniqueIdentifier = %s", (userIdentifier,))
    liked_row = cursor.fetchone()


    if liked_row:
        likedlist_json = liked_row[0] if liked_row[0] else '{"liked_posts": []}'
        liked_data = json.loads(likedlist_json)

        if 'liked_posts' not in liked_data or not isinstance(liked_data['liked_posts'], list):
            liked_data['liked_posts'] = []

        if post_id not in liked_data['liked_posts']:
            liked_data['liked_posts'].append(post_id)
            final_likelist_json = json.dumps(liked_data)
            cursor.execute("UPDATE users SET likedPosts = %s, likeCount = likeCount + 1 WHERE uniqueIdentifier = %s", (final_likelist_json, userIdentifier))
            cnx.commit()

    # on the post's entry, update the users who actually like the post. for the list
    cursor.execute("SELECT usersWhoLiked, authorID FROM posts WHERE postID = %s", (post_id,))
    like_row = cursor.fetchone()
    user_id = liked_row[1]
    if like_row:
        likelist_json = like_row[0] if like_row[0] else '{"liked": []}'
        like_data = json.loads(likelist_json)

        if 'liked' not in like_data or not isinstance(like_data['liked'], list):
            like_data['liked'] = []

        if user_id not in like_data['liked']:
            like_data['liked'].append(user_id)
            final_likerlist_json = json.dumps(like_data)
            cursor.execute("UPDATE posts SET usersWhoLiked = %s WHERE postID = %s", (final_likerlist_json, post_id))
            cnx.commit()


    notificationsManager.sendNotification(liked_row[1], like_row[1], post_id, type="LIKE")


    response = {
    "code": "",
    "data": [],
    "success": True,
    "error": ""
    }

    return make_response(jsonify(response), 201)


def unlikePost(post_id):
    userIdentifier = request.headers.get('vine-session-id')
    cnx = mysql.connector.connect(user=config.USERNAME, password=config.PASSWORD,host=config.DBHOST,database=config.DATABASE)
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT likedPosts, id FROM users WHERE uniqueIdentifier = %s", (userIdentifier,))
    liked_row = cursor.fetchone()

    likelist_json = liked_row[0]
    liked_list = json.loads(likelist_json)['liked_posts']
    
    if post_id in liked_list:
        liked_list.remove(post_id)
    final_likelist_json = json.dumps({"liked_posts": liked_list})

    cursor.execute("UPDATE users SET likedPosts = %s, likeCount = likeCount - 1  WHERE uniqueIdentifier = %s", (final_likelist_json, userIdentifier))
    cnx.commit()

    cursor.execute("SELECT usersWhoLiked FROM posts WHERE postID = %s", (post_id,))
    uwl_row = cursor.fetchone()
    uwl_json = uwl_row[0]
    uwl_list = json.loads(uwl_json)['liked']
    
    if liked_row[1] in uwl_list:
        uwl_list.remove(liked_row[1])
    final_uwllist_json = json.dumps({"liked": uwl_list})

    cursor.execute("UPDATE posts SET usersWhoLiked = %s WHERE postID = %s", (final_uwllist_json, post_id))
    cnx.commit()

    response = {
    "code": "",
    "data": [],
    "success": True,
    "error": ""
    }

    return make_response(jsonify(response), 201)


def fileAPostComplaint(post_id):
    cnx = mysql.connector.connect(user=config.USERNAME, password=config.PASSWORD,host=config.DBHOST,database=config.DATABASE)
    likerIdentifier = request.headers.get('vine-session-id')
    cursor = cnx.cursor(buffered=True)

    cursor.execute("SELECT username, id FROM users WHERE uniqueIdentifier = %s", (likerIdentifier,))
    sender_row = cursor.fetchone()


    print(f"[User Actions Manager] User {sender_row[0]} (User ID: {sender_row[1]}) filed a complaint against post(ID) {post_id}). Please check later in the complaints pot!")

    #todo, better complaint system. tables in db, and once the count reaches 10, by all different users, the account should be banned
    with open("complaints.txt", "a") as file:
        file.write(f"Complaint by User: {sender_row[0]} (User ID: {sender_row[1]}) against "
                   f"Post(id): {post_id}\n")

    response = {
    "code": "",
    "data": [],
    "success": True,
    "error": ""
    }

    return make_response(jsonify(response), 201)