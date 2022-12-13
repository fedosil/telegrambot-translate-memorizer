from data_base import sqlite_db as db
# from data_base import postgesql_db as db


def sql_start():
    db.sql_start()
    # postgesql_db.sql_start()


def sql_close():
    db.sql_close()
    # postgesql_db.sql_close()

def sql_add_id_table_command(id):
    db.sql_add_id_table_command(id)
    # postgesql_db.sql_add_id_table_command(id)


def sql_add_text_command(id, en, ru):
    db.sql_add_text_command(id, en, ru)
    # postgesql_db.sql_add_text_command(id, en, ru)


def sql_read_base(id):
    return db.sql_read_base(id)
    # return postgesql_db.sql_read_base(id)


def sql_update_date(id, en):
    db.sql_update_date(id, en)
    # postgesql_db.sql_update_date(id, en)


def sql_del_command(id, en):
    db.sql_del_command(id, en)
    # postgesql_db.sql_del_command(id, en)
