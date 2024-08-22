from typing import Union
from flask import Flask, request, jsonify, make_response
import mysql.connector
import config


def loadNotifications(user_id):
    return "null"

def retrievePendingNotifications(user_id):
    response = {
    "code": "",
    "data": 1,
    "success": True,
    "error": ""
    }
    return jsonify(response)



def sendNotification(sender_id, target_ID, type):
    print(f"Preparing send of notification, by User {sender_id}, to {target_ID}, with the type {type}")
    return "what"
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