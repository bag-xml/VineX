from flask import Flask, request, jsonify, make_response
import config
import mysql.connector

def loadHomeFeed():
    cnx = mysql.connector.connect(user=config.USERNAME, password=config.PASSWORD,host=config.DBHOST,database=config.DATABASE)
    # adding posts this way is a heck of a lot more convenient
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT * FROM notforever")
    rows = cursor.fetchall()

    response = {
    'posts': []
    }

    for row in rows:
        # Add each post to the response list
        response['posts'].append({
            'date': row[3],
            'title': row[1],
            'user': {
                "username": row[2]
            },
            'id': row[0],
            'type': None,
            'text': row[4],

        })

    cursor.close()
    cnx.close()

    return jsonify(response)

    """response = {
    'posts': [
        {
            'name': 'bag.xml',
            'date': '2024-07-04',
            'text': 'Development on the first version of MobileMali is almost done! Soon there will be tests...',
            'title': 'Test Release',
            'id': '1'
        },
        {
            'name': 'bag.xml',
            'date': '2024-06-19',
            'text': 'Welcome to MobileMali! Here you can get local news and updates on projects right on your iOS device!',
            'title': 'Welcome!',
            'id': '1'
        }
    ]
}

    return jsonify(response)"""

def loadRecentsFeed():
    cnx = mysql.connector.connect(user=config.USERNAME, password=config.PASSWORD,host=config.DBHOST,database=config.DATABASE)
    # adding posts this way is a heck of a lot more convenient
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT * FROM posts WHERE recent = 1")
    rows = cursor.fetchall()

    response = {
    'posts': []
    }

    for row in rows:
        # Add each post to the response list
        response['posts'].append({
            'date': row[4],
            'title': row[2],
            'name': row[3],
            'id': row[0],
            'imageURL': row[7],
        })

    cursor.close()
    cnx.close()

    return jsonify(response)

def loadBlogsFeed():
    cnx = mysql.connector.connect(user=config.USERNAME, password=config.PASSWORD,host=config.DBHOST,database=config.DATABASE)
    # adding posts this way is a heck of a lot more convenient
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT * FROM posts WHERE recent = 0")
    rows = cursor.fetchall()

    response = {
    'posts': []
    }

    for row in rows:
        # Add each post to the response list
        response['posts'].append({
            'date': row[4],
            'title': row[2],
            'name': row[3],
            'id': row[0],
            'thumbnail': row[7],
            'text': row[6]
        })

    cursor.close()
    cnx.close()

    return jsonify(response)