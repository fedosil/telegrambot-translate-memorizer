from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from os import getenv
from sys import exit

storage = MemoryStorage()

token = '5408384541:AAHgzaOrDzNedrXi-2D-pLCGtqESJKCPfxs'
# token = getenv('TOKEN')
if not token:
    exit('Error: not token provided')

bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)


