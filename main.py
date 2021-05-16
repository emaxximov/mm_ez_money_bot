import json
import telebot
from telebot import types
import uuid
import pas
import match
import keyboards

# данные телеграма
with open('config.json', 'r') as config_file:
    config = json.load(config_file)
token = config['api_token']
bot = telebot.TeleBot(token)

db = pas.db_obj()

@bot.message_handler(commands=['start'])
def hello(message):
    if db[message.chat.id] == None:
        p = pas.pas(message.chat.id)
        db.append(p)
    bot.send_message(message.chat.id, 'Здравия желаю.\nБот для подсчета баллов для ПАС')
    bot.send_message(message.chat.id, 'Пора делать выбор', reply_markup=keyboards.keyboard_main_menu)

@bot.message_handler(content_types=['text'])
def ans(message):
    p = db[message.chat.id]
    if message.text == 'Посчитать сумму':
        total = p.total()
        bot.send_message(message.chat.id, 'Сумма баллов: {}'.format(total))
        bot.send_message(message.chat.id, 'Пора делать выбор', reply_markup=keyboards.keyboard_main_menu)
    elif message.text == 'Добавить достижение':
        msg = bot.send_message(message.chat.id, 'Тип достижения', reply_markup=keyboards.keyboard_types)
        bot.register_next_step_handler(msg, type_achievement)
    elif message.text == 'Редактировать достижения':
        bot.send_message(message.chat.id, 'Пора делать выбор', reply_markup=keyboards.keyboard_main_menu)

def type_achievement(message):
    if message.text == 'Учебная деятельность':
        msg = bot.send_message(message.chat.id, 'Критерий', reply_markup=keyboards.keyboard_7)
        bot.register_next_step_handler(msg, type_achievement_local)

def type_achievement_local(message):
    if message.text == 'Только "отлично"':
        msg = bot.send_message(message.chat.id, 'Имя достижения')
        bot.register_next_step_handler(msg, lambda l: add_achievements(l, 8))
    # elif message.type == 'Олимпиада':
    #     msg = bot.send_message(message.chat.id, 'Пора делать выбор', reply_markup=keyboards.keyboard_7)
        # bot.register_next_step_handler(msg, type_achievement_local)

def add_achievements(message,score):
    p = db[message.chat.id]
    p.add(message.text,score)
    db[message.chat.id] = p
    bot.send_message(message.chat.id, 'Добавлено')
    bot.send_message(message.chat.id, 'Пора делать выбор', reply_markup=keyboards.keyboard_main_menu)

if __name__ == '__main__':
    bot.polling(none_stop=True)