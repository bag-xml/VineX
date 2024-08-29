from typing import Union
from flask import Flask, request, jsonify, make_response
import mysql.connector
import config
import json


# userinfo segment

def handleProfile(user_id):
    uniqueIdentifer = request.headers.get('vine-session-id')
    cnx = mysql.connector.connect(user=config.USERNAME, password=config.PASSWORD,host=config.DBHOST,database=config.DATABASE)
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT id FROM users WHERE uniqueIdentifier = %s", (uniqueIdentifer,))
    user_check_row = cursor.fetchone()

    cursor.execute("SELECT username, followingCount, followerCount, isVerified, description, pfp, likeCount, postCount, phoneNumber, location, email, promo FROM users WHERE id = %s", (user_id,))
    row = cursor.fetchone()

    database_id = str(user_check_row[0])
    userId = str(user_id)

    if database_id == userId: # account belongs to user, this will load faster
        print("Success!")
        
        response = {
        "code": "",
        "data": {
            "username": row[0],
            "following": 0,
            "blocked": 0,
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
            "includePromoted": row[11],
            "email": row[10]
        },
        "success": True,
        "error": ""
        }
        return jsonify(response)
    else:
        cursor.execute("SELECT blocked, following FROM users WHERE id = %s", (database_id,))
        listrows = cursor.fetchone()
        isBlocked = False
        isFollowing = False

        if listrows:
            blocked_json, following_json = listrows
            blocked_data = json.loads(blocked_json) if blocked_json else {"blocked": []}
            following_data = json.loads(following_json) if following_json else {"following": []}

            if 'blocked' in blocked_data and isinstance(blocked_data['blocked'], list):
                if user_id in blocked_data['blocked']:
                    isBlocked = True

            if 'following' in following_data and isinstance(following_data['following'], list):
                if user_id in following_data['following']:
                    print("following")
                    isFollowing = True
                if user_id not in following_data['following']:
                    print("porn")


        response = {
        "code": "",
        "data": {
            "username": row[0],
            "following": isFollowing,
            "blocked": isBlocked,
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
            "includePromoted": row[11],
            "email": row[10]
        },
        "success": True,
        "error": ""
        }
        return jsonify(response)

        

def handleMeRequest():
    cnx = mysql.connector.connect(user=config.USERNAME, password=config.PASSWORD,host=config.DBHOST,database=config.DATABASE)
    uniqueIdentifer = request.headers.get('vine-session-id')
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT username, followingCount, followerCount, isVerified, description, pfp, likeCount, postCount, phoneNumber, location, email, id, promo FROM users WHERE uniqueIdentifier = %s", (uniqueIdentifer,))
    row = cursor.fetchone()

    if row is None:
        response = {
        "code": "",
        "data": [],
        "success": False,
        "error": "An unexpected error has occured"
        }
        return make_response(jsonify(response), 401)
    
    #todo: orga, and make sure tha tif its "0" to send nothing

    phone_number = str(row[8])
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
        "userId": row[11],
        "twitterConnected": 0,
        "likeCount": row[6],
        "facebookConnected": 0,
        "postCount": row[7],
        "phoneNumber": phone_number,
        "location": row[9],
        "followingCount": row[1],
        "includePromoted": row[12],
        "email": row[10]
    },
    "success": True,
    "error": ""
    }
    
    return jsonify(response)


# follower and following pages
def followingPage(user_id):
    cnx = mysql.connector.connect(user=config.USERNAME, password=config.PASSWORD,host=config.DBHOST,database=config.DATABASE)
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT following FROM users WHERE id = %s", (user_id,))
    row = cursor.fetchone()


    response = {
        "code": "",
        "data": {
            "count": 0,
            "records": [],
            "nextPage": 1,
            "previousPage": None,
            "size": 250
        },
        "success": True,
        "error": ""
    }

    if row:
        following_dict = json.loads(row[0])
        following_list = following_dict.get('following', [])

        if following_list:
            following_list = [int(user_id) for user_id in following_list]
            format_strings = ','.join(['%s'] * len(following_list))

            query = f"SELECT id, username, pfp, following FROM users WHERE id IN ({format_strings})"
            cursor.execute(query, tuple(following_list))
            followed_users = cursor.fetchall()
            isFollowing = False


            for user in followed_users:

                fol_json = user[3]
                following_data = json.loads(fol_json) if fol_json else {"following": []}
                if 'following' in following_data and isinstance(following_data['following'], list):
                    if user_id in following_data['following']:
                        isFollowing = True
                    if user_id not in following_data['following']:
                        isFollowing = False

                response["data"]["count"] += 1
                response["data"]["records"].append({
                    "userId": user[0],
                    "username": user[1],
                    "avatarUrl": user[2],
                    "following": isFollowing
                })
    cursor.close()
    cnx.close()
    
    # Return the response as JSON
    return jsonify(response)

