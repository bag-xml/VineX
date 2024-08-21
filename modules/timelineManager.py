from typing import Union
from flask import Flask, request, jsonify, make_response
import mysql.connector
import config

cnx = mysql.connector.connect(user=config.USERNAME, password=config.PASSWORD,host=config.DBHOST,database=config.DATABASE)

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