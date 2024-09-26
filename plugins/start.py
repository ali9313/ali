import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# تعريف البوت
gagan = Client(
    "my_bot",
    api_id=int(os.getenv("API_ID")),  # API_ID يجب أن تكون معرفه في متغيرات البيئة
    api_hash=os.getenv("API_HASH"),   # API_HASH يجب أن تكون معرفه في متغيرات البيئة
    bot_token=os.getenv("TOKEN")      # TOKEN يجب أن تكون معرفه في متغيرات البيئة
)

S = "/start"
TEXT = "أرسل رابط المنشور فقط من قناة أو مجموعة عامة المقيدة دون مقدمات 📇.\n\n - لشرح البوت ارسل: /help"

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
    # طباعة لاستكشاف الأخطاء والتحقق من وصول الرسالة
    print(f"Received /start from {message.from_user.id}")

    # إنشاء أزرار للاستخدام في الرد
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
        1- إذا كانت المجموعة أو القناة عامة ولكن مقيدة، سيتمكن البوت من جلب المنشور بكل بساطة وسهولة، فقط أرسل رابط المنشور للبوت 🔍
        
        2- إذا كانت القناة أو المجموعة خاصة، أضف البوت يدويًا للمجموعة أو القناة ثم قم بترقيته إلى أدمن وسيتمكن البوت من جلب المنشورات بسهولة ✅
        
        🆕 » التحديث الجديد: إذا كانت القناة خاصة، أرسل للبوت رابط الدعوة/الانضمام وسيتمكن البوت من سحب المحتوى بسهولة.
    """

    await message.reply_text(
        help_text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

# تشغيل البوت
gagan.run()
