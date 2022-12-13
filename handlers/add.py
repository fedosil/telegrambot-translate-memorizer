from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from data_base import sqlite_db
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from keyboard import kb_user

class AddWord(StatesGroup):
    waiting_for_en_word = State()
    waiting_for_ru_word = State()

