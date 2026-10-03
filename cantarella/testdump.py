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
