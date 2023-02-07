import urllib.request
import sys
import configparser
import json
import sqlite3
from typing import Tuple

config = configparser.ConfigParser()


# the subdomain is the username for the Wufoo account
# comment to test workflow
def get_subdomain():
    config.read('app.config')
    subdomain_from_file = config['secrets']['subdomain']
    return subdomain_from_file


def get_apikey():
    config.read('app.config')
    apikey_from_file = config['secrets']['apikey']
    return apikey_from_file


# the form hash is the form ID
def get_form_hash():
    config.read('app.config')
    form_hash_from_file = config['secrets']['form_hash']
    return form_hash_from_file


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


def input_entries(table: str):
    with open('form_responses_file', 'r') as data:
        conn, cursor = open_db(table)
        for line in data:
            data1 = line.split()
            cursor.executemany('''INSERT INTO entries 
                               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (data.read().splitlines(),))
        close_db(conn)


# parses the raw response, creates file, and saves data from response in easily referenced format
def make_responses_file(api_response: list, data_file=None):
    for entry in api_response:
        for key, value in entry.items():
            print(f"{value}", file=data_file)
        print("+++\n___", file=data_file)  # separator


def get_response(url, api_key):
    # Following code is adapted from Wufoo API documentation
    # Authentication for requests
    password_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_manager.add_password(None, url, api_key, "nonsense")  # nonsense is 'password' that isn't checked
    handler = urllib.request.HTTPBasicAuthHandler(password_manager)

    # Create and install an opener using the AuthHandler
    opener = urllib.request.build_opener(handler)
    urllib.request.install_opener(opener)

    response = urllib.request.urlopen(url + f'forms/{get_form_hash()}/entries.json?')
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
    base_url = 'https://{}.wufoo.com/api/v3/'.format(get_subdomain())
    username = get_apikey()
    response = get_response(base_url, username)
    response_list = response["Entries"]
    with open("form_responses_file", 'w') as form_save:
        make_responses_file(response_list, data_file=form_save)

    f = open('form_responses_file')
    with open("new_file", 'w') as new_file:

        print(f.read().splitlines(), file=new_file)
    with open("new_file", 'r') as x:
        print(x.read())
    make_response_database('wufoo_entries.db')
    input_entries('wufoo_entries.db')

    # with open('form_responses_file', 'r') as file:
    #     print(file.read())

    # f = open('form_responses_file', 'r')
    # data = f.read().splitlines()
    # print(data)


if __name__ == '__main__':
    main()
