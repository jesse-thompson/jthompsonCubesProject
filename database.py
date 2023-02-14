import sqlite3
from typing import Tuple


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)
    cursor = db_connection.cursor()
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()
    connection.close()


def make_response_database(filename: str):
    conn, cursor = open_db(filename)
    cursor.execute('''CREATE TABLE IF NOT EXISTS entries(id INTEGER PRIMARY KEY, 
                    prefix TEXT NOT NULL, 
                    f_name TEXT NOT NULL, 
                    l_name TEXT NOT NULL, 
                    title TEXT NOT NULL, 
                    org_name TEXT NOT NULL, 
                    email TEXT NOT NULL, 
                    org_site TEXT NOT NULL, 
                    phone TEXT NOT NULL, 
                    interest1, interest2, interest3, interest4, interest5, interest6, interest7, 
                    colTime1, colTime2, colTime3, colTime4, colTime5, 
                    permission_grant REAL DEFAULT 'No',
                    date_created TEXT NOT NULL,
                    created_by TEXT NOT NULL,
                    date_updated TEXT NOT  NULL,
                    updated_by TEXT NOT NULL)''')
    close_db(conn)


def input_entries(response_file: str, table: str):
    with open(response_file, 'r') as data:
        data_text = data.read().splitlines()
        it = [iter(data_text)] * 26
        data_tuples = zip(*it)

        conn, cursor = open_db(table)
        cursor.executemany('''INSERT OR IGNORE INTO entries 
                           VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', data_tuples)
        close_db(conn)
