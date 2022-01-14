import asyncio
from time import time
from datetime import datetime
from modules.config import BOT_USERNAME
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/33a6f809c3ce77cdf51be.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
BOT FAST LIKE FAST AS ADVIK] [ADVIK](https://t.me/Luami_cifer)
ғᴏʀ ᴄʜᴇᴄᴋ ᴄᴏᴍᴍᴀɴᴅs /cmdlist
┏━━━━━━━━━━━━━━━━━┓
┣★ 𝘾𝙧𝙚𝙖𝙩𝙤𝙧 : [ɢʀᴏᴜᴘ](https://t.me/+i6XHgq8S_0k1NzQ1)
┣★ OWNER : [ADVIK](https://t.me/Luami_cifer)
┗━━━━━━━━━━━━━━━━━┛

━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       " ❰ GROUP ME ADD KAR ❱", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "ADVIK"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"hhttps://te.legra.ph/file/06531c5f534c04286f149.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "JOIN FOR MASTI", url=f"https://t.me/+i6XHgq8S_0k1NzQ1")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["ADVIK", "Owner"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4ea0334e7f95bbafbda8e.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
ADVIK ɪs ᴍʏ ᴏᴡɴᴇʀ😎 ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ɪssᴜᴇ🙁 ᴛʜᴇɴ ᴄᴏɴᴛᴀᴄᴛ❣️🌹] [ADVIK](https://t.me/Luami_cifer)
━━━━━━━━━━━━━━━━━━━━━━━━**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ADVIK's ᴡɪғᴇ❣️", url=f"https://t.me/onctxrxr")
                ]
            ]
        ),
    )
    
    

@Client.on_message(filters.command(["cmdlist", "help"]) & filters.private & ~filters.channel)
async def cmdlist(_, message: Message):
    await message.reply_text(
        text="""**ADVIK Music Bot : MADAT KENDRA 😂**
__× First Add Me To Your Group..
× Promote Me As Admin In Your Group With All Permission..__
**🏷 Common Commands.**
• `/JAAN, LOVE, play` - Song Name : __Plays Via Youtube__
• `ADVIK` : __About bot owner__
**🏷 Group Admin Commands.**
• `/next, AGLA` : __Skips current music__
• `/pause, CHUP` : __Pause Playing Music__
• `SHURUHOJA, /resume` : __Resume Playing Music__
• `/end, CHALA JA` : __Stops playing Music.__""",
        reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="🎙️ Support Group 🎙️", url="https://t.me/+i6XHgq8S_0k1NzQ1")
              ]]
          )
      )
