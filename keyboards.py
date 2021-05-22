from telebot import types
from match import scores

back_button = types.KeyboardButton(text='Главное меню') 

button_add = types.KeyboardButton(text='Добавить достижение')
button_edit = types.KeyboardButton(text='Редактировать достижения')
button_list = types.KeyboardButton(text='Список достижений')
button_total = types.KeyboardButton(text='Посчитать сумму')
button_acronyms = types.KeyboardButton(text='Расшифровка аббревиатур')
keyboard_main_menu = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
keyboard_main_menu.add(button_add,button_edit,button_list,button_total,button_acronyms)

button_type1 = types.KeyboardButton(text='Учебная деятельность')
button_type2 = types.KeyboardButton(text='Научно-исследовательская деятельность')
button_type3 = types.KeyboardButton(text='Общественная деятельность')
button_type4 = types.KeyboardButton(text='Культурно-творческая деятельность')
button_type5 = types.KeyboardButton(text='Спортивная деятельность')
keyboard_types = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
keyboard_types.add(button_type1,button_type2,button_type3,button_type4,button_type5,back_button)

button_edit_one = types.KeyboardButton(text='Удалить достижение')
button_edit_all = types.KeyboardButton(text='Удалить все')
keyboard_edit = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
keyboard_edit.add(button_edit_one,button_edit_all,back_button)

def get_keyboard(path):
    # print(path)
    names = scores
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True,one_time_keyboard=True)
    for i in path:
        names = names[i]
        if type(names) == list:
            # print('ya tut')
            return None
    for i in names:
        button = types.KeyboardButton(text=i)
        keyboard.add(button)
    keyboard.add(back_button)
    return keyboard