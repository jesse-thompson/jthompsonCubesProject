import urllib.request
import urllib.response
import configparser
import json


def get_subdomain():
    config = configparser.ConfigParser()
    config.read('app.config')
    subdomain_from_file = config['secrets']['subdomain']
    return subdomain_from_file


def get_apikey():
    config = configparser.ConfigParser()
    config.read('app.config')
    apikey_from_file = config['secrets']['apikey']
    return apikey_from_file


def get_form_hash():
    config = configparser.ConfigParser()
    config.read('app.config')
    form_hash_from_file = config['secrets']['form_hash']
    return form_hash_from_file


# Authentication formatting
base_url = 'https://{}.wufoo.com/api/v3/'.format(get_subdomain())
username = get_apikey()
password = 'footastic'  # this can be any string as per documentation as it is not checked

# Create a password manager
password_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# Add the username and password (API key and nonsense value)
password_manager.add_password(None, base_url, username, password)

# Create the AuthHandler
handler = urllib.request.HTTPBasicAuthHandler(password_manager)

# Create and install an opener using the AuthHandler
opener = urllib.request.build_opener(handler)
urllib.request.install_opener(opener)

# Now each request we make will be authenticated
response = urllib.request.urlopen(base_url + f'forms/{get_form_hash()}/entries.json?sort=EntryId&sortDirection=DESC')
data = json.load(response)

print(json.dumps(data, indent=4, sort_keys=True))

# TODO: parse response to change "Field#" into the field names
# TODO: save reformatted response to file
# TODO: pytest
# TODO: linter
# TODO: add README.md
