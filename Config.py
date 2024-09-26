# Requier Modules
from pyrogram import Client
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
import logging, time, sys, os



# Bot Configs 
class config:
    SESSION = "AgGB5kgAVdRYtsP1UkUlhNimiNACXHYARn12iVDZQGikoitpWWQGCKQ9LzfDradUYqIQFVbdbv9vp2bvsHIw8q93B9bTwJs_-1lO3MZrx3tR5m30o79HoWXUQCt25wM8kr3kRBeK8LhNa6W9jaf0qkOVk1crAECQzaeIlaZkqTiuB712ErD3CDwhtQflgn70r-NlYhi64K5FqNjWJap5lvLxjRSIiTrhnrPn-3Obp_FFhXCpsluL8RxdbbOQaSYWS7LqAqvn0F17Jdxu8pTkXcx16H9s60C7HrP1C9Idl7uMc7_rAL-4Nuv6nPEFz7_DMZfkNb4N2RJhSguhfoACBTbpN2mmdAAAAAAN26noAA" # This Is Pyrogram Session Hers
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
