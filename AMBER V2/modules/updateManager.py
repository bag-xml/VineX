from flask import Flask, request, jsonify, make_response
import config
import mysql.connector

def checkForUpdate(currentVersion, currentAmalgum):
    cnx = mysql.connector.connect(user=config.USERNAME, password=config.PASSWORD,host=config.DBHOST,database=config.DATABASE)
    # in our database, we have a version dictionary. Each version has an unique entry. We can kill and sign any ver we want!!!!!!!!!!!!!!!!!!
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT * FROM versionregister WHERE version = %s", (currentVersion,))
    row = cursor.fetchone()

    if row[2] == currentAmalgum:
        # good, user did not spoof version.
        if row[4] == True:
            # kill status = true
            response = {
            "update": 0,
            "kill": row[4],
            "outdateHead": "",
            "text": ""
            }
        
        if row[3] == True:
            response = {
            "update": row[3],
            "kill": 0,
            "outdateHead": "Update Available!",
            "text": row[5]
            }
        
        if row[3] + row[4] == 2:
            response = {
            "update": 0,
            "kill": 1,
            "outdateHead": "",
            "text": ""
            }
        
        if row[3] == 0:
            response = {
            "update": 0,
            "kill": 0,
            "outdateHead": "",
            "text": ""
            }
        
    else:
        response = {
            "update": 1,
            "kill": 1,
            "outdateHead": "Don't Fuck With My Service",
            "text": "You fucking idiot"
        }
    return jsonify(response)
