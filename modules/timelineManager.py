from typing import Union
from flask import Flask, request, jsonify, make_response
import mysql.connector
import config
import json


# this class is responsible for handling ALL timeline endpoints

def userLikes(user_id):
    cnx = mysql.connector.connect(user=config.USERNAME, password=config.PASSWORD,host=config.DBHOST,database=config.DATABASE)
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT likedPosts FROM users WHERE id = %s", (user_id,))
    row = cursor.fetchone()

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


    if row:
        liked_dict = json.loads(row[0])
        likers_list = liked_dict.get('liked_posts', [])

        if likers_list:
            likers_list = [int(post_id) for post_id in likers_list]
            format_strings = ','.join(['%s'] * len(likers_list))

            query = f"SELECT postID, authorID, authorName, thumbnailURL, videoURL, location, description, creationDate, comments, likes, tags, usersWhoLiked, verified, promoted, postToFacebook, foursquareVenueID, authorPFP FROM posts WHERE postID IN ({format_strings})"
            cursor.execute(query, tuple(likers_list))
            liked_posts = cursor.fetchall()

            for post in liked_posts:
                response["data"]["count"] += 1
                response["data"]["records"].append({
                    "username": post[2],
                    "videoLowURL": post[4],
                    "liked": 1,
                    "postToTwitter": 0,
                    "videoUrl": post[4],
                    "description": post[6],
                    "created": post[7],
                    "avatarUrl": post[16],
                    "userId": post[1],
                    "comments": {
                        "count": 1,
                        "records": [],
                        "nextPage": None,
                        "previousPage": None,
                        "size": 0
                    },
                    "thumbnailUrl": post[3],
                    "foursquareVenueId": post[15],
                    "likes": {
                        "count": 0,
                        "records": [],
                        "nextPage": None,
                        "previousPage": None,
                        "size": 10
                    },
                    "postToFacebook": post[14],
                    "promoted": post[13],
                    "verified": post[12],
                    "postId": post[0],
                    "explicitContent": 0,
                    "tags": [{}],
                    "location": post[5]
                })
    cursor.close()
    cnx.close()

    
    return jsonify(response)



def userTimeline(user_id):
    cnx = mysql.connector.connect(user=config.USERNAME, password=config.PASSWORD,host=config.DBHOST,database=config.DATABASE)
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT * FROM posts WHERE authorID = %s", (user_id,))
    posts_row = cursor.fetchall()

    response = {
        "code": "",
        "data": {
            "count": 0,
            "records": [],
            "nextPage": 1,
            "previousPage": None,
            "size": 250
        },
        "success": True,
        "error": ""
    }

    for row in posts_row:
        response["data"]["count"] += 1
        response["data"]["records"].append({
            "username": row[2],
            "videoLowURL": row[4],
            "liked": 1,
            "postToTwitter": 0,
            "videoUrl": row[4],
            "description": row[6],
            "created": row[7],
            "avatarUrl": row[16],
            "userId": row[1],
            "comments": {
                "count": 1,
                "records": [], #ssoonn
                "nextPage": None,
                "previousPage": None,
                "size": 0
            },
            "thumbnailUrl": row[3],
            "foursquareVenueId": row[15],
            "likes": {
                "count": 0,
                "records": [], #coming soon
                "nextPage": None,
                "previousPage": None,
                "size": 10
            },
            "postToFacebook": row[14],
            "promoted": row[13],
            "verified": row[12],
            "postId": row[0],
            "explicitContent": 0,
            "tags": [{}],
            "location": row[5]
    })


    return jsonify(response)




























































"""
response = {
    "code": "",
    "data": {
        "count": 18,
        "records": [{
            "username": "Alex",
            "videoLowURL": "https://bag-xml.com",
            "liked": 1,
            "postToTwitter": 0,
            "videoUrl": "https://bag-xml.com",
            "description": "My #design project. The theme for my calendar is #mustaches #tribalprint #pattern and #handmade",
            "created": "2013-01-29T13:51:02.000000",
            "avatarUrl": "avatar url",
            "userId": 123456789,
            "comments": {
                "count": 1,
                "records": [
                    {
                        "avatarUrl": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTS7Co_QnaZxKJNSGG4Wfy6fGOtzvDoBWxCN8e4DteeklxYnvXw",
                        "comment": "penis",
                        "commentId": 3123123123,
                        "created": "NA",
                        "location": "Brooklyn, NY",
                        "userId": 2,
                        "username": "bag.xml"
                    }
                ],
                "nextPage": None,
                "previousPage": None,
                "size": 10
            },
            "thumbnailUrl": "wtf",
            "foursquareVenueId": None,
            "likes": {
                "count": 0,
                "records": [],
                "nextPage": None,
                "previousPage": None,
                "size": 10
            },
            "postToFacebook": 0,
            "promoted": 0,
            "verified": 0,
            "postId": 123456789,
            "explicitContent": 0,
            "tags": [{
                "tagId": 123456789,
                "tag": "design"
            }],
            "location": None
        }],
        "nextPage": None,
        "previousPage": None,
        "size": 20
    },
    "success": True,
    "error": ""
    }
    """
