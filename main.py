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


# the form hash is the form ID
def get_form_hash():
    config = configparser.ConfigParser()
    config.read('app.config')
    form_hash_from_file = config['secrets']['form_hash']
    return form_hash_from_file


# parses the raw response, creates file, and saves data from response in easily referenced format
def make_responses_file(api_response):
    f = open('form_responses_file', 'w', encoding="utf-8")
    with open('form_responses_file', 'w', encoding="utf-8") as f:
        file_data = f.write(f"Entry ID: {api_response.get('EntryId')}\n"
                            f"Date Created: {api_response.get('DateCreated')}\n"
                            f"Prefix: {api_response.get('Field2')}\n"
                            f"First Name: {api_response.get('Field3')}\n"
                            f"Last Name: {api_response.get('Field4')}\n"
                            f"Title: {api_response.get('Field5')}\n"
                            f"Organization Name: {api_response.get('Field6')}\n"
                            f"Email: {api_response.get('Field7')}\n"
                            f"Organization Website: {api_response.get('Field8')}\n"
                            f"Phone #: {api_response.get('Field9')}\n"
                            f"Interests:\n  {api_response.get('Field10')}\n  {api_response.get('Field11')}\n"
                            f"  {api_response.get('Field12')}\n  {api_response.get('Field13')}\n"
                            f"  {api_response.get('Field14')}\n  {api_response.get('Field15')}\n"
                            f"  {api_response.get('Field16')}\n"
                            f"Collaboration Time:\n  {api_response.get('Field110')}\n"
                            f"  {api_response.get('Field111')}\n  {api_response.get('Field112')}\n"
                            f"  {api_response.get('Field113')}\n  {api_response.get('Field114')}\n"
                            f"Permission Granted: {api_response.get('Field210')}")


# unused appending of responses file
# def append_responses_file(api_response):
#     f = open('form_responses_file', 'a', encoding="utf=8")


# Following code adapted from wufoo API documentation
# Authentication formatting
base_url = 'https://{}.wufoo.com/api/v3/'.format(get_subdomain())
username = get_apikey()
password = 'footastic'  # this can nonsense as per documentation as it is not checked

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
response = urllib.request.urlopen(base_url + f'forms/{get_form_hash()}/entries.json?')
data = json.loads(response.read())
# End of code adapted from wufoo API documentation

# json_response = json.dumps(data, indent=4, sort_keys=True)
# json_response = response.json()

make_responses_file(data)

with open('form_responses_file', 'r', encoding="utf-8") as file:
    print(file.read())

print()

# TODO: parse response to change "Field#" into the field names
# TODO: save reformatted response to file
# TODO: linter
# TODO: add README.md