def followerPage(user_id):
    cnx = mysql.connector.connect(user=config.USERNAME, password=config.PASSWORD,host=config.DBHOST,database=config.DATABASE)
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT followers FROM users WHERE id = %s", (user_id,))
    row = cursor.fetchone()


    response = {
        "code": "",
        "data": {
            "count": 0,
            "records": [],
            "nextPage": 1,
            "previousPage": None,
            "size": 250
        },
        "success": True,
        "error": ""
    }

    if row:
        followers_dict = json.loads(row[0])
        followers_list = followers_dict.get('followers', [])

        if followers_list:
            followers_list = [int(user_id) for user_id in followers_list]
            format_strings = ','.join(['%s'] * len(followers_list))

            query = f"SELECT id, username, pfp, following FROM users WHERE id IN ({format_strings})"
            cursor.execute(query, tuple(followers_list))
            follower_users = cursor.fetchall()
            isFollowing = False


            for user in follower_users:

                fol_json = user[3]
                follow_data = json.loads(fol_json) if fol_json else {"following": []}
                if 'following' in follow_data and isinstance(follow_data['following'], list):
                    if user_id in follow_data['following']:
                        isFollowing = True
                    if user_id not in follow_data['following']:
                        isFollowing = False

                response["data"]["count"] += 1
                response["data"]["records"].append({
                    "userId": user[0],
                    "username": user[1],
                    "avatarUrl": user[2],
                    "following": isFollowing
                })
    cursor.close()
    cnx.close()
    
    # Return the response as JSON
    return jsonify(response)
# userpreferences segment
def settings_management(user_id):
    cnx = mysql.connector.connect(user=config.USERNAME, password=config.PASSWORD,host=config.DBHOST,database=config.DATABASE)
    form_data = request.form

    if 'username' in form_data:
        cursor = cnx.cursor(buffered=True)
        cursor.execute("SELECT COUNT(*) FROM users WHERE username = %s", (form_data['username'],))
        username_overlap = cursor.fetchone()[0]
        if username_overlap > 0:
            response = {
                "code": "",
                "data": [],
                "success": False,
                "error": "An account with that username already exists. Please choose another username to continue."
            }
            return make_response(jsonify(response), 401)
        else:
            cursor.execute("UPDATE users SET username = %s WHERE id = %s", (form_data["username"], user_id))
            cnx.commit()
            cursor.close()
            print(f"[Settings management] User {user_id} has changed their username to {form_data['username']}")
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
        response = {
            "code": "",
            "data": [],
            "success": True,
            "error": ""
        }
        return make_response(jsonify(response), 201)

    elif 'email' in form_data:
        cursor = cnx.cursor(buffered=True)
        cursor.execute("SELECT COUNT(*) FROM users WHERE email = %s", (form_data['email'],))
        email_overlap = cursor.fetchone()[0]
        if email_overlap > 0:
            response = {
                "code": "",
                "data": [],
                "success": False,
                "error": "An account with that Email address already exists. Please choose another Email to continue."
            }
            return make_response(jsonify(response), 401)
        else:
            cursor.execute("UPDATE users SET email = %s WHERE id = %s", (form_data["email"], user_id))
            cnx.commit()
            cursor.close()
            print(f"[Settings management] User {user_id} has changed their Email address to {form_data['email']}")
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
        response = {
            "code": "",
            "data": [],
            "success": True,
            "error": ""
        }
        return make_response(jsonify(response), 201)

    elif 'deviceToken' in form_data:
        print(f"[Settings management] User {user_id} sent a device token. Token: {form_data['deviceToken']}")
        response = {
            "code": "",
            "data": [],
            "success": True,
            "error": ""
        }
        return make_response(jsonify(response), 201)

    else:
        print(f"[Settings management] User {user_id} has encountered an error.")
        response = {
            "code": "",
            "data": [],
            "success": False,
            "error": "An unexpected error has occurred. Sorry for the inconvenience."
        }
        return make_response(jsonify(response), 401)


def furtherSettingsManagement(user_id):
    cnx = mysql.connector.connect(user=config.USERNAME, password=config.PASSWORD,host=config.DBHOST,database=config.DATABASE)
    form_data = request.form
    if 'includePromoted' in form_data:
        cursor = cnx.cursor(buffered=True)
        cursor.execute("UPDATE users SET promo = %s WHERE id = %s", (form_data["includePromoted"], user_id))
        cnx.commit()
        cursor.close()
        print(f"[Settings management] User {user_id} has changed their 'Follow Editor's Picks' setting to {form_data['includePromoted']}")
        # success
        response = {
        "code": "",
        "data": [],
        "success": True,
        "error": ""
        }
        return make_response(jsonify(response), 201)

# need to engineer this still
def setPFP(filename, file_data):
    return "A"