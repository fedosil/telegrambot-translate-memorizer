from data_base import config
import psycopg2


def sql_start():
    global connection, cursor
    connection = psycopg2.connect(
        host=config.host,
        user=config.user,
        password=config.password,
        database=config.database
    )
    connection.autocommit = True
    cursor = connection.cursor()
    if connection:
        print('PostgeSQL base connected OK')


def sql_close():
    cursor.close()
    connection.close()


def sql_add_id_table_command(id):
    cursor.execute(
        f"""CREATE TABLE IF NOT EXISTS dict_en_user_id_%s
        (
            id_word int GENERATED ALWAYS AS IDENTITY,
	        en_word varchar(64) UNIQUE,
	        ru_word varchar(64) UNIQUE,
            repeat_date date DEFAULT NOW()
        );""", (id,)
    )


def sql_add_text_command(id, en, ru):
    cursor.execute(
        f"""INSERT INTO dict_en_user_id_%s(en_word, ru_word)
            VALUES
            (%s, %s);""", (id, en, ru)
    )


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


def sql_del_command(id, en):
    cursor.execute(
        f"""DELETE FROM dict_en_user_id_%s
            WHERE en_word = %s;""", (id, en)
    )
