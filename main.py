import os
import time
from telethon import TelegramClient
from plugins.start import *  # استيراد جميع الوحدات الإضافية
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

# تشغيل البوت
if __name__ == "__main__":
    print("Bot is running...")
    bot.run_until_disconnected()  # في Telethon يتم استخدام run_until_disconnected() لتشغيل البوت
