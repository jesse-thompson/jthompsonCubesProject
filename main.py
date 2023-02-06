import urllib.request
import sys
import configparser
import json
import sqlite3
from typing import Tuple

config = configparser.ConfigParser()


# the subdomain is the username for the Wufoo account
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


def make_response_database(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS entries(id INTEGER PRIMARY KEY, 
                    created TEXT NOT NULL, 
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
                    perm_grant REAL DEFAULT 'No')''')


def input_entries(cursor: sqlite3.Cursor):
    f = open('form_responses_file', 'r')
    data = f.read().splitlines()

    cursor.executemany('''INSERT INTO ENTRIES (id, created, prefixm, f_name, l_name, title, org_name, email, org_site,
                    phone, interest1, interest2, interest3, interest4, interest5, interest6, interest7, colTime1,
                    colTime2, colTime3, colTime4, colTime5, perm_grant) 
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', data)


# parses the raw response, creates file, and saves data from response in easily referenced format
def make_responses_file(api_response):
    with open('form_responses_file', 'w') as f:
        f.write(f"{api_response['Entries'][0]['EntryId']}\n"
                f"{api_response['Entries'][0]['DateCreated']}\n"
                f"{api_response['Entries'][0]['Field2']}\n"
                f"{api_response['Entries'][0]['Field3']}\n"
                f"{api_response['Entries'][0]['Field4']}\n"
                f"{api_response['Entries'][0]['Field5']}\n"
                f"{api_response['Entries'][0]['Field6']}\n"
                f"{api_response['Entries'][0]['Field7']}\n"
                f"{api_response['Entries'][0]['Field8']}\n"
                f"{api_response['Entries'][0]['Field9']}\n"
                f"{api_response['Entries'][0]['Field10']}\n"
                f"{api_response['Entries'][0]['Field11']}\n"
                f"{api_response['Entries'][0]['Field12']}\n"
                f"{api_response['Entries'][0]['Field13']}\n"
                f"{api_response['Entries'][0]['Field14']}\n"
                f"{api_response['Entries'][0]['Field15']}\n"
                f"{api_response['Entries'][0]['Field16']}\n"
                f"{api_response['Entries'][0]['Field110']}\n"
                f"{api_response['Entries'][0]['Field111']}\n"
                f"{api_response['Entries'][0]['Field112']}\n"
                f"{api_response['Entries'][0]['Field113']}\n"
                f"{api_response['Entries'][0]['Field114']}\n"
                f"{api_response['Entries'][0]['Field210']}")


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

    make_responses_file(response)
    input_entries(sqlite3.Cursor)

    # conn, cursor = open_db("wufoo_entries.db")
    # print(type(conn))
    # input_entries()
    # close_db(conn)

    # with open('form_responses_file', 'r') as file:
    #     print(file.read())

    # f = open('form_responses_file', 'r')
    # data = f.read().splitlines()
    # print(data)


if __name__ == '__main__':
    main()
