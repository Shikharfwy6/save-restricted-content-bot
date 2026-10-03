from pyrogram import Client, filters
from database.db import db

@Client.on_message(filters.command("testdump") & filters.private)
async def testdump(client, message):
    target = await db.get_dump_chat(message.from_user.id)
    if not target:
        return await message.reply("dump_chat set nahi hai")
    try:
        await client.send_message(target, "test")
        await message.reply(f"OK, bheja gaya: {target}")
    except Exception as e:
        await message.reply(f"Error: {e}")
        @Client.on_message(filters.channel)
async def channel_seen(client, message):
    for a in ADMINS:
        try:
            await client.send_message(
                a, f"Channel dikha: {message.chat.title}\nID: {message.chat.id}"
            )
        except Exception:
            pass
