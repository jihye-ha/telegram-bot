from telegram.ext import Updater 

from basic import start_handler, trans_handler, echo_handler
from stocks import buy_handler, sell_handler, reset_handler, remove_handler, show_handler


if __name__ == '__main__':
    with open("./info/API_TOKEN", 'r') as f:
        API_TOKEN = f.readline()

    updater = Updater(API_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(trans_handler)
    dispatcher.add_handler(buy_handler)
    dispatcher.add_handler(sell_handler)
    dispatcher.add_handler(remove_handler)
    dispatcher.add_handler(show_handler)

    updater.start_polling()
    updater.idle()
