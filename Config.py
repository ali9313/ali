import os
import logging
from telethon import TelegramClient
import sys

# إعدادات تسجيل الأخطاء (تسجيل الأخطاء فقط)
logging.basicConfig(level=logging.ERROR)  # تغيير مستوى التسجيل إلى ERROR لتقليل الإشعارات
logger = logging.getLogger(__name__)

# تكوين البوت
class config:
    SESSION = os.environ.get("SESSION")  # الجلسة الخاصة بحساب Telethon
    API_KEY = os.environ.get("TOKEN")    # توكن بوت Telegram
    API_ID = int(os.environ.get("API_ID"))  # API ID الخاص بحساب Telegram
    API_HASH = os.environ.get("API_HASH")  # API Hash الخاص بحساب Telegram

# إعداد اسم الجلسة
session_name = config.SESSION if config.SESSION else "my_userbot"
session_file_path = f"{session_name}.session"  # تحديد مسار ملف الجلسة

# تشغيل الـ Userbot من خلال Telethon باستخدام جلسة صالحة
try:
    userbot = TelegramClient(
        session_file_path,  # استخدام مسار الملف بدلاً من اسم الجلسة
        api_id=config.API_ID,
        api_hash=config.API_HASH
    )

    userbot.start()  

    # حفظ الجلسة في ملف
    session_string = userbot.session.save()  
    with open(session_file_path, 'w') as session_file:
        session_file.write(session_string)

    # بعد نجاح حفظ الجلسة، استدعاء العمليات من ملف main.py
    main.run_operations()  # افترض أن لديك دالة run_operations في ملف main.py

except Exception as e:
    logger.error(f"Error starting Telethon Userbot: {e}", exc_info=True)
    sys.exit(1)

# أكمل باقي الكود لتشغيل الـ Bot ...
