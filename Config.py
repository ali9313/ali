# Requier Modules
from pyrogram import Client
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
import logging, time, sys, os



# Bot Configs 
class config:
    SESSION = "<PYROGRAM_SESSION>" # This Is Pyrogram Session Hers
    API_KEY = "<API_KEY>" # This is Bot API Key
    AUTH = 0000 # Sudo id
    FORCESUB = '<CHANNLS>' # Public Channls
    
    API_ID = 22119881 
    API_HASH = "95f5f60466a696e33a34f297c734d048"
    SUDO_USERS = set() # Admins List 


# Check Bot File Exists 
if not os.path.exists('./.sessions'):
    os.mkdir('./.sessions')


bot = TelegramClient('./.sessions/rad', os.environ.get("API_ID"), os.environ.get("API_HASH")).start(bot_token=os.environ.get("TOKEN")) 
userbot = Client("myacc",api_id=os.environ.get("API_ID"),api_hash=os.environ.get("API_HASH"),session_string=os.environ.get("SESSION"))

try:
    userbot.start()
except BaseException:
    sys.exit(1)


Bot = Client(
    "./.sessions/SaveRestricted",
    bot_token=os.environ.get("TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)    


try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
