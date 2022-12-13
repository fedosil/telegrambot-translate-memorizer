import sqlite3 as sq


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
    base.execute(
        f"""CREATE TABLE IF NOT EXISTS dict_en_user_id_%s
            (
                id_word int GENERATED ALWAYS AS IDENTITY,
    	        en_word varchar(64) UNIQUE,
    	        ru_word varchar(64) UNIQUE,
                repeat_date date DEFAULT NOW()
            );""", (id,)
    )
    base.commit()


def sql_add_text_command(id, en, ru):
    cursor.execute(
        f"""INSERT INTO dict_en_user_id_%s(en_word, ru_word)
                VALUES
                (%s, %s);""", (id, en, ru)
    )
    base.commit()


def sql_read_base(id):
    cursor.execute(
        f"""SELECT * FROM dict_en_user_id_%s
                ORDER BY repeat_date;""", (id,)
    )
    return cursor.fetchall()

def sql_update_date(id, en):
    cursor.execute(
        f"""UPDATE dict_en_user_id_%s
            SET repeat_date = NOW()
            WHERE en_word = %s""", (id, en)
    )
    base.commit()


def sql_del_command(id, en):
    cursor.execute(
        f"""DELETE FROM dict_en_user_id_%s
                WHERE en_word = %s;""", (id, en)
    )
    base.commit()
