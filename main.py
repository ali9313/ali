import time
from Config import bot  # استيراد إعدادات البوت من ملف Config
from plugins.start import *  # استيراد جميع الوحدات الإضافية
from plugins.progress import *
from plugins.pyroplug import *
from plugins.batch import *
from plugins.frontend import *
from plugins.helpers import *

# استيراد الدالة is_set_button
from plugins.helpers import is_set_button  # افترضت أن الدالة موجودة هنا

botStartTime = time.time()

print(' Edit And Fix Error By Radfx2 Telegram : @R_AFX')

if __name__ == "__main__":
    # استدعاء الدالة عند بدء التشغيل
    data = "set"  # يمكنك تعديل هذه القيمة حسب احتياجاتك
    if is_set_button(data):
        print("Button is set!")  # يمكنك استبدال هذا بعملية أخرى
    bot.run()  # في Pyrogram يتم استخدام run() لبدء البوت
