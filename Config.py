from pyrogram import Client
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
import logging, time, sys, os

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Bot Configs 
class config:
    SESSION = os.environ.get("SESSION")  # This Is Pyrogram Session Here
    API_KEY = os.environ.get("TOKEN")  # This is Bot API Key
    AUTH = 0000  # Sudo id
    FORCESUB = 'https://t.me/u_gg_u'  # Public Channel
    
    API_ID = 22119881 
    API_HASH = "95f5f60466a696e33a34f297c734d048"
    SUDO_USERS = set()  # Admins List 

# Check if sessions directory exists 
if not os.path.exists('./.sessions'):
    os.mkdir('./.sessions')

# Telethon Bot client
try:
    bot = TelegramClient('./.sessions/rad', config.API_ID, config.API_HASH).start(bot_token=config.API_KEY) 
    logger.info("Telethon Bot started successfully.")
except Exception as e:
    logger.error(f"Error starting Telethon bot: {e}")
    sys.exit(1)

# Pyrogram Userbot client
try:
    userbot = Client("myacc", api_id=config.API_ID, api_hash=config.API_HASH, session_string=config.SESSION)
    userbot.start()
    logger.info("Pyrogram Userbot started successfully.")
except Exception as e:
    logger.error(f"Error starting Pyrogram Userbot: {e}")
    sys.exit(1)

# Pyrogram Bot client
try:
    Bot = Client(
        "./.sessions/SaveRestricted",
        bot_token=config.API_KEY,
        api_id=int(config.API_ID),
        api_hash=config.API_HASH
    )    
    Bot.start()
    logger.info("Pyrogram Bot started successfully.")
except Exception as e:
    logger.error(f"Error starting Pyrogram bot: {e}")
    sys.exit(1)
