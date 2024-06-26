# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os



def get_user_list(config, key):
    with open("{}/AstrakoBot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 12799559  # integer value, dont use ""
    API_HASH = "077254e69d93d08357f25bb5f4504580"
    TOKEN = "7101309513:AAFch9CExFpQXNeNTxduPCJQqAnN2uqZvjk"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 6984581562   # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "CORNX_OWNER"
    SUPPORT_CHAT = "CORNX_SUPPORT"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001535538162
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001535538162
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    ALLOW_CHATS = True

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgresql://cluuyrg340013a4me382u4t2x:95n8IsjX4KLwPg5wgUdMDsPL@104.251.218.202:9010/cluuyrg350015a4me49x20uo8"  # needed for any database modules
    DB_NAME = "cluuyrg350015a4me49x20uo8"  # needed for cron_jobs module, use same databasename from SQLALCHEMY_DATABASE_URI
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "LjgKRwr7XOKSZOvlsSajPm__of53BgJB0HdfNg4rUD9B~bozYyv296fHqPb1AqR9"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
    WEATHER_API = "b8a945b3c11262b14960cd60edb018c7"  # go to openweathermap.org/api to get key

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    SUDO_USERS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    SUPPORT_USERS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    WHITELIST_USERS = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://pixabay.com/api/docs
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    
    BACKUP_PASS = "12345" # The password used for the cron backups zip
    DROP_UPDATES = False # whether to drop the pending updates or not

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
