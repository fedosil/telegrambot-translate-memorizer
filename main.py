from aiogram.utils import executor
from create_bot import dp
from handlers import start, translate, memorize
from data_base import sql_db
import logging

logging.basicConfig(level=logging.INFO)

start.register_handlers_start(dp)
memorize.register_handlers_memorize(dp)
translate.register_handlers_translate(dp)


async def on_startup(_):
    sql_db.sql_start()

async def on_shutdown(_):
    sql_db.sql_close()

executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
