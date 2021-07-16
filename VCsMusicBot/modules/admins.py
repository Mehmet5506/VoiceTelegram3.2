from asyncio import QueueEmpty
from pyrogram import Client 
from pyrogram import filters
from pyrogram.types import Message

from VCsMusicBot.config import que
from VCsMusicBot.function.admins import set
from VCsMusicBot.helpers.channelmusic import get_chat_id
from VCsMusicBot.helpers.decorators import authorized_users_only
from VCsMusicBot.helpers.decorators import errors
from VCsMusicBot.helpers.filters import command
from VCsMusicBot.helpers.filters import other_filters
from VCsMusicBot.services.callsmusic import callsmusic
from VCsMusicBot.services.queues import queues


@Client.on_message(filters.command("adminreset"))
async def update_admin(client, message: Message):
    chat_id = get_chat_id(message.chat)
    set(
        chat_id,
        [
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ],
    )
    await message.reply_text("❇️ Yönetici önbelleği yenilendi!")


@Client.on_message(command("pause") & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if (chat_id not in callsmusic.active_chats) or (
        callsmusic.active_chats[chat_id] == "paused"
    ):
        await message.reply_text("❗ Hiçbir şey oynamıyor.!")
    else:
        callsmusic.pause(chat_id)
        await message.reply_text("▶️ Duraklatıldı!")


@Client.on_message(command("rasume") & other_filters)
@errors
@authorized_users_only
async def rasume(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if (chat_id not in callsmusic.active_chats) or (
        callsmusic.active_chats[chat_id] == "playing"
    ):
        await message.reply_text("❗ Hiçbir şey duraklatılı değil!")
    else:
        callsmusic.resume(chat_id)
        await message.reply_text("⏸ Devam!")


@Client.on_message(command("end") & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.active_chats:
        await message.reply_text("❗ Hiçbir şey çalışmıyor!")
    else:
        try:
            queues.clear(chat_id)
        except QueueEmpty:
            pass

        await callsmusic.stop(chat_id)
        await message.reply_text("❌ Hey müzik kapatıldı!")


@Client.on_message(command("skip") & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.active_chats:
        await message.reply_text("❗ Parçanın geçilmesi için birşey yok!")
    else:
        queues.task_done(chat_id)
        if queues.is_empty(chat_id):
            await callsmusic.stop(chat_id)
        else:
            await callsmusic.set_stream(
                chat_id, 
                queues.get(chat_id)["file"]
            )

    qeue = que.get(chat_id)
    if qeue:
        skip = qeue.pop(0)
    if not qeue:
        return
    await message.reply_text(f"- Atlanır **{skip[0]}**\n- Şimdi Yürütülen **{qeue[0][0]}**")


@Client.on_message(filters.command("reload"))
@errors
async def admincache(client, message: Message):
    set(
        message.chat.id,
        [
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ],
    )
    await message.reply_text("❇️ Yönetici önbelleği yenilendi!")
