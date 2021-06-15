from pyrogram import filters
from pyrogram.types import Message
from MusicBot.config import MT_PM_MESSAGE_TEXT
from MusicBot.services.callsmusic.callsmusic import client as USER


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    await USER.send_message(
        message.chat.id,
        "MT_PM_MESSAGE_TEXT",
    )
    return
