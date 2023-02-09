import main


# Compares retrieved number of entries to expected number of entries
def test_entry_retrieval():
    url = 'https://{}.wufoo.com/api/v3/'.format("jessethompson")
    u_name = main.get_apikey()
    entries = main.get_response(url, u_name)
    print(entries)

# TODO: make tests
# TODO: ensure tests work on GitHub Actions
