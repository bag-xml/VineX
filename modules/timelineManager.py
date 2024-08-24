from typing import Union
from flask import Flask, request, jsonify, make_response
import mysql.connector
import config


# this class is responsible for handling ALL timeline endpoints

def userLikes(user_id):
    print(f"{user_id}")
    response = {
    "code": "",
    "data": [],
    "success": False,
    "error": "Sorry, this endpoint hasn't been engineered yet."
    }

    return make_response(jsonify(response), 401)


def userTimeline(user_id):
    print(f"{user_id}")
    response = {
    "code": "",
    "data": [],
    "success": False,
    "error": "Sorry, this endpoint hasn't been engineered yet."
    }

    return make_response(jsonify(response), 401)

    """# timeline endpoints
# user specific
@app.route('/timelines/users/<user_id>/likes', methods=['GET'])
def callLikePageFunction(user_id):
    return timelineManager.userLikes(user_id)

@app.route('/timelines/users/<user_id>', methods=['GET'])
def callUserTimelineRetrieval(user_id):
    return timelineManager.userLikes(user_id)"""