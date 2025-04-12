# Only for use for the hoster, specify hoster's user ID in configuration.
# Made for use with SkyGlow Notifications on iOS 6

import config
import requests

#requires SkyGlow's TCP Communicator
def send_http_request(body):
    url = "http://localhost:7878/send_data"
    payload = {
        "message": body,
        "topic": "com.vine.iphone",
        "extra": "a"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)
    print(f"HTTP request sent. Status code: {response.status_code}, Payload: {payload}")