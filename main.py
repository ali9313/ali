import os
import time
from telethon import TelegramClient

# استيراد جميع الوحدات الإضافية
from plugins.progress import *
from plugins.pyroplug import *
from plugins.batch import *
from plugins.frontend import *
from plugins.helpers import *

# إعدادات Telethon (ضع القيم الخاصة بك هنا)
API_ID = int(os.environ.get("API_ID"))  # ضع API_ID هنا
API_HASH = os.environ.get("API_HASH")  # ضع API_HASH هنا
BOT_TOKEN = os.environ.get("TOKEN")  # ضع توكن البوت هنا

# تعريف البوت باستخدام Telethon
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

botStartTime = time.time()

print(' Edit And Fix Error By Radfx2 Telegram : @R_AFX')

# تشغيل العمليات من ملف start.py الموجود في مجلد plugins
try:
    from plugins.start import *  # استيراد العمليات من ملف start.py
    print("Operations from start.py loaded successfully.")
except Exception as e:
    print(f"Error loading operations from plugins/start.py: {e}")

# تشغيل البوت
if __name__ == "__main__":
    print("Bot is running...")
    try:
        bot.run_until_disconnected()  # في Telethon يتم استخدام run_until_disconnected() لتشغيل البوت
    except Exception as e:
        print(f"Error running the bot: {e}")
