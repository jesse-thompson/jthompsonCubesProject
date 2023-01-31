import urllib.request
import urllib.response
import configparser
import json


# the subdomain is the username for the Wufoo account
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
        f.write(f"Entry ID: {api_response['Entries'][0]['EntryId']}\n"
                f"Date Created: {api_response['Entries'][0]['DateCreated']}\n"
                f"Prefix: {api_response['Entries'][0]['Field2']}\n"
                f"First Name: {api_response['Entries'][0]['Field3']}\n"
                f"Last Name: {api_response['Entries'][0]['Field4']}\n"
                f"Title: {api_response['Entries'][0]['Field5']}\n"
                f"Organization Name: {api_response['Entries'][0]['Field6']}\n"
                f"Email: {api_response['Entries'][0]['Field7']}\n"
                f"Organization Website: {api_response['Entries'][0]['Field8']}\n"
                f"Phone #: {api_response['Entries'][0]['Field9']}\n"
                f"Interests:\n  {api_response['Entries'][0]['Field10']}\n  {api_response['Entries'][0]['Field11']}\n"
                f"  {api_response['Entries'][0]['Field12']}\n  {api_response['Entries'][0]['Field13']}\n"
                f"  {api_response['Entries'][0]['Field14']}\n  {api_response['Entries'][0]['Field15']}\n"
                f"  {api_response['Entries'][0]['Field16']}\n"
                f"Collaboration Time:\n  {api_response['Entries'][0]['Field110']}\n"
                f"  {api_response['Entries'][0]['Field111']}\n  {api_response['Entries'][0]['Field112']}\n"
                f"  {api_response['Entries'][0]['Field113']}\n  {api_response['Entries'][0]['Field114']}\n"
                f"Permission Granted: {api_response['Entries'][0]['Field210']}")


# unused appending of responses file, may use later
# def append_responses_file(api_response):
#     f = open('form_responses_file', 'a', encoding="utf=8")


# Following code adapted from Wufoo API documentation
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
# End of code adapted from Wufoo API documentation

# json_response = json.dumps(data, indent=4, sort_keys=True)
# json_response = response.json()

make_responses_file(data)

with open('form_responses_file', 'r', encoding="utf-8") as file:
    print(file.read())
