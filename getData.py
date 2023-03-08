# Code from Dr. John F. Santore's Sprint 3 Instructor Demo used as basis for Sprint 4

import requests
import sys
from secrets import wufoo_key  # add a secrets file with wufoo_key='YoUr-WuFoo-KeY-Here'
from requests.auth import HTTPBasicAuth

# adjust this to your URL
url = "https://jessethompson.wufoo.com/api/v3/forms/cubes-project-proposal-submission/entries/json"


def get_wufoo_data() -> dict:
    response = requests.get(url, auth=HTTPBasicAuth(wufoo_key, "pass"))
    if response.status_code != 200:  # if we don't get an ok response we have trouble
        print(
            f"Failed to get data, response code:{response.status_code} and error message: {response.reason} "
        )
        sys.exit(-1)
    jsonresponse = response.json()
    return jsonresponse


def main():
    data = get_wufoo_data()
    data1 = data["Entries"]
    file_to_save = open("output.txt", "w")
    save_data(data1, save_file=file_to_save)


def save_data(data_to_save: list, save_file=None):
    for entry in data_to_save:
        for key, value in entry.items():
            print(f"{key}: {value}", file=save_file)
        # now print the spacer
        print(
            "+++++++++++++++++++++++++++++++++++++++++++++\n_______________________________________________",
            file=save_file,
        )


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()
