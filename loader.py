from aiogram import Bot, Dispatcher, types
from utils.db.storage import DatabaseManager

from data import confing


bot = Bot(token=confing.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()
# db = DatabaseManager('data/database.db')