from pyrogram import filters
from pyrogram.types import Message

from MusicBot.services.callsmusic.callsmusic import client as USER


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    await USER.send_message(
        message.chat.id,
        "**Hi there, This is a music assistant service @MT_Music_BoT {Private Bot}.**",
    )
    return
