import time
from Config import bot  # استيراد إعدادات البوت من ملف Config
from plugins.start import *  # استيراد جميع الوحدات الإضافية
from plugins.progress import *
from plugins.pyroplug import *
from plugins.batch import *
from plugins.frontend import *
from plugins.helpers import *

botStartTime = time.time()

print(' Edit And Fix Error By Radfx2 Telegram : @R_AFX')

if __name__ == "__main__":
    bot.run()  # في Pyrogram يتم استخدام run() لبدء البوت
