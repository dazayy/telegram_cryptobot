from contextlib import suppress
from states.crypto import CryptoState
from states.register import RegisterState
from aiogram.fsm.context import FSMContext
from utils.db.storage import DatabaseManager  
from utils.api.fetch_data_api import  get_data
from aiogram.types import Message, CallbackQuery
from aiogram.exceptions import TelegramBadRequest
from utils.api.fetch_data_api import get_crypto_symbols 
from keyboards.default.pagination_kb import Pagination, paginator

db = DatabaseManager("data/database.db")
all_crypts = db.fetchall("SELECT * FROM cryptocurrencies")



async def start_register(message: Message, state: FSMContext):

    """
    set_state используется по цепеочке (на 1 шаг назад, от нужного действия)

    сначала выполняется действие, которое предшевствует нужному
    Например:

        - Приветствие от бота
        - Выбор функции регистрации:
        -> В этот момент устанавливается ожидание состояния, которое нужно получить от пользователя
        - Ввод имя пользователя
            -> Обновление данных, которые были получены от пользователя с помощью метода:
                update_data 


    .....Действия.....Зарегистрироваться + установка состояния ожидания....Ввод от пользователя -> обновление данных....

    """


    db = DatabaseManager("data/database.db")
    users = db.select_user_id(message.from_user.id)


    if users:
        await message.answer(f'{users[-1]}\nВы уже зарегестрированы')
    else:
        await message.answer(f"Давайте начем регистрацию\nУкажите свое имя/псевдоним:")
        await state.set_state(RegisterState.regname) # установка ожидания для получения состояния 


async def register_name(message: Message, state: FSMContext):
    user_name = message.text.capitalize()
    await state.update_data(regname=user_name) # обновление данных на полученные от пользователя


    reg_data = await state.get_data() # получение всех данных из состояния 
    reg_name = reg_data.get("regname") # выборка имени пользователя
    
    msg = f"Приятно познакомиться {reg_name}"
    await message.answer(msg)

    db = DatabaseManager("data/database.db") 
    db.add_user(reg_name, message.from_user.id)    
    """
       Положение закрытия состояния важно, если закрыть его раньше, то не выйдет получить данныне:
            reg_data = await state.get_data() # получение всех данных  
            reg_name = reg_data.get("regname") # выборка имени пользователя

            и вернется None 
    
    """
    await state.clear() # закрытие ожидания состояния 
    

async def show_help_info(message: Message):
    command_list = {
        "/start": "Старт работы с ботом",
        "/help": "Вывод базовых команд",
        "/description": "Описание работы с ботом"
    } 
    msg = ""
    for key, value in command_list.items():
        msg += f"{key}: {value}\n"

    await message.answer(f"Список команд:\n{msg}") 


async def show_description(message : Message):
    msg = "Использование бота:\n1. Регистрация (команда /start)\n2. Выбор операции:\n\t2.1 Посмотреть список криптовалют\n\t2.2 Посмотреть цену криптовалюты" 
    await message.answer(msg)

async def pagination_handler(call: CallbackQuery, callback_data: Pagination):

    page_num = int(callback_data.page)
    page = page_num - 1 if page_num > 0 else 0

    if callback_data.action == "next":
        page = page_num + 1 if page_num < (len(all_crypts) - 1) else page_num

    with suppress(TelegramBadRequest):
        await call.message.edit_text(
            f"{all_crypts[page][0]} <b>{all_crypts[page][1]}</b>",
            reply_markup=paginator(page),
        )

    await call.answer()

async def show_crypto_list(message:Message):
    await message.answer(f"{all_crypts[0][0]}) <b>{all_crypts[0][1]}</b>", reply_markup=paginator())    


async def start_crypto(message: Message, state: FSMContext):
    await state.set_state(CryptoState.crypto_name)
    await message.answer("Введите валюту, которой хотите получить курс\nADAUSDT")


async def get_crypto(message: Message, state: FSMContext):
    crypto_name = message.text.upper()
    await state.update_data(crypto_name=crypto_name)

    data = await state.get_data()
    crypt_s = data.get("crypto_name")
    crypt_data = await get_data(crypt_s)

    if crypt_data is None:  
        await message.answer("Криптовалюта не найдена. Проверьре коррекность названия валюты и введите еще раз😉")
    else:
        msg = ""
        course_headers = ["Название валюты", "Цена", "Временная метра"]
        for key, value in zip(course_headers, crypt_data.values()):
            msg += f"{key}: {value}\n"

        await message.answer(f"Полученные данные:\n\n{msg}")
        await state.clear()
   


    