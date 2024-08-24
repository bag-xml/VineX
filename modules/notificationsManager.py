from flask import Flask, request, jsonify, make_response
from datetime import datetime
import mysql.connector
import config



def displayNotifications(user_id):
    response = {
    "code": "",
    "data": {
        "count": 1,
        "records": [
            {
                "body": "what the fuck",
                "username": "wtf",
                "verified": 0,
                "avatarUrl": "https://blog.bag-xml.com/assets/img/ios3.png",
                "notificationTypeId": 1,
                "created": "2024-08-24T05:29:1.2",
                "userId": 23,
                "notificationId": 492792423,
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

def retrievePendingNotifications(user_id):
    response = {
    "code": "",
    "data": 1,
    "success": True,
    "error": ""
    }
    return jsonify(response)



def sendNotification(sender_id, target_ID, type):
    cnx = mysql.connector.connect(user=config.USERNAME, password=config.PASSWORD,host=config.DBHOST,database=config.DATABASE)
    print(f"[Notifications Manager] Preparing send of notification, by User {sender_id}, to {target_ID}, with the type {type}")

    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT pfp, username FROM users WHERE id = %s", (sender_id,))
    sender_row = cursor.fetchone()
    
    time = datetime.now()
    timeOfPush = time.strftime("%Y-%m-%dT%H:%M:1.2")

    if type == 'FOLLOW':
        notificationTypeID = int(1)
        notificationMessage = str("started to follow you!")
        cursor.execute("INSERT INTO notifications (userID, authorID, notificationType, avatarURL, creationDate, message, sender_username) VALUES (%s, %s, %s, %s, %s, %s, %s)", (target_ID, sender_id, notificationTypeID, sender_row[0], timeOfPush, notificationMessage, sender_row[1]))
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