import urllib.request
import sys
import json


def get_response(url, api_key):
    # Following code is adapted, with slight modifications, from Wufoo API documentation
    # Authentication for requests
    password_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_manager.add_password(None, url, api_key, "nonsense")  # nonsense is 'password' that isn't checked
    handler = urllib.request.HTTPBasicAuthHandler(password_manager)

    # Create and install an opener using the AuthHandler
    opener = urllib.request.build_opener(handler)
    urllib.request.install_opener(opener)

    response = urllib.request.urlopen(url + 'forms/z1pdyem009hdgsr/entries.json?')  # gibberish is form's hash
    if response.code != 200:
        print(f"Request failed, form data not retrieved.\n"
              f"Response Code: {response.code}\n"
              f"Error Message: {response.reason}")
        sys.exit(-1)
    data = json.loads(response.read())
    # End of code adapted from Wufoo API documentation

    return data


# parses the raw response, creates file, and saves data from response in easily referenced format
def make_responses_file(api_response: list, data_file=None):
    for entry in api_response:
        for key, value in entry.items():
            print(f"{value}", file=data_file)
