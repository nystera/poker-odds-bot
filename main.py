import requests
import re
import telebot

from keyboard import gen_card_num_markup
from dotenv import load_dotenv


import os
load_dotenv()
API_KEY = os.getenv("API_KEY")

bot = telebot.TeleBot(API_KEY, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id, "Welcome! Type /new to start calcuating odds for a game")


@bot.message_handler(commands=['new'])
def setup_cards(message):
    bot.send_message(message.chat.id, "Add your hands:",
                     reply_markup=gen_card_num_markup())


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    print(call)
    try:
        bot.send_message(call.from_user.id, str(call.data))
    except:
        bot.send_message(call.from_user.id, 'something went wrong')


bot.polling()
