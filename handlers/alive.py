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
BOT FAST LIKE FAST AS FUCK] [ᴄᴀᴅᴇɴ](https://t.me/Caden_OP)
ғᴏʀ ᴄʜᴇᴄᴋ ᴄᴏᴍᴍᴀɴᴅs /cmdlist
┏━━━━━━━━━━━━━━━━━┓
┣★ 𝘾𝙧𝙚𝙖𝙩𝙤𝙧 : [ɢʀᴏᴜᴘ](https://t.me/VAMPIRE_EMPIRE_OFFICIAL)
┣★ 𝙎𝙪𝙥𝙥𝙤𝙧𝙩 : [ʟᴜᴄʏ](https://t.me/LOCYS)
┗━━━━━━━━━━━━━━━━━┛

━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       " ❰ 𝘼𝙙𝙙 𝙈𝙚 𝙄𝙣 𝙂𝙧𝙤𝙪𝙥 ❱", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "legend"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/57aab166a5805db73592d.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "JOIN FOR BAKCHODI", url=f"https://t.me/VAMPIRE_EMPIRE_OFFICIAL")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["caden", "Owner"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/33a6f809c3ce77cdf51be.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
ᴄᴀᴅᴇɴ ɪs ᴍʏ ᴏᴡɴᴇʀ😎 ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ɪssᴜᴇ🙁 ᴛʜᴇɴ ᴄᴏɴᴛᴀᴄᴛ❣️🌹] [ᴄᴀᴅᴇɴ](https://t.me/Caden_OP)
━━━━━━━━━━━━━━━━━━━━━━━━**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴄᴀᴅᴇɴ's ᴡɪғᴇ❣️", url=f"https://t.me/Caden_XD")
                ]
            ]
        ),
    )
    
    

@Client.on_message(filters.command(["cmdlist", "start@Caden_music_bot"]) & filters.private & ~filters.channel)
async def cmdlist(_, message: Message):
    await message.reply_text(
        text="""**Caden Music Bot : Help Menu**
__× First Add Me To Your Group..
× Promote Me As Admin In Your Group With All Permission..__
**🏷 Common Commands.**
• `/love, fuck, play` - Song Name : __Plays Via Youtube__
• `Caden` : __About bot owner__
**🏷 Group Admin Commands.**
• `/next, next` : __Skips current music__
• `/pause, bhagbsdk` : __Pause Playing Music__
• `rukbsdk, /resume` : __Resume Playing Music__
• `/end, mc` : __Stops playing Music.__""",
        reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="🎙️ Support Group 🎙️", url="https://t.me/VAMPIRE_EMPIRE_OFFICIAL")
              ]]
          )
      )
