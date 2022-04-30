from pyrogram import Client, filters
import asyncio
import os
from pytube import YouTube
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from youtubesearchpython import VideosSearch
from song.utils import ignore_blacklisted_users, get_arg
from song import app, LOGGER
from song.sql.chat_sql import add_chat_to_db

# from __future__ import unicode_literals

import aiohttp
import requests
import logging
logger = logging.getLogger(__name__)
import os, re, time, math, yt_dlp, json, string, random, traceback, wget, asyncio, datetime, aiofiles, aiofiles.os, requests, youtube_dl, lyricsgenius, wget
from random import choice 
from pyrogram import Client, filters
from youtube_search import YoutubeSearch
from youtubesearchpython import VideosSearch
from yt_dlp import YoutubeDL
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent
# from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid, MessageNotModified
# from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid

def yt_search(song):
    videosSearch = VideosSearch(song, limit=1)
    result = videosSearch.result()
    if not result:
        return False
    else:
        video_id = result["result"][0]["id"]
        url = f"https://youtu.be/{video_id}"
        return url


@app.on_message(filters.command("song"))
def song(bot, message): #client, message,
    query = " ".join(message.command[1:])
    m = message.reply("🔍 **Mahnı axtarılır...**")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:100]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]
        
    except Exception as e:
        m.edit("❗ **Zəhmət olmasa mahnı adını düzgün yazın!**\n\n__Bu xətanı aldınızsa botda prablem olub olmadığına əmin olmaq üçün başqa mahnı adı yazıb yükləyərək yoxlayın. Bəzi hallarda youtubedə olan mahnıları telegram yükləyə bilmir__")
        print(str(e))
        return
    m.edit("🔍 **Mahnı yüklənir...**")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"🎵 `{title}`"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit(f"🎵 **Mahnı Adı:** `{title}`") 
        mess = message.reply_audio(
            audio_file,
            caption=rep,
            thumb=thumb_name,
            performer="@Songazbot",
            parse_mode='md',
            title=title,
            duration=dur
        )
        bot.copy_message(
            -1001512529266,
            message.chat.id,
            mess.message_id
        )
        m.delete()
    except Exception as e:
        m.edit("😊 Bizi seçdiyiniz üçün təşəkkürlər\n Hər hansı Prablem olarsa @Samil - ə bildirin")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
