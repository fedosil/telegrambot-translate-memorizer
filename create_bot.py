from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from sys import exit
from config_reader import config

storage = MemoryStorage()

token = config.bot_token.get_secret_value()
if not token:
    exit('Error: not token provided')

bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)


