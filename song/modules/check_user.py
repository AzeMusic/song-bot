import datetime

import config
import logging

from song.modules.database import Database

from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton

DB_URL = config.DB_URL
DB_NAME = config.DB_NAME
LOG_CHANNEL = config.LOG_CHANNEL

db = Database(DB_URL, DB_NAME)

async def handle_user_status(bot, cmd):
    chat_id = cmd.from_user.id
    if not await db.is_user_exist(chat_id):
        data = await bot.get_me()
        BOT_USERNAME = data.username
        await db.add_user(chat_id)
        if LOG_CHANNEL:
            await bot.send_message(
                LOG_CHANNEL,
                f"Yeni istifadəçi [{cmd.from_user.first_name}](tg://user?id={cmd.from_user.id}) botu @{BOT_USERNAME} başlatdı",
            )
        else:
            logging.info(f"#YeniUser :- Ad : {cmd.from_user.first_name} ID : {cmd.from_user.id}")

    ban_status = await db.get_ban_status(chat_id)
    if ban_status["is_banned"]:
        if (
            datetime.date.today() - datetime.date.fromisoformat(ban_status["banned_on"])
        ).days > ban_status["ban_duration"]:
            await db.remove_ban(chat_id)
        else:
            await cmd.reply_text(f"""⛔ Siz Banlandınız! [{cmd.from_user.first_name}](tg://user?id={message.from_user.id})
Bu botu istifadə etməyinizə icazə yoxdur! """, quote=False
        )
            return
    await cmd.continue_propagation()
