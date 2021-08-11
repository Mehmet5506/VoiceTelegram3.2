import logging
from VCsMusicBot.modules.msg import Messages as tr
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from VCsMusicBot.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL,BOT_USERNAME
logging.basicConfig(level=logging.INFO)

@Client.on_message(filters.private & filters.incoming & filters.command(['start']))
def _start(client, message):
    client.send_message(message.chat.id,
        text=tr.START_MSG.format(message.from_user.first_name, message.from_user.id),
        parse_mode="markdown",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Beni Grubunuza Ekleyin ➕", url=f"https://t.me/Airmusic_Bot?startgroup=true")],
                [
                    InlineKeyboardButton(
                        "👥 Group", url=f"https://t.me/sohbety"), 
                    InlineKeyboardButton(
                        "Owner 📢", url=f"https://t.me/byboss"), 
                ],[
                    InlineKeyboardButton(
                        "🔥 Proje Kanalı🔥", url=f"https://t.me/DjByboss"), 
                ]
            ]
        ),
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.command(["start","startAirmusic_Bot"]) & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        f"""**Müzik botu çevrimiçi.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 Support Chat", url=f"https://t.me/sohbety"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "🔎 YT Ara ", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "Kapat ❌", callback_data="close"
                    )
                ]
            ]
        ),
    )


@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    disable_web_page_preview=True
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = '▶️ Next', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        url = f"https://t.me/Djbyboss"
        button = [
            [InlineKeyboardButton("➕ Add me to your Group ➕", url=f"https://t.me/Airmusic_Bot?startgroup=true")],
            [InlineKeyboardButton(text = '👥 Group', url=f"https://t.me/Djbyboss"),
             InlineKeyboardButton(text = 'Channel 📢', url=f"https://t.me/sohnety")],
            [InlineKeyboardButton(text = '🔥 Source Code 🔥', url=f"https://{SOURCE_CODE}")],
            [InlineKeyboardButton(text = '◀️ Back', callback_data = f"help+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '◀️ Back', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = 'Next ▶️', callback_data = f"help+{pos+1}")
            ],
        ]
    return button

@Client.on_message(filters.command(["help","helpAirmusic_Bot"]) & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        f"""**Merhaba efendim. !ben @byboss için yapılmış müzik botu! Telgraf gruplarının ve kanallarının sesli sohbetlerinde müzik çalabilirim.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Yardım için tıklayınız", url=f"https://t.me/sohbety?start"
                    )
                ]
            ]
        ),
    )

