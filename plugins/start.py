import os
from Config import bot as gagan
from telethon import events, Button
from telethon.tl.types import InputMediaPhoto

S = "/start"
TEXT = "ارسل رابط المنشور فقط من قـناة أو مـجـمـوعـة عـامـة المقيدة دون مقدمات 📇 .\n\n - لي شرح البوت ارسل : /help"

def is_set_button(data):
    return data == "set"

def is_rem_button(data):
    return data == "rem"

@gagan.on(events.CallbackQuery(pattern=b"set"))
async def sett(event):    
    gagan = event.client
    button = await event.get_message()
    msg = await button.get_reply_message()
    await event.delete()
    async with gagan.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("أرسل لي أي صورة مصغرة كـ رد على هذه الرسالة 🏞✅")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("لم يتم العثور على أي وسائط. 💾")
            return
        mime = x.file.mime_type
        if 'png' not in mime and 'jpg' not in mime and 'jpeg' not in mime:
            return await xx.edit("لم يتم العثور على صورة.😢")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'Trying.')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("تم حفظ الصورة المصغرة المؤقتة ⚡️✅")

@gagan.on(events.CallbackQuery(pattern=b"rem"))
async def remt(event):  
    gagan = event.client            
    await event.edit('أنـتـظـر مـن فـضـلك ⌛️👍🏻')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('تــم مـسـح الـصـورة 🚫')
    except Exception:
        await event.edit("لم يتم حفظ الصورة المصغرة.👍🏻🚫 /start")                        

@gagan.on(events.NewMessage(pattern=f"^{S}"))
async def start_command(event):
    # Creating inline keyboard with buttons
    buttons = [
        [Button.url("R A D", url="t.me/r_afx")]

         
    ]

    # Sending photo with caption and buttons
    await gagan.send_message(
        entity=event.chat.id, message=TEXT,
        buttons=buttons

    )

@gagan.on(events.NewMessage(pattern=f"^/help"))
async def start_command(event):
    # Creating inline keyboard with buttons
    buttons = [
        [Button.url("R A D", url="t.me/r_afx")]
    ]

    message = """
        -  خـطواط استخدام البوت 
        1- اذا كانت المجموعة او القناة عامة ولكن مقيدة سيتمكن البوت من جلب المنشور بكل بساطه وسهولة مجرد ارسال رابط المنشور للبوت 🔍

        2- اذا كانت القناة او المجموعه خاصه اضف البوت يدوي للمجموعه او القناة او ارسل رابط الانضمام ثم قم بترقيته الي ادمن وسيتمكن البوت بجلب المنشورات بكل سهوله ✅

        🆕 »  تحديث الجديد اذا كانت القناة خاصة ارسل للبوت رابط الدعوة/الانضمام وسيتمكن البوت من سحب المحتوي بسهولة 


    """

    # Sending photo with caption and buttons
    await gagan.send_message(
        entity=event.chat.id, message='rr',
        buttons=message

    )
