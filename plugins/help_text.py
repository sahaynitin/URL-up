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


@Clinton.on_message(filters.private & filters.command(["help"]))
async def help_user(bot, update):
    # logger.info(update)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
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
        text=Translation.START_TEXT.format(update.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Source code ⚡", url="https://github.com/Clinton-Abraham/UPLOADER-BOT"
                    ),
                    InlineKeyboardButton("Project Channel 👨🏻‍💻", url="https://t.me/Space_X_bots"),
                ],
                [InlineKeyboardButton("Developer 👨‍⚖️", url="https://t.me/clinton_abraham_bot")],
            ]
        ),
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
