import datetime
import json
import pandas as pd
import requests
import telegram

from bs4 import BeautifulSoup
from googletrans import Translator
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler
from telegram.ext import Filters, MessageHandler, Updater 

translator = Translator()

with open('./info/user.json') as f:
    info = json.load(f)

def start(update: Update, context: CallbackContext):
    user_id = update.effective_chat.id
    context.bot.send_message(chat_id=user_id, text="Welcome to HaZBot ʕ•ᴥ•ʔ💕.\n")

def trans(update, context):
    user_id = update.effective_chat.id
    user_text = update.message.text
    text = translator.translate(user_text, dest="en")
    context.bot.send_message(chat_id=user_id, text=f" ʕ•ᴥ•ʔ💕\n{text.text}")

def echo(update, context):
    user_id = update.effective_chat.id
    user_text = update.message.text
    context.bot.send_message(chat_id=user_id, text=f" ʕ•ᴥ•ʔ💕\n{user_text}")

def unknown(update, context):
    user_id = update.effective_chat.id
    context.bot.send_message(chat_id=user_id, text="Sorry ʕ•ᴥ•ʔ?")


start_handler = CommandHandler("start", start)
trans_handler = MessageHandler(Filters.text & (~Filters.command), trans)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)