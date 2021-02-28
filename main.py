#!/usr/bin/env python3
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import locale
import sys
import json
import logging
import arzyab
import cryptoyab


#TODO: Tokenizer 
with open('cred.json') as file:
    config = json.load(file)
    token = config["telegram_token"]


updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=arzyab.rate_graber())
def eur(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=arzyab.rate_graber("sana_buy_eur"))
def usd(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=arzyab.rate_graber("sana_buy_usd"))
def gbp(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=arzyab.rate_graber("sana_buy_gbp"))
def bitcoin_eur(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=cryptoyab.euro_based_price('bitcoin', 'eur'))
def ethereum_eur(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=cryptoyab.euro_based_price('ethereum', 'eur'))
def dogecoin_eur(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=cryptoyab.euro_based_price('dogecoin', 'eur'))
def cardano_eur(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=cryptoyab.euro_based_price('cardano', 'eur'))
def iota_eur(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=cryptoyab.euro_based_price('iota', 'eur'))

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
start_eur = CommandHandler('eur', eur)
dispatcher.add_handler(start_eur)
start_usd = CommandHandler('usd', usd)
dispatcher.add_handler(start_usd)
start_gbp = CommandHandler('gbp', gbp)
dispatcher.add_handler(start_gbp)
start_bitcoin_eur = CommandHandler('bitcoin_eur', bitcoin_eur)
dispatcher.add_handler(start_bitcoin_eur)
start_ethereum_eur = CommandHandler('ethereum_eur', ethereum_eur)
dispatcher.add_handler(start_ethereum_eur)
start_dogecoin_eur = CommandHandler('dogecoin_eur', dogecoin_eur)
dispatcher.add_handler(start_dogecoin_eur)
start_cardano_eur = CommandHandler('cardano_eur', cardano_eur)
dispatcher.add_handler(start_cardano_eur)
start_iota_eur = CommandHandler('iota_eur', iota_eur)
dispatcher.add_handler(start_iota_eur)

def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

updater.start_polling()
updater.idle()
