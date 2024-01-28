from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

register_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Зарегистрировать аккаунт"
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Для продолжения нажмите на кнопку ниже")


# resize_keyboard = True - изменение размера кнопки/клавиатуры под доступный размер (если кнопка одна, то она занимает все пространство) 
# one_time_keyboard = True - кнопа исчезает после нажатия
# input_field_placeholder = "Some text" - placeholder(html) подсказка в поле ввода