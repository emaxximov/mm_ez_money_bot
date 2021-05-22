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
        bot.register_next_step_handler(msg, lambda l: process_add_achievement(l, []))
    elif message.text == 'Редактировать достижения':
        msg = bot.send_message(message.chat.id, 'Выбор', reply_markup=keyboards.keyboard_edit)
        bot.register_next_step_handler(msg, process_edit_achievement_request)
    elif message.text == 'Расшифровка аббревиатур':
        s = ''
        for i in match.acronyms:
            s += '{} {}\n'.format(i,match.acronyms[i])
        bot.send_message(message.chat.id, s)
        bot.send_message(message.chat.id, 'Пора делать выбор', reply_markup=keyboards.keyboard_main_menu)
    elif message.text == 'Список достижений':
        s = p.get_list()
        if s != '':
            bot.send_message(message.chat.id, s)
        else:
            bot.send_message(message.chat.id, 'Пусто')
        bot.send_message(message.chat.id, 'Пора делать выбор', reply_markup=keyboards.keyboard_main_menu)
    else:
        bot.send_message(message.chat.id, 'Не шарю')
        bot.send_message(message.chat.id, 'Пора делать выбор', reply_markup=keyboards.keyboard_main_menu)

def process_add_achievement(message,path):
    if message.text == 'Главное меню':
        bot.send_message(message.chat.id, 'Пора делать выбор', reply_markup=keyboards.keyboard_main_menu)
        return 0
    path.append(message.text)
    try:
        keyboard = keyboards.get_keyboard(path)
        if keyboard != None:
            keyboard.add(keyboards.back_button)
            msg = bot.send_message(message.chat.id, 'Выбор', reply_markup=keyboards.get_keyboard(path))
            bot.register_next_step_handler(msg, lambda l: process_add_achievement(l, path))
        else:
            msg = bot.send_message(message.chat.id, 'Имя достижения')
            bot.register_next_step_handler(message, lambda l: add_achievement(l, path))
    except:
        bot.send_message(message.chat.id, 'Не шарю')
        bot.send_message(message.chat.id, 'Пора делать выбор', reply_markup=keyboards.keyboard_main_menu)

def add_achievement(message,path):
    p = db[message.chat.id]
    resp = p.add(message.text,path)
    if resp:
        db[message.chat.id] = p
        bot.send_message(message.chat.id, 'Добавлено')
        bot.send_message(message.chat.id, 'Пора делать выбор', reply_markup=keyboards.keyboard_main_menu)
    else:
        msg = bot.send_message(message.chat.id, 'Имя занято, введите уникальное имя')
        bot.register_next_step_handler(msg, lambda l: add_achievement(l, path))

def process_edit_achievement_request(message):
    if message.text == 'Главное меню':
        bot.send_message(message.chat.id, 'Пора делать выбор', reply_markup=keyboards.keyboard_main_menu)
        return 0
    if message.text == 'Удалить все':
        edit_all_achievements(message)
    elif message.text == 'Удалить достижение':
        p = db[message.chat.id]
        s = p.get_list()
        if s != '':
            msg = bot.send_message(message.chat.id, s)
            bot.register_next_step_handler(msg, edit_one_achievement)
        else:
            bot.send_message(message.chat.id, 'Пусто')
            bot.send_message(message.chat.id, 'Пора делать выбор', reply_markup=keyboards.keyboard_main_menu)
    else:
        bot.send_message(message.chat.id, 'Не шарю')
        bot.send_message(message.chat.id, 'Пора делать выбор', reply_markup=keyboards.keyboard_main_menu)

def edit_one_achievement(message):
    name = message.text
    p = db[message.chat.id]
    resp = p.delete(name)
    if resp:
        db[message.chat.id] = p
        bot.send_message(message.chat.id, 'Удалено')
        bot.send_message(message.chat.id, 'Пора делать выбор', reply_markup=keyboards.keyboard_main_menu)
    else:
        bot.send_message(message.chat.id, 'Некорректное имя, введите корректное')
        msg = bot.send_message(message.chat.id, p.get_list())
        bot.register_next_step_handler(msg, edit_one_achievement)

def edit_all_achievements(message):
    p = db[message.chat.id]
    p.delete_all()
    db[message.chat.id] = p
    bot.send_message(message.chat.id, 'Все достижения удалены')
    bot.send_message(message.chat.id, 'Пора делать выбор', reply_markup=keyboards.keyboard_main_menu)

if __name__ == '__main__':
    bot.polling(none_stop=True)