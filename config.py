from AstrakoBot.sample_config import Config

class Development(Config):
    OWNER_ID = 5499564416  # your telegram ID
    OWNER_USERNAME = "CORNX_OWNER"  # your telegram username
    API_KEY = "7101309513:AAFch9CExFpQXNeNTxduPCJQqAnN2uqZvjk"  # your api key, as provided by the @botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://cluuyrg340013a4me382u4t2x:95n8IsjX4KLwPg5wgUdMDsPL@104.251.218.202:9010/cluuyrg350015a4me49x20uo8'  # sample db credentials
    JOIN_LOGGER = '-1001535538162' # some group chat that your bot is a member of
    USE_JOIN_LOGGER = True
    SUDO_USERS = []  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
