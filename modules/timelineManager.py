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
                    "liked": 1, # todo
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
    # current user
    uniqueIdentifer = request.headers.get('vine-session-id')

    cnx = mysql.connector.connect(user=config.USERNAME, password=config.PASSWORD,host=config.DBHOST,database=config.DATABASE)
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT * FROM posts WHERE authorID = %s", (user_id,))
    posts_row = cursor.fetchall()
    
    cursor.execute("SELECT id FROM users WHERE uniqueIdentifier = %s", (uniqueIdentifer,))
    liker_row = cursor.fetchone()

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


    for row in posts_row:
        didLike = False
        uwf_json = row[11]
        uwf_data = json.loads(uwf_json) if uwf_json else {"liked": []}
        if 'liked' in uwf_data and isinstance(uwf_data['liked'], list):
            if liker_row[0] in uwf_data['liked']:
                didLike = True

        response["data"]["count"] += 1
        response["data"]["records"].append({
            "username": row[2],
            "videoLowURL": row[4],
            "liked": didLike,
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




def loadSinglePost(post_id):
    # current user
    uniqueIdentifer = request.headers.get('vine-session-id')
    cnx = mysql.connector.connect(user=config.USERNAME, password=config.PASSWORD, host=config.DBHOST, database=config.DATABASE)
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT * FROM posts WHERE postID = %s", (post_id,))
    row = cursor.fetchone()

    cursor.execute("SELECT id FROM users WHERE uniqueIdentifier = %s", (uniqueIdentifer,))
    liker_id = cursor.fetchone()

    didLike = False
    uwf_json = row[11]
    uwf_data = json.loads(uwf_json) if uwf_json else {"liked": []}

    likes_records = []
    if 'liked' in uwf_data and isinstance(uwf_data['liked'], list):
        # Check if the current user liked the post and build the likes records
        for liker in uwf_data['liked']:
            if liker_id and liker == liker_id[0]:
                didLike = True
            cursor.execute("SELECT username, pfp, location FROM users WHERE id = %s", (liker,))
            liker_row = cursor.fetchone()
            if liker_row:
                likes_records.append({
                    "userId": liker,
                    "username": liker_row[0],
                    "avatarUrl": liker_row[1],
                    "location": liker_row[2],
                    "likeId": None,
                    "created": 1
                })

    response = {
        "code": "",
        "data": {
            "count": 1,
            "records": [{
                "username": row[2],
                "videoLowURL": row[4],
                "liked": didLike,
                "postToTwitter": 0,
                "videoUrl": row[4],
                "description": row[6],
                "created": row[7],
                "avatarUrl": row[16],
                "userId": row[1],
                "comments": {
                    "counts": 1,
                    "nextPage": None,
                    "previousPage": None,
                    "records": [
						{
							"avatarUrl": 'https://cdn.discordapp.com/avatars/574490948499800104/dabda0b41ba29cff30f6535864d2e3aa.jpeg?size=512',
							"comment": "lol lol lol lol lol lol lol lol lol lol lol lol lol lol lol lol lol lol lol lol",
							"commentId": 1,
							"created": 12,
							"location": "hell",
							"userId": 12,
							"username": "bag.xml"
						}
					],
                    "size": 10,
                },
                "thumbnailUrl": row[3],
                "foursquareVenueId": row[14],
                "likes": {
                    "count": len(likes_records),
                    "records": likes_records,
                    "nextPage": None,
                    "previousPage": None,
                    "size": 10
                },
                "postToFacebook": 0,
                "promoted": row[13],
                "verified": row[12],
                "postId": row[0],
                
                "explicitContent": 0,
                "tags": [{}],
                "location": row[5]
            }],
            "nextPage": None,
            "previousPage": None,
            "size": 20
        },
        "success": True,
        "error": ""
    }

    return jsonify(response)






""""likes": {
                "count": 10,
                "records": [
                    {
                    "avatarUrl": "",
                    "created": "2013-01-02T16:26:28.000000",
                    "likeId": 1,
                    "location": "Hell",
                    "userId": 1,
                    "username": "Daphne XML"
                    }
                ],
                "nextPage": None,
                "previousPage": None,
                "size": 10
            },"""
















































"""
{
	"code": "",
	"data": {
		"count": 1,
		"anchorStr": "1408203984",
		"records": [{
			"liked": 0,
			"videoDashUrl": "https:\/\/vine.stuffingyourfaceasusual.lol",
			"foursquareVenueId": null,
			"postFlags": 1,
			"postVerified": null,
			"userId": 52,
			"private": 0,
			"location": "test,test",
			"likes": {
				"count": 13,
				"anchorStr": "1112454214547857408",
				"records": [{
					"username": "Termy",
					"videoUrl": null,
					"verified": 1,
					"vanityUrls": [],
					"created": "2025-01-08T19:59:38.000000",
					"locale": "SE",
					"flags|platform_lo": 0,
					"userId": 3,
					"user": {
						"private": 0
					},
					"videoDashUrl": null,
					"postId": 278,
					"likeId": 318,
					"flags|platform_hi": 0
				}, {
					"username": "bruhdude",
					"videoUrl": null,
					"verified": 1,
					"vanityUrls": [],
					"created": "2025-01-08T20:13:37.000000",
					"locale": "SE",
					"flags|platform_lo": 0,
					"userId": 1,
					"user": {
						"private": 0
					},
					"videoDashUrl": null,
					"postId": 278,
					"likeId": 327,
					"flags|platform_hi": 0
				}, {
					"username": "Hyperdash",
					"videoUrl": null,
					"verified": 0,
					"vanityUrls": [],
					"created": "2025-01-08T20:20:08.000000",
					"locale": "SE",
					"flags|platform_lo": 0,
					"userId": 24,
					"user": {
						"private": 0
					},
					"videoDashUrl": null,
					"postId": 278,
					"likeId": 338,
					"flags|platform_hi": 0
				}, {
					"username": "Gab",
					"videoUrl": null,
					"verified": 1,
					"vanityUrls": [],
					"created": "2025-01-08T20:29:39.000000",
					"locale": "SE",
					"flags|platform_lo": 0,
					"userId": 6,
					"user": {
						"private": 0
					},
					"videoDashUrl": null,
					"postId": 278,
					"likeId": 344,
					"flags|platform_hi": 0
				}, {
					"username": "Hugo",
					"videoUrl": null,
					"verified": 0,
					"vanityUrls": [],
					"created": "2025-01-08T21:45:56.000000",
					"locale": "SE",
					"flags|platform_lo": 0,
					"userId": 58,
					"user": {
						"private": 0
					},
					"videoDashUrl": null,
					"postId": 278,
					"likeId": 364,
					"flags|platform_hi": 0
				}, {
					"username": "hdmi3gbi",
					"videoUrl": null,
					"verified": 0,
					"vanityUrls": [],
					"created": "2025-01-09T00:30:16.000000",
					"locale": "SE",
					"flags|platform_lo": 0,
					"userId": 62,
					"user": {
						"private": 0
					},
					"videoDashUrl": null,
					"postId": 278,
					"likeId": 389,
					"flags|platform_hi": 0
				}, {
					"username": "lek",
					"videoUrl": null,
					"verified": 0,
					"vanityUrls": [],
					"created": "2025-01-09T01:41:14.000000",
					"locale": "SE",
					"flags|platform_lo": 0,
					"userId": 59,
					"user": {
						"private": 0
					},
					"videoDashUrl": null,
					"postId": 278,
					"likeId": 400,
					"flags|platform_hi": 0
				}, {
					"username": "Battlax",
					"videoUrl": null,
					"verified": 0,
					"vanityUrls": [],
					"created": "2025-01-09T03:32:00.000000",
					"locale": "SE",
					"flags|platform_lo": 0,
					"userId": 63,
					"user": {
						"private": 0
					},
					"videoDashUrl": null,
					"postId": 278,
					"likeId": 404,
					"flags|platform_hi": 0
				}, {
					"username": "ScruffyC0rd",
					"videoUrl": null,
					"verified": 0,
					"vanityUrls": [],
					"created": "2025-01-09T08:57:02.000000",
					"locale": "SE",
					"flags|platform_lo": 0,
					"userId": 37,
					"user": {
						"private": 0
					},
					"videoDashUrl": null,
					"postId": 278,
					"likeId": 455,
					"flags|platform_hi": 0
				}, {
					"username": "walidbek6",
					"videoUrl": null,
					"verified": 0,
					"vanityUrls": [],
					"created": "2025-01-09T10:11:44.000000",
					"locale": "SE",
					"flags|platform_lo": 0,
					"userId": 68,
					"user": {
						"private": 0
					},
					"videoDashUrl": null,
					"postId": 278,
					"likeId": 465,
					"flags|platform_hi": 0
				}, {
					"username": "Valahul",
					"videoUrl": null,
					"verified": 0,
					"vanityUrls": [],
					"created": "2025-01-09T12:22:05.000000",
					"locale": "SE",
					"flags|platform_lo": 0,
					"userId": 35,
					"user": {
						"private": 0
					},
					"videoDashUrl": null,
					"postId": 278,
					"likeId": 485,
					"flags|platform_hi": 0
				}, {
					"username": "intcyro",
					"videoUrl": null,
					"verified": 0,
					"vanityUrls": [],
					"created": "2025-01-09T20:41:18.000000",
					"locale": "SE",
					"flags|platform_lo": 0,
					"userId": 78,
					"user": {
						"private": 0
					},
					"videoDashUrl": null,
					"postId": 278,
					"likeId": 543,
					"flags|platform_hi": 0
				}, {
					"username": "legacy_bomboclat",
					"videoUrl": null,
					"verified": 0,
					"vanityUrls": [],
					"created": "2025-01-10T05:24:50.000000",
					"locale": "SE",
					"flags|platform_lo": 0,
					"userId": 85,
					"user": {
						"private": 0
					},
					"videoDashUrl": null,
					"postId": 278,
					"likeId": 573,
					"flags|platform_hi": 0
				}]
			},
			"loops": {
				"count": 31,
				"velocity": 0.1,
				"onFire": 0
			},
			"thumbnailUrl": "http:\/\/uvr.a1429.lol\/dynamic\/thumbnails\/vines4u_677f2bf589d91_web.jpg",
			"explicitContent": 0,
			"myRepostId": null,
			"vanityUrls": ["no"],
			"verified": 0,
			"userBackgroundColor": "0x000000",
			"avatarUrl": "http:\/\/uvr.a1429.lol\/dynamic\/avatars\/default_avatar.png",
			"comments": {
				"count": 1,
				"anchorStr": "1112453849194823680",
				"records": [{
					"comment": "Man I missed  Zach King",
					"username": "ScruffyC0rd",
					"verified": 0,
					"avatarUrl": "http:\/\/uvr.a1429.lol\/dynamic\/avatars\/ScruffyC0rd_d38929d2fbf15875a7884ac718cd9bb9.png",
					"created": "2025-01-09T08:58:16.000000",
					"userId": 37,
					"entities": [],
					"location": "Roblox Starterplace",
					"commentId": 244,
					"user": {
						"username": "ScruffyC0rd",
						"verified": 0,
						"description": "I love The good old dayz",
						"avatarUrl": "http:\/\/uvr.a1429.lol\/dynamic\/avatars\/ScruffyC0rd_d38929d2fbf15875a7884ac718cd9bb9.png",
						"userId": 37,
						"location": "Roblox Starterplace",
						"explicitContent": null
					}
				}]
			},
			"entities": [],
			"videoLowURL": "http:\/\/uvr.a1429.lol\/dynamic\/videos\/vines4u_677f2bf589d91_web_resized.mp4",
			"permalinkUrl": "https:\/\/vine.stuffingyourfaceasusual.lol",
			"username": "vines4u",
			"description": "",
			"tags": [],
			"postId": 278,
			"videoUrl": "http:\/\/uvr.a1429.lol\/dynamic\/videos\/vines4u_677f2bf589d91_web_resized.mp4",
			"created": "2025-01-09T01:52:54.000000",
			"shareUrl": "https:\/\/uvr.a1429.lol\/watch\/278",
			"profileBackground": "0x5082e5",
			"promoted": 0,
			"reposts": {
				"count": null,
				"anchorStr": "1112454163276697600",
				"records": [{
					"username": "lek",
					"avatarUrl": "http:\/\/uvr.a1429.lol\/dynamic\/avatars\/lek_app_677f583b3b92d.jpg",
					"videoUrl": null,
					"verified": 0,
					"created": "2025-01-09T01:41:17.000000",
					"createdAt": "2025-01-09T01:41:17.000000",
					"description": "Just Chilling All Time !",
					"location": "Lansaka ,Thailand",
					"userId": 59,
					"priv": 0,
					"unflaggable": 0,
					"postId": 278,
					"repostId": 87
				}]
			}
		}]
	},
	"previousPage": null,
	"backAnchor": "",
	"anchor": "",
	"nextPage": 0,
	"size": 1,
	"success": true,
	"error": ""
}
"""