import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# تفعيل تسجيل الأخطاء
logging.basicConfig(level=logging.INFO)

# إدخال البيانات المطلوبة مباشرة داخل الكود
API_ID = 1747534  # ضع API_ID هنا
API_HASH = "5a2684512006853f2e48aca9652d83ea"  # ضع API_HASH هنا
BOT_TOKEN = "7260017955:AAEDZOsfFEpqb4u5EEkU1jWkocf1-rIJ5-U"  # ضع توكن البوت هنا

# تعريف البوت
gagan = Client(
    "my_bot",
    api_id=API_ID,  # استخدام API_ID مباشرة
    api_hash=API_HASH,  # استخدام API_HASH مباشرة
    bot_token=BOT_TOKEN  # استخدام توكن البوت مباشرة
)

TEXT = "أرسل رابط المنشور فقط من قناة أو مجموعة عامة 📇.\n\n - لشرح البوت ارسل: /help"

# التعامل مع الأمر /start
@gagan.on_message(filters.command("start"))
async def start_command(client, message):
    print(f"Bot is working! Received /start from {message.from_user.id}")
    
    buttons = [
        [InlineKeyboardButton("R A D", url="t.me/r_afx")]
    ]
    
    await message.reply_text(
        TEXT,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

# التعامل مع الأمر /help
@gagan.on_message(filters.command("help"))
async def help_command(client, message):
    buttons = [
        [InlineKeyboardButton("R A D", url="t.me/r_afx")]
    ]
    
    help_text = """
        - خطوات استخدام البوت:
        1- إذا كانت المجموعة أو القناة عامة ولكن مقيدة، سيتمكن البوت من جلب المنشور بكل بساطة وسهولة.
        
        2- إذا كانت القناة أو المجموعة خاصة، أضف البوت يدويًا ثم قم بترقيته إلى أدمن.
        
        🆕 » التحديث الجديد: إذا كانت القناة خاصة، أرسل للبوت رابط الدعوة وسيتمكن البوت من جلب المحتوى.
    """
    
    await message.reply_text(
        help_text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

# تشغيل البوت
print("Bot is running...")
gagan.run()
