from create_bot import dp, bot
from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from data_base import sql_db
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from keyboard import kb_user
import random


class RepeatWord(StatesGroup):
    waiting_for_word = State()


def get_words(id):
    base_words = sql_db.sql_read_base(id)
    en, ru = base_words[0][1], base_words[0][2]
    words_list = [ru]
    for word in base_words[1:]:
        words_list.append(word[2])
        if len(words_list) == 9:
            break
    random.shuffle(words_list)
    return en, ru, words_list


async def del_callback_run(callback: types.CallbackQuery):
    await callback.answer('del')


async def question_word(message: types.Message, state: FSMContext):
    try:
        en, ru, words_list = get_words(message.from_user.id)
    except:
        await message.answer('Добавьте слов для изучения')
    else:
        await state.update_data(id_user=message.from_user.id, en=en, ru=ru)
        kb_question = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(*words_list)
        await message.answer(en, reply_markup=kb_question)
        await state.set_state(RepeatWord.waiting_for_word.state)

async def response_word(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    if message.text == user_data['ru']:
        await message.reply('Верно', reply_markup=kb_user)
        sql_db.sql_update_date(user_data['id_user'], user_data['en'])
        await state.finish()
    elif message.text in ['/Удалить', '/удалить', '/del']:
        sql_db.sql_del_command(user_data['id_user'], user_data['en'])
        await message.reply(f'Слово {user_data["en"]} удалено', reply_markup=kb_user)
        await state.finish()
    else:
        await message.reply('Нет')
        await message.answer(user_data['en'])
        return


def register_handlers_memorize(dp: Dispatcher):
    dp.register_callback_query_handler(del_callback_run, text='del')
    dp.register_message_handler(question_word, commands='Повторить', state="*")
    dp.register_message_handler(response_word, state=RepeatWord.waiting_for_word)
