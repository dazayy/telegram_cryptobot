from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

crypto_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Посмотреть список криптовалют"
        ),
         KeyboardButton(
            text="Посмотреть цену криптовалюты"
        )
    ],
],  resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Нажмите, чтобы прекратить добавление криптовалют")
