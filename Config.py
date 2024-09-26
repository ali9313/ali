# Requier Modules
from pyrogram import Client
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
import logging, time, sys, os



# Bot Configs 
class config:
    SESSION = "AgGB5kgAcmFmW_pZRaTLtQOCK_r798RWaH1aTjVGwhqtezv3pAKGS8Q3XVJT3Gw5_jrbjt1TC0QePJE0wXPm2Tlpw0MBD8OO3p680ncEepjAqIyVzOHiAepUGzCLMuO7gI3rTdqV1lWF9cJE8WaQ9qKRhL4gEkVeYDjHFlOCrxT6d1TMzb5TZuHPDwXAzDrutLkPIHP1AxlDGHEweThE3tuEwFIaU_wJpO9jupc71JWNkPTNC-QGCKMdKXTZT130htXxu-3UkEcsvYR7FA88MofwSAi7TrrdvZyxKhVneQd17FXJn_a1gVuBuSLHPq8kleDYHBvTIIB8M7GiWUv5aSfM7PQymgAAAAAN26noAA" # This Is Pyrogram Session Hers
    API_KEY = "7260017955:AAEDZOsfFEpqb4u5EEkU1jWkocf1-rIJ5-U" # This is Bot API Key
    AUTH = 0000 # Sudo id
    FORCESUB = 'https://t.me/u_gg_u' # Public Channls
    
    API_ID = 22119881 
    API_HASH = "95f5f60466a696e33a34f297c734d048"
    SUDO_USERS = set() # Admins List 


# Check Bot File Exists 
if not os.path.exists('./.sessions'):
    os.mkdir('./.sessions')


bot = TelegramClient('./.sessions/rad', config.API_ID, config.API_HASH).start(bot_token=config.API_KEY) 
userbot = Client("myacc",api_id=config.API_ID,api_hash=config.API_HASH,session_string=config.SESSION)

try:
    userbot.start()
except BaseException:
    sys.exit(1)


Bot = Client(
    "./.sessions/SaveRestricted",
    bot_token=config.API_KEY,
    api_id=int(config.API_ID),
    api_hash=config.API_HASH
)    


try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
