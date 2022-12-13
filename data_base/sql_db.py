from data_base import sqlite_db
from data_base import postgesql_db


def sql_start():
    sqlite_db.sql_start()
    # postgesql_db.sql_start()


def sql_close():
    sqlite_db.sql_close()
    # postgesql_db.sql_close()

def sql_add_id_table_command(id):
    sqlite_db.sql_add_id_table_command(id)
    # postgesql_db.sql_add_id_table_command(id)


def sql_add_text_command(id, en, ru):
    sqlite_db.sql_add_text_command(id, en, ru)
    # postgesql_db.sql_add_text_command(id, en, ru)


def sql_read_base(id):
    return sqlite_db.sql_read_base(id)
    # return postgesql_db.sql_read_base(id)


def sql_update_date(id, en):
    sqlite_db.sql_update_date(id, en)
    # postgesql_db.sql_update_date(id, en)


def sql_del_command(id, en):
    sqlite_db.sql_del_command(id, en)
    # postgesql_db.sql_del_command(id, en)
