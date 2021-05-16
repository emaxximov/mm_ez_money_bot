import json
import telebot
from telebot import types
import uuid

# данные телеграма
with open('config.json', 'r') as config_file:
    config = json.load(config_file)
token = config['api_token']
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def get_phone(message):
    bot.send_message(message.chat.id, "Здравия желаю")

@bot.message_handler(content_types=['text'])
def undef(message):
    bot.send_message(message.chat.id, "Соси, я знаю только команду /start")

bot.polling(none_stop=True)