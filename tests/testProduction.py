import main
import secrets


# Compares retrieved number of entries to expected number of entries
def test_entry_retrieval():
    total_entries = 13
    url = 'https://{}.wufoo.com/api/v3/'.format("jessethompson")
    retrieved_entries = main.get_response(url, secrets.apikey)
    assert len(retrieved_entries['Entries']) == total_entries


def test_database_entry():
    total_entries = 13
    # url = 'https://{}.wufoo.com/api/v3/'.format(secrets.subdomain)
    # retrieved_entries = main.get_response(url, secrets.apikey)
    # entries_list = retrieved_entries['Entries']
    # with open("test_file", 'w') as form_save:
    #     main.make_responses_file(entries_list, data_file=form_save)

    main.make_response_database('testing.db')
    main.input_entries('test_file', 'testing.db')
    conn, cursor = main.open_db('testing.db')

    found_entries = cursor.execute('SELECT * FROM entries')
    num_entries = len(found_entries.fetchall())

    assert num_entries == total_entries
    main.close_db(conn)

# TODO: ensure tests work on GitHub Actions
