import sqlite3 as sq


def sql_start():
    global base, cur
    base = sq.connect('translate_memo.db')
    cur = base.cursor()
    if base:
        print('SQLite base connected OK')


def sql_add_id_table_command(id):
    base.execute(f'CREATE TABLE IF NOT EXISTS id{id}(en PRIMARY KEY, ru)')
    base.commit()


def sql_add_text_command(id, en, ru):
    cur.execute(f'INSERT INTO id{id} VALUES (?, ?)', (en, ru))
    base.commit()


def sql_read_base(id):
    return cur.execute(f'SELECT * FROM id{id}').fetchall()


def sql_del_command(id, en):
    cur.execute(f'DELETE FROM id{id} WHERE en = \'{en}\'')
    base.commit()
