# DevilHacker

import os
import aiohttp
import asyncio
import json
import sys
import time
from youtubesearchpython import SearchVideos
from pyrogram import filters, Client
from yt_dlp import YoutubeDL
from yt_dlp.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)


@Client.on_message(filters.command("song") & ~filters.edited)
async def song(client, message):
    cap = "**JA RAHA KHOJNE ](https://t.me/+HBlyprUka24zMjk1) ...**"
    url = message.text.split(None, 1)[1]
    rkp = await message.reply("**MIL GAYA**")
    if not url:
        await rkp.edit("**PLZ FIND ANOTHER SONG IN KHOPCHA ...**")
    search = SearchVideos(url, offset=1, mode="json", max_results=1)
    test = search.result()
    p = json.loads(test)
    q = p.get("search_result")
    try:
        url = q[0]["link"]
    except BaseException:
        return await rkp.edit("**KYA GUNDA BANEGA RE TU SONG NAHI MILA  ...**")
    type = "audio"
    if type == "audio":
        opts = {
            "format": "bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "writethumbnail": True,
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",
                }
            ],
            "outtmpl": "%(id)s.mp3",
            "quiet": True,
            "logtostderr": False,
        }
        song = True
    try:
        await rkp.edit("**READY HAI ...**`")
        with YoutubeDL(opts) as rip:
            rip_data = rip.extract_info(url)
    except DownloadError as DE:
        await rkp.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await rkp.edit("`THODI TO BADI FILE DWONALOAD KAR.`")
        return
    except GeoRestrictedError:
        await rkp.edit(
            "`ARE YE VIDEO IDHAR ALLOWED NAHI HAI`"
        )
        return
    except MaxDownloadsReached:
        await rkp.edit("`LIMIT REACH HO GAYI`")
        return
    except PostProcessingError:
        await rkp.edit("`HR CHEEJ KI EK SEEMA HOTI HAI`")
        return
    except UnavailableVideoError:
        await rkp.edit("`Media is not available in the requested format.`")
        return
    except XAttrMetadataError as XAME:
        await rkp.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return
    except ExtractorError:
        await rkp.edit("`There was an error during info extraction.`")
        return
    except Exception as e:
        await rkp.edit(f"{str(type(e)): {str(e)}}")
        return
    time.time()
    if song:
        await rkp.edit("**📤LOADING SONG FROM ADVIK-ADVIKA...**"),
        lol = "./etc/tg_vc_bot.jpg"
        lel = await message.reply_audio(
                 f"{rip_data['id']}.mp3",
                 duration=int(rip_data["duration"]),
                 title=str(rip_data["title"]),
                 performer=str(rip_data["uploader"]),
                 thumb=lol,
                 caption=cap)
        await rkp.delete()
