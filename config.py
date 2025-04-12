"""
-- -- -- configuration -- -- --
    -- -- VineXServer -- --
         -- bag.xml --
        -- 2024-08-17 --
"""


# Version and name, will be reported back in logs

AUTHOR = "XML"
NAME = "XineServer"
VERSION = "development"

# Networking
PORT = "5001"
HOST = "0.0.0.0"

# Database
USERNAME = "root"
PASSWORD = ""
DBHOST = "127.0.0.1"
DATABASE = "VineXDB"

# Push Notifications (optional)
# If you're the hoster, and coincidentally know how to use "SkyGlow Notifications", a custom push notifications tweak at https://cydia.skyglow.es, I recommend enabling this for extra authenticity.
# If you don't want to enable this, leave as is.
# Please specify your user id here
ENABLE_ADMIN_PUSHNOTIFS = True
HOSTER_USERID = 11

