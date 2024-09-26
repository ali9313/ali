import os
import logging
from telethon import TelegramClient, events
import sys

# إعدادات تسجيل الأخطاء
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# تكوين البوت
class config:
    SESSION = os.environ.get("SESSION")  # الجلسة الخاصة بحساب Telethon
    API_KEY = os.environ.get("TOKEN")    # توكن بوت Telegram
    API_ID = 22119881                    # API ID الخاص بحساب Telegram
    API_HASH = "95f5f60466a696e33a34f297c734d048"  # API Hash الخاص بحساب Telegram
    AUTH = 0000  # معرف المستخدم المسؤول (sudo)
    FORCESUB = 'https://t.me/u_gg_u'  # القناة العامة للاشتراك الإجباري

# التأكد من وجود مجلد الجلسات
if not os.path.exists('./.sessions'):
    os.mkdir('./.sessions')

# تشغيل الـ Userbot من خلال Telethon باستخدام جلسة صالحة
try:
    userbot = TelegramClient(
        "my_userbot",  # اسم الجلسة
        api_id=config.API_ID,
        api_hash=config.API_HASH,
        session=config.SESSION  # تأكد من أن الجلسة موجودة
    )
    userbot.start()
    logger.info("Telethon Userbot started successfully.")
except Exception as e:
    logger.error(f"Error starting Telethon Userbot: {e}")
    sys.exit(1)

# تشغيل الـ Bot باستخدام Telethon
try:
    bot = TelegramClient(
        "my_bot",  # اسم جلسة البوت
        api_id=config.API_ID,
        api_hash=config.API_HASH
    ).start(bot_token=config.API_KEY)
    
    logger.info("Telethon Bot started successfully.")
except Exception as e:
    logger.error(f"Error starting Telethon Bot: {e}")
    sys.exit(1)

# إبقاء البوت واليوزربوت يعملان
try:
    @userbot.on(events.NewMessage(pattern='/start'))
    async def start(event):
        await event.respond('Userbot and Bot are running!')

    @bot.on(events.NewMessage(pattern='/start'))
    async def bot_start(event):
        await event.respond('Bot is running!')

    # إبقاء كلا البوتين يعملان
    userbot.run_until_disconnected()
    bot.run_until_disconnected()

except KeyboardInterrupt:
    logger.info("Bot stopped manually.")
finally:
    userbot.disconnect()
    bot.disconnect()
