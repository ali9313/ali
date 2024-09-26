import os
from config import *
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# تعريف البوت
gagan = Client(
    "my_bot",
    api_id=int(os.getenv("API_ID")),  # ضع API_ID هنا
    api_hash=os.getenv("API_HASH"),   # ضع API_HASH هنا
    bot_token=os.getenv("TOKEN")      # ضع توكن البوت هنا
)

S = "/start"
TEXT = "ارسل رابط المنشور فقط من قـناة أو مـجـموعـة عـامـة المقيدة دون مقدمات 📇 .\n\n - لي شرح البوت ارسل : /help"

# دالة للتأكد من الزر
def is_set_button(data):
    return data == "set"

def is_rem_button(data):
    return data == "rem"

# التعامل مع الزر الخاص بتعيين الصورة
@gagan.on_callback_query(filters.regex("set"))
async def sett(client, callback_query):
    await callback_query.message.delete()
    # إرسال رسالة تطلب صورة
    xx = await callback_query.message.reply_text("أرسل لي أي صورة مصغرة كـ رد على هذه الرسالة 🏞✅")
    
    # انتظار الرد بالصورة
    try:
        response = await client.listen(callback_query.message.chat.id, timeout=60)
        if not response.photo:
            await xx.edit_text("لم يتم العثور على أي وسائط. 💾")
            return
        
        # تحميل الصورة
        path = await response.download()

        # إعادة تسمية الصورة
        if os.path.exists(f'{callback_query.from_user.id}.jpg'):
            os.remove(f'{callback_query.from_user.id}.jpg')
        os.rename(path, f'./{callback_query.from_user.id}.jpg')

        await xx.edit_text("تم حفظ الصورة المصغرة المؤقتة ⚡️✅")
    except Exception as e:
        await xx.edit_text("حدث خطأ أثناء العملية: " + str(e))

# التعامل مع الزر الخاص بمسح الصورة
@gagan.on_callback_query(filters.regex("rem"))
async def remt(client, callback_query):
    try:
        os.remove(f'{callback_query.from_user.id}.jpg')
        await callback_query.message.edit("تم مسح الصورة 🚫")
    except FileNotFoundError:
        await callback_query.message.edit("لم يتم حفظ الصورة المصغرة.👍🏻🚫")

# التعامل مع الأمر /start
@gagan.on_message(filters.command("start"))
async def start_command(client, message):
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
        - خـطواط استخدام البوت:
        1- اذا كانت المجموعة او القناة عامة ولكن مقيدة سيتمكن البوت من جلب المنشور بكل بساطة وسهولة مجرد ارسال رابط المنشور للبوت 🔍
        
        2- اذا كانت القناة او المجموعة خاصة، اضف البوت يدويًا للمجموعة أو القناة ثم قم بترقيته إلى أدمن وسيتمكن البوت من جلب المنشورات بسهولة ✅
        
        🆕 » تحديث الجديد: اذا كانت القناة خاصة، ارسل للبوت رابط الدعوة/الانضمام وسيتمكن البوت من سحب المحتوى بسهولة.
    """

    await message.reply_text(
        help_text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

# تشغيل البوت
gagan.run()
