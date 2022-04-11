import os

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

class var:
    BOT_TOKEN = os.getenv("BOT_TOKEN")  # from @botfather
    API_ID = int(os.getenv("API_ID"))  # from https://my.telegram.org/apps
    API_HASH = os.getenv("API_HASH")  # from https://my.telegram.org/apps
    START_MESSAGE = os.getenv("START_MESSAGE", None)  # Not Mandatory
    OWNER_ID = os.getenv("OWNER_ID", None)
    ENVIRONMENT = os.getenv("ENVIRONMENT")
    MUST_JOIN = os.getenv("MUST_JOIN")
