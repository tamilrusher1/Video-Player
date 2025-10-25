import re
from os import environ

# Bot Session Name
SESSION = environ.get('SESSION', 'streambotv1tarbot')

# Your Telegram Account Api Id And Api Hash
API_ID = int(environ.get('API_ID', '25420882'))
API_HASH = environ.get('API_HASH', 'fe9fbeabce8c3931a7796ad3fa130278')

# Bot Token, This Is Main Bot
BOT_TOKEN = environ.get('BOT_TOKEN', "8436236573:AAEBHwwsO4jLr8YrOE63-5oRl_9GDLoID-I")

# Admin Telegram Account Id For Withdraw Notification Or Anything Else
ADMIN = int(environ.get('ADMIN', '1231933846'))

# Back Up Bot Token For Fetching Message When Floodwait Comes
BACKUP_BOT_TOKEN = environ.get('BACKUP_BOT_TOKEN', "8377389837:AAH_sRck0kbESSO5RiNhlgxxDZ2cM6oSFx8")

# Log Channel, In This Channel Your All File Stored.
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1003109509751'))

# Mongodb Database For User Link Click Count Etc Data Store.
MONGODB_URI = environ.get("MONGODB_URI", "mongodb+srv://indianviolation_db_user:WQhd9XmgzDwnsJTG
@cluster0.plhmbhy.mongodb.net/?appName=Cluster0")

# Stream Url Means Your Deploy Server App Url, Here You Media Will Be Stream And Ads Will Be Shown.
STREAM_URL = environ.get("STREAM_URL", "")

# This Link Used As Permanent Link That If Your Deploy App Deleted Then You Change Stream Url, So This Link Will Redirect To Stream Url.
LINK_URL = environ.get("LINK_URL", "https://botsworldtar.blogspot.com/p/f.html")

# Others, Not Usefull
PORT = environ.get("PORT", "8080")
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