"""
def sampleRetrieve():
    response = {
    "code": "",
    "data": {
        "count": 18,
        "records": [{
            "username": "Alex",
            "videoLowURL": "https://bag-xml.com",
            "liked": 1,
            "postToTwitter": 0,
            "videoUrl": "https://bag-xml.com",
            "description": "My #design project. The theme for my calendar is #mustaches #tribalprint #pattern and #handmade",
            "created": "2013-01-29T13:51:02.000000",
            "avatarUrl": "avatar url",
            "userId": 123456789,
            "comments": {
                "count": 1,
                "records": [
                    {
                        "avatarUrl": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTS7Co_QnaZxKJNSGG4Wfy6fGOtzvDoBWxCN8e4DteeklxYnvXw",
                        "comment": "penis",
                        "commentId": 3123123123,
                        "created": "NA",
                        "location": "Brooklyn, NY",
                        "userId": 2,
                        "username": "bag.xml"
                    }
                ],
                "nextPage": None,
                "previousPage": None,
                "size": 10
            },
            "thumbnailUrl": "wtf",
            "foursquareVenueId": None,
            "likes": {
                "count": 0,
                "records": [],
                "nextPage": None,
                "previousPage": None,
                "size": 10
            },
            "postToFacebook": 0,
            "promoted": 0,
            "verified": 0,
            "postId": 1234567890,
            "explicitContent": 0,
            "tags": [{
                "tagId": 123456789,
                "tag": "design"
            }],
            "location": None
        },
        {
            "username": "Alex",
            "videoLowURL": "https://bag-xml.com",
            "liked": 1,
            "postToTwitter": 0,
            "videoUrl": "https://bag-xml.com",
            "description": "My #design project. The theme for my calendar is #mustaches #tribalprint #pattern and #handmade",
            "created": "2013-01-29T13:51:02.000000",
            "avatarUrl": "avatar url",
            "userId": 123456789,
            "comments": {
                "count": 1,
                "records": [
                    {
                        "avatarUrl": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTS7Co_QnaZxKJNSGG4Wfy6fGOtzvDoBWxCN8e4DteeklxYnvXw",
                        "comment": "penis",
                        "commentId": 3123123123,
                        "created": "NA",
                        "location": "Brooklyn, NY",
                        "userId": 2,
                        "username": "bag.xml"
                    }
                ],
                "nextPage": None,
                "previousPage": None,
                "size": 10
            },
            "thumbnailUrl": "wtf",
            "foursquareVenueId": None,
            "likes": {
                "count": 0,
                "records": [],
                "nextPage": None,
                "previousPage": None,
                "size": 10
            },
            "postToFacebook": 0,
            "promoted": 0,
            "verified": 0,
            "postId": 1234567567589,
            "explicitContent": 0,
            "tags": [{
                "tagId": 123456789,
                "tag": "design"
            }],
            "location": None
        },
        {
            "username": "Alex",
            "videoLowURL": "https://bag-xml.com",
            "liked": 1,
            "postToTwitter": 0,
            "videoUrl": "https://bag-xml.com",
            "description": "My #design project. The theme for my calendar is #mustaches #tribalprint #pattern and #handmade",
            "created": "2013-01-29T13:51:02.000000",
            "avatarUrl": "avatar url",
            "userId": 123456789,
            "comments": {
                "count": 1,
                "records": [
                    {
                        "avatarUrl": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTS7Co_QnaZxKJNSGG4Wfy6fGOtzvDoBWxCN8e4DteeklxYnvXw",
                        "comment": "penis",
                        "commentId": 3123123123,
                        "created": "NA",
                        "location": "Brooklyn, NY",
                        "userId": 2,
                        "username": "bag.xml"
                    }
                ],
                "nextPage": None,
                "previousPage": None,
                "size": 10
            },
            "thumbnailUrl": "wtf",
            "foursquareVenueId": None,
            "likes": {
                "count": 0,
                "records": [],
                "nextPage": None,
                "previousPage": None,
                "size": 10
            },
            "postToFacebook": 0,
            "promoted": 0,
            "verified": 0,
            "postId": 123451236789,
            "explicitContent": 0,
            "tags": [{
                "tagId": 123456789,
                "tag": "design"
            }],
            "location": None
        },
        {
            "username": "Alex",
            "videoLowURL": "https://bag-xml.com",
            "liked": 1,
            "postToTwitter": 0,
            "videoUrl": "https://bag-xml.com",
            "description": "My #design project. The theme for my calendar is #mustaches #tribalprint #pattern and #handmade",
            "created": "2013-01-29T13:51:02.000000",
            "avatarUrl": "avatar url",
            "userId": 123456789,
            "comments": {
                "count": 1,
                "records": [
                    {
                        "avatarUrl": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTS7Co_QnaZxKJNSGG4Wfy6fGOtzvDoBWxCN8e4DteeklxYnvXw",
                        "comment": "penis",
                        "commentId": 3123123123,
                        "created": "NA",
                        "location": "Brooklyn, NY",
                        "userId": 2,
                        "username": "bag.xml"
                    }
                ],
                "nextPage": None,
                "previousPage": None,
                "size": 10
            },
            "thumbnailUrl": "wtf",
            "foursquareVenueId": None,
            "likes": {
                "count": 0,
                "records": [],
                "nextPage": None,
                "previousPage": None,
                "size": 10
            },
            "postToFacebook": 0,
            "promoted": 0,
            "verified": 0,
            "postId": 123411111156789,
            "explicitContent": 0,
            "tags": [{
                "tagId": 123456789,
                "tag": "design"
            }],
            "location": None
        },
        {
            "username": "Alex",
            "videoLowURL": "https://bag-xml.com",
            "liked": 1,
            "postToTwitter": 0,
            "videoUrl": "https://bag-xml.com",
            "description": "My #design project. The theme for my calendar is #mustaches #tribalprint #pattern and #handmade",
            "created": "2013-01-29T13:51:02.000000",
            "avatarUrl": "avatar url",
            "userId": 123456789,
            "comments": {
                "count": 1,
                "records": [
                    {
                        "avatarUrl": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTS7Co_QnaZxKJNSGG4Wfy6fGOtzvDoBWxCN8e4DteeklxYnvXw",
                        "comment": "penis",
                        "commentId": 3123123123,
                        "created": "NA",
                        "location": "Brooklyn, NY",
                        "userId": 2,
                        "username": "bag.xml"
                    }
                ],
                "nextPage": None,
                "previousPage": None,
                "size": 10
            },
            "thumbnailUrl": "wtf",
            "foursquareVenueId": None,
            "likes": {
                "count": 0,
                "records": [],
                "nextPage": None,
                "previousPage": None,
                "size": 10
            },
            "postToFacebook": 0,
            "promoted": 0,
            "verified": 0,
            "postId": 1234567790900089,
            "explicitContent": 0,
            "tags": [{
                "tagId": 123456789,
                "tag": "design"
            }],
            "location": None
        },
        {
            "username": "Alex",
            "videoLowURL": "https://bag-xml.com",
            "liked": 1,
            "postToTwitter": 0,
            "videoUrl": "https://bag-xml.com",
            "description": "My #design project. The theme for my calendar is #mustaches #tribalprint #pattern and #handmade",
            "created": "2013-01-29T13:51:02.000000",
            "avatarUrl": "avatar url",
            "userId": 123456789,
            "comments": {
                "count": 1,
                "records": [
                    {
                        "avatarUrl": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTS7Co_QnaZxKJNSGG4Wfy6fGOtzvDoBWxCN8e4DteeklxYnvXw",
                        "comment": "penis",
                        "commentId": 3123123123,
                        "created": "NA",
                        "location": "Brooklyn, NY",
                        "userId": 2,
                        "username": "bag.xml"
                    }
                ],
                "nextPage": None,
                "previousPage": None,
                "size": 10
            },
            "thumbnailUrl": "wtf",
            "foursquareVenueId": None,
            "likes": {
                "count": 0,
                "records": [],
                "nextPage": None,
                "previousPage": None,
                "size": 10
            },
            "postToFacebook": 0,
            "promoted": 0,
            "verified": 0,
            "postId": 1234565675767789,
            "explicitContent": 0,
            "tags": [{
                "tagId": 123456789,
                "tag": "design"
            }],
            "location": None
        }],
        "nextPage": None,
        "previousPage": None,
        "size": 20
    },
    "success": True,
    "error": ""
    }

    
    return jsonify(response), 200"""