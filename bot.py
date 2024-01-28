import sys
import asyncio
import logging

from keyboards.default.pagination_kb import Pagination, paginator
from aiogram import F
from loader import bot, dp

from aiogram.filters import Command
from states.crypto import CryptoState
from utils.commands import set_commands
from states.register import RegisterState
from handlers.start_handler import get_start
from handlers.handlers import start_register, register_name, start_crypto, get_crypto, show_crypto_list, pagination_handler, show_help_info, show_description

# Регистрация слушателей событий
dp.message.register(get_start, Command("start")) # регистрация для команды "start"
# Регистрация register_handler
dp.message.register(start_register, F.text == "Зарегистрировать аккаунт") # Елси text == "Зарегистрировать аккаунт", то срабатывает данная функция  


"""
Метод: 
-> dp.message.register(register_name, RegisterState.regName) 

второй параметр метода  dp.message.register действительно используется в качестве фильтра. 
Этот параметр представляет собой состояние (state) беседы, в котором должен находиться чат, 
чтобы зарегистрированный обработчик был запущен.
----------

так же можно и со всеми состояниями
Например:
    Регистраиця номер телефона/почты

    dp.message.register(register_phone|email, RegisterState.phone|mail)
"""


dp.message.register(register_name, RegisterState.regname)
dp.message.register(show_help_info, Command("help"))
dp.message.register(show_description, Command("description"))
dp.message.register(show_crypto_list, F.text == "Посмотреть список криптовалют")
dp.message.register(start_crypto, F.text == "Посмотреть цену криптовалюты")
dp.callback_query.register(pagination_handler, Pagination.filter(F.action.in_(["prev", "next"])))
dp.message.register(get_crypto, CryptoState.crypto_name)


async def main() -> None:
    await set_commands(bot) # register command in pop up menu 
    await dp.start_polling(bot) 

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout) # log
    asyncio.run(main())

"""


добавить обработчики на 
    /help

затем (handlers) на 
    "Добаивть крипту"
    "Посмотреть крипту"

"""
