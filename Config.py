import os
import logging
from telethon import TelegramClient, events
import sys
import subprocess

# إعدادات تسجيل الأخطاء
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# تكوين البوت
class config:
    SESSION = os.environ.get("SESSION")  # الجلسة الخاصة بحساب Telethon
    API_KEY = os.environ.get("TOKEN")    # توكن بوت Telegram
    API_ID = 22119881                    # API ID الخاص بحساب Telegram
    API_HASH = "95f5f60466a696e33a34f297c734d048"  # API Hash الخاص بحساب Telegram

# التأكد من وجود مجلد الجلسات
session_dir = os.path.abspath('./.sessions')
if not os.path.exists(session_dir):
    os.mkdir(session_dir)
    logger.info("Session directory created.")

# منح الأذونات اللازمة للكتابة في المجلد
try:
    subprocess.run(["chmod", "755", session_dir], check=True)
    logger.info("Write permissions granted for the session directory.")
except Exception as e:
    logger.error(f"Failed to set permissions: {e}")

# إعداد اسم الجلسة
session_name = config.SESSION if config.SESSION else "my_userbot"  # استخدام الجلسة من البيئة أو اسم افتراضي
session_file_path = os.path.join(session_dir, session_name)

# تشغيل الـ Userbot من خلال Telethon باستخدام جلسة صالحة
try:
    userbot = TelegramClient(
        session_file_path,  # استخدام المسار
        api_id=config.API_ID,
        api_hash=config.API_HASH
    )
    
    userbot.start()  # بدء الجلسة بدون إدخال رقم الهاتف
    logger.info("Telethon Userbot started successfully.")
except Exception as e:
    logger.error(f"Error starting Telethon Userbot: {e}")
    sys.exit(1)

# تشغيل الـ Bot باستخدام Telethon
try:
    bot = TelegramClient(
        os.path.join(session_dir, "my_bot"),  # استخدام مسار الجلسة
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
        await event.respond('Userbot is running!')

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
