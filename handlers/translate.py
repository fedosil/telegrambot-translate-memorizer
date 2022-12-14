from create_bot import dp, bot
from aiogram import types, Dispatcher
from aiohttp import ClientSession
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from data_base import sql_db
from libretranslatepy import LibreTranslateAPI
import string


async def get_detect_language_api(text):
    async with ClientSession() as session:
        url = 'https://translate.argosopentech.com/detect'
        async with session.post(url=url, data={'q': text}) as response:
            if response:
                response_json = await response.json()
                return response_json[0]['language']
            raise response.status


async def get_translate_api(text, source, target):
    async with ClientSession() as session:
        url = 'https://libretranslate.de/translate'
        data = {'q': text, 'source': source, 'target': target}
        async with session.post(url, data=data) as response:
            if response:
                translate_json = await response.json()
                return translate_json['translatedText']
            raise response.status


def libretranslatepy_get_traslate(text, source, target):
    lt = LibreTranslateAPI("https://translate.argosopentech.com/")
    res = lt.translate(text, source, target)
    return res


def detect_language(text):
    RUSSIAN_LATTERS = {chr(i) for i in range(1072, 1104)}
    # ENGLISH_LATTERS = set(string.ascii_lowercase)
    set_text = set(text)
    if set_text.intersection(RUSSIAN_LATTERS):
        return 'ru', 'en'
    # if set_text.intersection(ENGLISH_LATTERS):
    return 'en', 'ru'


async def handle_translate(text):
    source, target = detect_language(text.lower())
    # translate_text = await get_translate_api(text, source, target)
    translate_text = libretranslatepy_get_traslate(text, source, target)
    return translate_text, source


# @dp.register_message_handler()
async def register_translate(message: types.Message):
    translate_text, source = await handle_translate(message.text)
    if len(message.text.split()) <= 4:
        await message.reply(
            text=translate_text,
            reply_markup=InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Добавить', callback_data='add'))
        )
    else:
        await message.reply(text=translate_text)



# @dp.message_handler(commands='id')
# async def get_id(message: types.Message):
#     await message.answer(message.from_user.id)


# @dp.callback_query_handler(text='add')
async def add_callback_run(callback: types.CallbackQuery):
    message_text = callback.message.reply_to_message['text']
    translate_text, source = await handle_translate(message_text)
    en, ru = message_text, translate_text
    if source == 'ru':
        ru, en = en, ru
    sql_db.sql_add_text_command(callback.from_user.id, en, ru)
    await callback.answer('✅')


def register_handlers_translate(dp: Dispatcher):
    # dp.register_message_handler(get_id, commands='id')
    dp.register_message_handler(register_translate)
    dp.register_callback_query_handler(add_callback_run, text='add')
