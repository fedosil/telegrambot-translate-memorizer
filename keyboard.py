from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # , ReplyKeyboardRemove

memorize = KeyboardButton('/Повторить')
add = KeyboardButton('/Добавить слово')

# kb_user = ReplyKeyboardMarkup(resize_keyboard=True).add(add).insert(memorize)
kb_user = ReplyKeyboardMarkup(resize_keyboard=True).add(memorize)
