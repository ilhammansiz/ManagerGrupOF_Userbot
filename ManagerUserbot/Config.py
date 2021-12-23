import os

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", 6))
    API_HASH = os.environ.get("API_HASH", None)
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    BOT_US = os.environ.get("BOT_US", None)
    WELCOME_TEXT = os.environ.get("WELCOME_TEXT", None)
    RULES = os.environ.get("RULES", None)
