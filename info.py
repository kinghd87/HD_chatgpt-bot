# ©️biisal jai shree krishna 😎
from os import environ
from dotenv import load_dotenv

load_dotenv()

API_ID = environ.get("API_ID" , "23340169")
API_HASH = environ.get("API_HASH" , "4e600e23e419b9cffd280ee2791c273a")
BOT_TOKEN = environ.get("BOT_TOKEN" , "8217509079:AAEY3LgU3o4W36mOhAURCN0xjVipK7u-ofc")
ADMIN = int(environ.get("ADMIN" , "7409967984"))
CHAT_GROUP = int(environ.get("CHAT_GROUP", "-1003002158481"))
LOG_CHANNEL = environ.get("LOG_CHANNEL", "-1002569365457")
MONGO_URL = environ.get("MONGO_URL" , "mongodb://localhost:27017")
AUTH_CHANNEL = int(
    environ.get("AUTH_CHANNEL", "-1001734958816")
)
FSUB = environ.get("FSUB", True)
STICKERS_IDS = (
    "CAACAgQAAxkBAAEK99dlfC7LDqnuwtGRkIoacot_dGC4zQACbg8AAuHqsVDaMQeY6CcRojME"
).split()
COOL_TIMER = 20  # keep this atleast 20
ONLY_SCAN_IN_GRP = environ.get(
    "ONLY_SCAN_IN_GRP", True
)  # If IMG_SCAN_IN_GRP is set to True, image scanning is restricted to your support group only. If it's False, the image scanning feature can be used anywhere.
REACTIONS = ["❤️‍🔥", "⚡", "🔥"]


