import os
import logging
import psycopg2
from telethon import TelegramClient, events
import sys

# استيراد العمليات من ملف main.py
import main  # افترض أن main.py يحتوي على دوال تريد تشغيلها بعد الحفظ

# إعدادات تسجيل الأخطاء (تسجيل الأخطاء فقط)
logging.basicConfig(level=logging.ERROR)
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
    # لا تعرض رسالة عند نجاح الاتصال بقاعدة البيانات
except Exception as e:
    logger.error(f"Unable to connect to the database: {e}")
    sys.exit(1)

# إعداد اسم الجلسة
session_name = config.SESSION if config.SESSION else "my_userbot"

# تشغيل الـ Userbot من خلال Telethon باستخدام جلسة صالحة
try:
    userbot = TelegramClient(
        session_name,  
        api_id=config.API_ID,
        api_hash=config.API_HASH
    )

    userbot.start()  

    # حفظ الجلسة في قاعدة البيانات
    session_string = userbot.session.save()  
    with connection.cursor() as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS sessions (name VARCHAR PRIMARY KEY, session TEXT);")
        cursor.execute("INSERT INTO sessions (name, session) VALUES (%s, %s) ON CONFLICT (name) DO UPDATE SET session = EXCLUDED.session;", (session_name, session_string))
        connection.commit()

    # بعد نجاح حفظ الجلسة، استدعاء العمليات من ملف main.py
    main.run_operations()  # افترض أن لديك دالة run_operations في ملف main.py

except Exception as e:
    logger.error(f"Error starting Telethon Userbot: {e}", exc_info=True)
    sys.exit(1)

# أكمل باقي الكود لتشغيل الـ Bot ...
