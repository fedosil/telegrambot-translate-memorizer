import sqlite3 as sq
from datetime import datetime


def sql_start():
    global base, cursor
    base = sq.connect('translate_memo.db')
    cursor = base.cursor()
    if base:
        print('SQLite base connected OK')


def sql_close():
    cursor.close()
    base.close()


def sql_add_id_table_command(id):
    current_date = datetime.now().strftime('%Y %m %d')
    base.execute(
        f"""CREATE TABLE IF NOT EXISTS dict_en_user_id_{id}
        (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
        en_word text NOT NULL UNIQUE, 
        ru_word text NOT NULL, 
        repeat_date text DEFAULT CURRENT_TIMESTAMP);"""
    )
    base.commit()


def sql_add_text_command(id, en, ru):
    current_date = datetime.now().strftime('%Y %m %d')
    cursor.execute(
        f"""INSERT INTO dict_en_user_id_{id}(en_word, ru_word) VALUES (?, ?);""", (en, ru)
    )
    base.commit()


def sql_read_base(id):
    cursor.execute(
        f"""SELECT * FROM dict_en_user_id_{id} ORDER BY repeat_date;"""
    )
    return cursor.fetchall()


def sql_update_date(id, en):
    current_date = datetime.now().strftime('%Y %m %d')
    cursor.execute(
        f"""UPDATE dict_en_user_id_{id} SET repeat_date = CURRENT_TIMESTAMP WHERE en_word = ?""", (en,)
    )
    base.commit()


def sql_del_command(id, en):
    cursor.execute(
        f"""DELETE FROM dict_en_user_id_{id} WHERE en_word = ?;""", (en,)
    )
    base.commit()
