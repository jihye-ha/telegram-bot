import datetime
import pandas as pd
import requests
import telegram

from bs4 import BeautifulSoup
from googletrans import Translator
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler
from telegram.ext import Filters, MessageHandler, Updater 

history_file = './info/history.pkl'


def get_single_arg(command, text):
    return text.replace(command, '').split(' ')[0]

def get_info(command, text):
    ticker, price, shares, date = text.replace(command, '').split(' ')[1:]
    state = command.replace('\\', '')
    ticker = ticker.upper()
    price = float(price)
    shares = int(shares)
    date = int(date)

    return state, ticker, price, shares, date

def reset(update, context):
    user_id = update.effective_chat.id
    history = pd.read_pickle(history_file)

    try:
        history.drop(hisotory[history.id==user_id].index, inplace=True)
        history.to_pickle(history_file)
    except Exception as e:
         context.bot.send_message(chat_id=user_id, 
                            text=f"Sorry, but failed to process your request ʕ;ᴥ;ʔ \n \
                                {e}")
    

def buy(update, context):
    user_id = update.effective_chat.id
    user_text = update.message.text

    state, ticker, price, shares, date = get_info('\buy', user_text)

    info = {"id": user_id, "state": state, "ticker": ticker,
            "price": price, "shares": shares, "date":date}
        
    try: 
        history = pd.read_pickle(history_file)
        history.append(info, ignore_index=True)
        history.to_pickle(history_file)

        context.bot.send_message(chat_id=user_id, 
                            text=f"ʕ•ᴥ•ʔ I love {info.ticker}💕!\n \
                            Now, You have {info.shares} {info.ticker} at {info.price}")
    except Exception as e:
         context.bot.send_message(chat_id=user_id, 
                            text=f"Sorry, but failed to process your request ʕ;ᴥ;ʔ \n \
                                Error Message: {e}")


def sell(update, context):
    user_id = update.effective_chat.id
    user_text = update.message.text

    state, ticker, price, shares, date = get_info('\sell', user_text)

    info = {"id": user_id, "state": state, "ticker": ticker,
            "price": price, "shares": shares, "date":date}

    try: 
        history = pd.read_pickle(history_file)
        history.append(info, ignore_index=True)
        history.to_pickle(history_file)

        context.bot.send_message(chat_id=user_id, 
                            text=f"ʕ•ᴥ•ʔ Bye Bye {info.ticker}🖐!\n \
                            Now, You sold {info.shares} {info.ticker}(s) at {info.price}")
    except Exception as e:
         context.bot.send_message(chat_id=user_id, 
                            text=f"Sorry, but failed to process your request ʕ;ᴥ;ʔ \n \
                                Error Message: {e}")


def remove(update, context):
    user_id = update.effective_chat.id
    user_text = update.message.text
    index = int(get_single_arg('\remove', user_text))

    try:
        history = pd.read_pickle(history_file)
        line = history.iloc[index].to_dict()
        history.drop(index, inplace=True)
        hisotry.to_pickle(history_file)
        context.bot.send_message(chat_id=user_id, 
                    text=f"Ok, hisotry No.{index} is removed🧹!\n \
                    {line} is gone!🖐🖐🖐")
    except Exception as e:
         context.bot.send_message(chat_id=user_id, 
                            text=f"Sorry, but failed to process your request ʕ;ᴥ;ʔ \n \
                                Error Message: {e}")

def show(update, context):
    user_id = update.effective_chat.id
    user_text = update.message.text
    ticker = get_single_arg('\show', user_text)

    try:
        history = pd.read_pickle(history_file)
        result = history.loc(history['ticker']==ticker)
        context.bot.send_photo(chat_id=user_id,
                                text=result.to_markdown())
        # context.bot.send_photo(chat_id=user_id,
        #                         photo=open('./info/result.png', 'rb'))
    except Exception as e:
         context.bot.send_message(chat_id=user_id, 
                            text=f"Sorry, but failed to process your request ʕ;ᴥ;ʔ \n \
                                Error Message: {e}")


reset_handler = CommandHandler("reset", reset)
buy_handler = CommandHandler("buy", buy)
sell_handler = CommandHandler("sell", sell)
remove_handler = CommandHandler("remove", remove)
show_handler = CommandHandler("show", show)