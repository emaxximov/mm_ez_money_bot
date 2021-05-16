from telebot import types

button_add = types.KeyboardButton(text='Добавить достижение')
button_edit = types.KeyboardButton(text='Редактировать достижения')
button_total = types.KeyboardButton(text='Посчитать сумму')
keyboard_main_menu = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
keyboard_main_menu.add(button_add,button_edit,button_total)

button_type1 = types.KeyboardButton(text='Учебная деятельность')
button_type2 = types.KeyboardButton(text='Научно-исследовательская деятельность')
button_type3 = types.KeyboardButton(text='Общественная деятельность')
button_type4 = types.KeyboardButton(text='Культурно-творческая деятельность')
button_type5 = types.KeyboardButton(text='Спортивная деятельность')
keyboard_types = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
keyboard_types.add(button_type1,button_type2,button_type3,button_type4,button_type5)

button_7a = types.KeyboardButton(text='Только "отлично"')
button_7b = types.KeyboardButton(text='Приз за проектную деятельность')
button_7c = types.KeyboardButton(text='Олимпиада')
keyboard_7 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
keyboard_7.add(button_7a,button_7b,button_7c)
