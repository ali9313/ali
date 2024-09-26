import os
import logging
from pyrogram import Client, idle
import sys

# إعدادات تسجيل الأخطاء
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# تكوين البوت
class config:
    SESSION = os.environ.get("SESSION")  # الجلسة الخاصة بحساب Pyrogram
    API_KEY = os.environ.get("TOKEN")    # توكن بوت Telegram
    API_ID = 22119881                    # API ID الخاص بحساب Telegram
    API_HASH = "95f5f60466a696e33a34f297c734d048"  # API Hash الخاص بحساب Telegram
    AUTH = 0000  # معرف المستخدم المسؤول (sudo)
    FORCESUB = 'https://t.me/u_gg_u'  # القناة العامة للاشتراك الإجباري

# التأكد من وجود مجلد الجلسات
if not os.path.exists('./.sessions'):
    os.mkdir('./.sessions')

# تشغيل الـ Userbot من خلال Pyrogram باستخدام جلسة صالحة
try:
    userbot = Client(
        "my_userbot",  # اسم الجلسة
        api_id=config.API_ID,
        api_hash=config.API_HASH,
        session_string=config.SESSION
    )
    userbot.start()
    logger.info("Pyrogram Userbot started successfully.")
except Exception as e:
    logger.error(f"Error starting Pyrogram Userbot: {e}")
    sys.exit(1)

# تشغيل الـ Bot باستخدام Pyrogram
try:
    Bot = Client(
        "my_bot",  # اسم جلسة البوت
        bot_token=config.API_KEY,
        api_id=config.API_ID,
        api_hash=config.API_HASH
    )
    Bot.start()
    logger.info("Pyrogram Bot started successfully.")
except Exception as e:
    logger.error(f"Error starting Pyrogram Bot: {e}")
    sys.exit(1)

# إبقاء البوت واليوزربوت يعملان
try:
    idle()  # يستخدم لإبقاء كلا من الـ Userbot والـ Bot قيد التشغيل
except KeyboardInterrupt:
    logger.info("Bot stopped manually.")
finally:
    userbot.stop()
    Bot.stop()
