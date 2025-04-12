# People-finder page
from typing import Union
from flask import Flask, request, jsonify, make_response
import mysql.connector
import json
import config

def addressBookIntegration():
    response = {
    "code": "",
    "data": [],
    "success": False,
    "error": "Address book integration may come at a later date. Sorry for the inconvenience."
    }

    return make_response(jsonify(response), 401)

def searchForUser(query):
    cnx = mysql.connector.connect(user=config.USERNAME, password=config.PASSWORD,host=config.DBHOST,database=config.DATABASE)
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT * FROM users WHERE username LIKE %s", (f"%{query}%",))
    user_row = cursor.fetchall()

    uniqueIdentifier = request.headers.get('vine-session-id')
    cursor.execute("SELECT following FROM users WHERE uniqueIdentifier = %s", (uniqueIdentifier,))
    foll = cursor.fetchone()

    following_list = []
    if foll and foll[0]:
        following_dict = json.loads(foll[0])
        following_list = following_dict.get("following", [])

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

    for row in user_row:
        user_id = str(row[0])
        is_following = False
        if user_id in following_list:
            is_following = True

        response["data"]["count"] += 1
        response["data"]["records"].append({
            "username": row[5],
            "avatarUrl": row[7],
            "location": row[8],
            "userId": row[0],
            "following": is_following
        })

    return jsonify(response)