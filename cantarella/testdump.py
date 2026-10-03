from pyrogram import Client, filters
from config import ADMINS
from database.db import db


def _admin_list():
    if isinstance(ADMINS, (list, tuple, set)):
        return list(ADMINS)
    return [ADMINS]


# /testdump - dump chat par test message bhejta hai aur error dikhata hai
@Client.on_message(filters.command("testdump") & filters.private)
async def testdump(client: Client, message):
    target = await db.get_dump_chat(message.from_user.id)
    if not target:
        return await message.reply("dump_chat set nahi hai. Pehle /setchat <chat_id> karo.")
    try:
        await client.send_message(target, "test")
        await message.reply(f"OK, bheja gaya: {target}")
    except Exception as e:
        await message.reply(f"Error: {e}")


# Channel mein koi bhi post aaye to admins ko channel ka naam aur exact ID DM karta hai
@Client.on_message(filters.channel)
async def channel_seen(client: Client, message):
    for admin in _admin_list():
        try:
            await client.send_message(
                int(admin),
                f"Channel dikha: {message.chat.title}\nID: {message.chat.id}"
            )
        except Exception:
            pass
            
