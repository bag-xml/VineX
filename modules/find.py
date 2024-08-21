# People-finder page

from typing import Union
from flask import Flask, request, jsonify, make_response
import mysql.connector
import bcrypt
import uuid
import config


# Will never be supported.
def twitterRecommendations():
    response = {
    "code": "",
    "data": [],
    "success": False,
    "error": "Twitter recommendations are not supported, and never will be. Sorry for the inconvenience."
    }

    return make_response(jsonify(response), 401)

def addressBookIntegration():
    response = {
    "code": "",
    "data": [],
    "success": False,
    "error": "Address book integration may come at a later date. Sorry for the inconvenience."
    }

    return make_response(jsonify(response), 401)

