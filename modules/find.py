# People-finder page

from typing import Union
from flask import Flask, request, jsonify, make_response
import mysql.connector
import uuid
import config



def addressBookIntegration():
    response = {
    "code": "",
    "data": [],
    "success": False,
    "error": "Address book integration may come at a later date. Sorry for the inconvenience."
    }

    return make_response(jsonify(response), 401)

