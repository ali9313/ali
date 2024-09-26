import asyncio
import time
import os
import logging
from telethon import events
from telethon.sync import TelegramClient
from telethon.errors import ChannelBanned, ChannelInvalid, ChannelPrivate, ChatIdInvalid, ChatInvalid
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument, MessageMediaVideo
from Config import Bot, bot
from plugins.progress import progress_for_telethon
from plugins.helpers import screenshot, video_metadata

logging.basicConfig(level=logging.debug,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("telethon").setLevel(logging.INFO)

user_chat_ids = {}

def thumbnail(sender):
    return f'{sender}.jpg' if os.path.exists(f'{sender}.jpg') else f'thumb.jpg'

async def copy_message_with_chat_id(client, sender, chat_id, message_id):
    target_chat_id = user_chat_ids.get(sender, sender)
    try:
        await client.send_message(target_chat_id, await client.get_message(chat_id, message_id))
    except Exception as e:
        error_message = f"Error occurred while sending message to chat ID {target_chat_id}: {str(e)}"
        await client.send_message(sender, error_message)
        await client.send_message(sender, f"Make Bot admin in your Channel - {target_chat_id} and restart the process after /cancel")

async def send_message_with_chat_id(client, sender, message):
    chat_id = user_chat_ids.get(sender, sender)
    try:
        await client.send_message(chat_id, message)
    except Exception as e:
        error_message = f"Error occurred while sending message to chat ID {chat_id}: {str(e)}"
        await client.send_message(sender, error_message)
        await client.send_message(sender, f"Make Bot admin in your Channel - {chat_id} and restart the process after /cancel")

@bot.on(events.NewMessage(incoming=True, pattern='/setchat'))
async def set_chat_id(event):
    try:
        chat_id = int(event.raw_text.split(" ", 1)[1])
        user_chat_ids[event.sender_id] = chat_id
        await event.reply("Chat ID set successfully!")
    except ValueError:
        await event.reply("Invalid chat ID!")

async def send_video_with_chat_id(client, sender, path, caption, duration, hi, wi, thumb_path, upm):
    chat_id = user_chat_ids.get(sender, sender)
    try:
        await client.send_file(
            chat_id=chat_id,
            file=path,
            caption=caption,
            thumb=thumb_path
        )
    except Exception as e:
        error_message = f"Error occurred while sending video to chat ID {chat_id}: {str(e)}"
        await client.send_message(sender, error_message)
        await client.send_message(sender, f"Make Bot admin in your Channel - {chat_id} and restart the process after /cancel")

async def send_document_with_chat_id(client, sender, path, caption, thumb_path, upm):
    chat_id = user_chat_ids.get(sender, sender)
    try:
        await client.send_file(
            chat_id=chat_id,
            file=path,
            caption=caption,
            thumb=thumb_path
        )
    except Exception as e:
        error_message = f"Error occurred while sending document to chat ID {chat_id}: {str(e)}"
        await client.send_message(sender, error_message)
        await client.send_message(sender, f"Make Bot admin in your Channel - {chat_id} and restart the process after /cancel")

async def check(userbot, client, link):
    logging.info(link)
    msg_id = 0
    try:
        msg_id = int(link.split("/")[-1])
    except ValueError:
        if '?single' not in link:
            return False, "**رابط غير صالح أعـد مـحاولة من فضـلك ❌**"
        link_ = link.split("?single")[0]
        msg_id = int(link_.split("/")[-1])
    
    if 't.me/c/' in link:
        try:
            chat = int('-100' + str(link.split("/")[-2]))
            await userbot.get_message(chat, msg_id)
            return True, None
        except ValueError:
            return False, "**رابط غير صالح أعـد مـحاولة من فضـلك ❌**"
        except Exception as e:
            logging.info(e)
            return False, "هل انضممت إلى القناة ⁉️"
    else:
        try:
            chat = str(link.split("/")[-2])
            await client.get_message(chat, msg_id)
            return True, None
        except Exception as e:
            logging.info(e)
            return False, "ربما تم حظر البوت من المجموعة/قناة  أو أن الرابط الخاص بك غير صالح ⚠️"

async def get_msg(userbot, client, sender, edit_id, msg_link, i, file_n):
    edit = ""
    chat = ""
    msg_id = int(i)
    if msg_id == -1:
        await client.edit_message(sender, edit_id, "**رابط غير صالح أعـد مـحاولة من فضـلك ❌**")
        return None
    if 't.me/c/' in msg_link or 't.me/b/' in msg_link:
        if "t.me/b" not in msg_link:    
            chat = int('-100' + str(msg_link.split("/")[-2]))
        else:
            chat = int(msg_link.split("/")[-2])
        try:
            msg = await userbot.get_message(chat_id=chat, message_id=msg_id)
            logging.info(msg)

            if msg.media and isinstance(msg.media, MessageMediaDocument):
                await send_document_with_chat_id(client, sender, msg.file, msg.message, thumbnail(sender), None)
            elif msg.media and isinstance(msg.media, MessageMediaVideo):
                await send_video_with_chat_id(client, sender, msg.file, msg.message, None, None, None, thumbnail(sender), None)

            elif msg.media and isinstance(msg.media, MessageMediaPhoto):
                await send_message_with_chat_id(client, sender, "جـار الـسـحـب...🔍")
                await client.send_file(sender, msg.file, caption=msg.message)

            else:
                await client.edit_message(sender, edit_id, "لا يمكن حفظ وسائط الاستطلاع. ❌")
            return None

        except (ChannelBanned, ChannelInvalid, ChannelPrivate, ChatIdInvalid, ChatInvalid):
            await client.edit_message(sender, edit_id, "عـزيـزي هـذا الـقـناة خـاصـة لـبـدأ سـحـب الـمحتـوي ارسـل رابـط الـدعـوة/الانـضـمـام ✅")
            return None
    else:
        edit = await client.edit_message(sender, edit_id, "جــار سـحـب المـنـشـور ....🆙")
        chat = msg_link.split("/")[-2]
        await copy_message_with_chat_id(client, sender, chat, msg_id)
        await edit.delete()
        return None   

async def get_bulk_msg(userbot, client, sender, msg_link, i):
    x = await client.send_message(sender, "جــار الـمـعـالـجـة... 🔀")
    file_name = ''
    await get_msg(userbot, client, sender, x.id, msg_link, i, file_name)
