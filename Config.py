import os
import logging
import psycopg2
from telethon import TelegramClient, events
import sys

# إعدادات تسجيل الأخطاء
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# تكوين البوت
class config:
    SESSION = os.environ.get("SESSION")  # الجلسة الخاصة بحساب Telethon
    API_KEY = os.environ.get("TOKEN")    # توكن بوت Telegram
    API_ID = int(os.environ.get("API_ID"))  # API ID الخاص بحساب Telegram
    API_HASH = os.environ.get("API_HASH")  # API Hash الخاص بحساب Telegram

# إعداد اتصال قاعدة البيانات
database_url = os.environ.get("DATABASE_URL")
try:
    connection = psycopg2.connect(database_url)
    logger.info("Database connection established.")
except Exception as e:
    logger.error(f"Unable to connect to the database: {e}")
    sys.exit(1)

# إعداد اسم الجلسة
session_name = config.SESSION if config.SESSION else "my_userbot"

# تشغيل الـ Userbot من خلال Telethon باستخدام جلسة صالحة
try:
    userbot = TelegramClient(
        session_name,  # استخدام اسم الجلسة
        api_id=config.API_ID,
        api_hash=config.API_HASH
    )

    # بدء الجلسة بدون إدخال رقم الهاتف
    userbot.start()  

    # حفظ الجلسة في قاعدة البيانات
    session_string = userbot.session.save()  # الحصول على سلسلة الجلسة
    with connection.cursor() as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS sessions (name VARCHAR PRIMARY KEY, session TEXT);")
        cursor.execute("INSERT INTO sessions (name, session) VALUES (%s, %s) ON CONFLICT (name) DO UPDATE SET session = EXCLUDED.session;", (session_name, session_string))
        connection.commit()

    logger.info("Telethon Userbot started successfully and session saved to database.")
except Exception as e:
    logger.error(f"Error starting Telethon Userbot: {e}", exc_info=True)
    sys.exit(1)

# تشغيل الـ Bot باستخدام Telethon
try:
    bot = TelegramClient(
        "my_bot",  # استخدام اسم جلسة البوت
        api_id=config.API_ID,
        api_hash=config.API_HASH
    ).start(bot_token=config.API_KEY)

    logger.info("Telethon Bot started successfully.")
except Exception as e:
    logger.error(f"Error starting Telethon Bot: {e}", exc_info=True)
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
    if connection:
        connection.close()  # اغلاق الاتصال بقاعدة البيانات
