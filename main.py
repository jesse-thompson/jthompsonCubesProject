import urllib.request
import sys
import json
import sqlite3
from typing import Tuple
import secrets

# TODO: finish readme


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


# parses the raw response, creates file, and saves data from response in easily referenced format
def make_responses_file(api_response: list, data_file=None):
    for entry in api_response:
        for key, value in entry.items():
            print(f"{value}", file=data_file)
        # print("+++\n___", file=data_file)  # separator


def get_response(url, api_key):
    # Following code is adapted, with slight modifications, from Wufoo API documentation
    # Authentication for requests
    password_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_manager.add_password(None, url, api_key, "nonsense")  # nonsense is 'password' that isn't checked
    handler = urllib.request.HTTPBasicAuthHandler(password_manager)

    # Create and install an opener using the AuthHandler
    opener = urllib.request.build_opener(handler)
    urllib.request.install_opener(opener)

    response = urllib.request.urlopen(url + f'forms/z1pdyem009hdgsr/entries.json?')  # gibberish is form's hash
    if response.code != 200:
        print(f"Request failed, form data not retrieved.\n"
              f"Response Code: {response.code}\n"
              f"Error Message: {response.reason}")
        sys.exit(-1)
    data = json.loads(response.read())
    # End of code adapted from Wufoo API documentation

    return data


def main():
    # Authentication formatting
    base_url = 'https://{}.wufoo.com/api/v3/'.format("jessethompson")   # name is the subdomain of Wufoo acct
    response = get_response(base_url, secrets.apikey)
    response_list = response["Entries"]
    with open("form_responses_file", 'w') as form_save:
        make_responses_file(response_list, data_file=form_save)

    make_response_database('wufoo_entries.db')
    input_entries('form_responses_file', 'wufoo_entries.db')


if __name__ == '__main__':
    main()
