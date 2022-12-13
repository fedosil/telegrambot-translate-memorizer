from create_bot import dp, bot
from aiogram import types, Dispatcher
from data_base import sql_db
from keyboard import kb_user

# @dp.register_message_handler(commands=['start'])
async def start_command(message: types.Message):
    sql_db.sql_add_id_table_command(message.from_user.id)
    await message.answer(f'Hello, your id {message.from_user.id} table created', reply_markup=kb_user)

def register_handlers_start(dp:Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])