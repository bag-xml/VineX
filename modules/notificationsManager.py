from flask import Flask, request, jsonify, make_response
from datetime import datetime
import mysql.connector
import config



def displayNotifications(user_id):
    cnx = mysql.connector.connect(user=config.USERNAME, password=config.PASSWORD,host=config.DBHOST,database=config.DATABASE)
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT * FROM notifications WHERE userID = %s", (user_id,))
    sender_row = cursor.fetchall()



    response = {
        "code": "",
        "data": {
            "count": 0,
            "records": [],
            "nextPage": None,
            "previousPage": None,
            "size": 250
        },
        "success": True,
        "error": ""
    }

    for row in sender_row:
        response["data"]["count"] += 1
        response["data"]["records"].append({
            "body": row[7],
            "username": row[6],
            "verified": 0,
            "avatarUrl": row[9],
            "notificationTypeId": row[1],
            "created": row[8],
            "userId": row[3],
            "notificationId": row[0],
        })

    return jsonify(response)

def retrievePendingNotifications(user_id):
    cnx = mysql.connector.connect(user=config.USERNAME, password=config.PASSWORD,host=config.DBHOST,database=config.DATABASE)
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT pending_notifications_count FROM users WHERE id = %s", (user_id,))
    row = cursor.fetchone()
    response = {
    "code": "",
    "data": row[0],
    "success": True,
    "error": ""
    }

    cursor.execute("UPDATE users SET pending_notifications_count = 0 WHERE id = %s", (user_id,))
    cnx.commit()
    cursor.close()
    return jsonify(response)
    



def sendNotification(sender_id, target_ID, type):
    cnx = mysql.connector.connect(user=config.USERNAME, password=config.PASSWORD,host=config.DBHOST,database=config.DATABASE)
    print(f"[Notifications Manager] Preparing send of notification, by User {sender_id}, to {target_ID}, with the type {type}")

    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT pfp, username FROM users WHERE id = %s", (sender_id,))
    sender_row = cursor.fetchone()
    print(f"asderfieopkorgihofjek {sender_row[0]}")

    time = datetime.now()
    timeOfPush = time.strftime("%Y-%m-%dT%H:%M:%S.%f")

    if type == 'FOLLOW':
        notificationTypeID = int(1)
        notificationMessage = str("started to follow you!")
        cursor.execute("INSERT INTO notifications (userID, authorID, notificationType, avatarURL, creationDate, message, sender_username) VALUES (%s, %s, %s, %s, %s, %s, %s)", (target_ID, sender_id, notificationTypeID, sender_row[0], timeOfPush, notificationMessage, sender_row[1]))
        cursor.execute("UPDATE users SET pending_notifications_count = pending_notifications_count + 1 WHERE id = %s", (target_ID,))  # Note the comma here
        cnx.commit()
        cursor.close()
    	

        print(f"[Notifications Manager] Successfully added notification of type {notificationTypeID} to the notifications pool.")

    elif type == "UNFOLLOW":
        return "b"
    elif type == "COMMENT":
        return "c"
    elif type == "MENTION":
        return "d"
    elif type == "LIKE":
        return "e"
    else:
        return "error"

"""
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

    return jsonify(response)"""