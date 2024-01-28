from aiogram import Bot
from aiogram.types import Message
from keyboards.default.register_kb import register_keyboard 
from keyboards.default.crypto_kb import crypto_keyboard
from utils.db.storage import DatabaseManager
from utils.api.fetch_data_api import get_crypto_symbols

async def get_start(message: Message, bot: Bot):
    db = DatabaseManager("data/database.db")
    users = db.select_user_id(message.from_user.id)
    symbols = db.select_symbols()

    
    if symbols is None:
        symbols = await get_crypto_symbols()
        db.add_crypto(symbols.get("symbols")) 

    if users:
        await message.answer(f' Здравствуйте, {users[-1]}', reply_markup=crypto_keyboard)
    else:
        await bot.send_message(message.from_user.id, f"Привет, я криптобот, могу помочь тебе с определением курса любых валют!", reply_markup=register_keyboard)
        