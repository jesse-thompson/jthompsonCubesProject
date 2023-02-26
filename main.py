import sys
import PyQt5
from secrets import apikey  # requires a secrets file in place of "secrets.template"
from dataRetrieval import get_response, make_responses_file
from database import make_response_database, input_entries
import GUI


def display_gui():
    cubes_app = PyQt5.QtWidgets.QApplication(sys.argv)  # sys.argv is the list of command line arguments
    GUI.make_connection()
    window = GUI.WufooEntries()
    window.show()
    sys.exit(cubes_app.exec())


def main():
    # Authentication formatting
    base_url = 'https://jessethompson.wufoo.com/api/v3/'
    response = get_response(base_url, apikey)
    response_list = response["Entries"]
    with open("form_responses_file", 'w') as form_save:
        make_responses_file(response_list, data_file=form_save)

    make_response_database('wufoo_entries.db')
    input_entries('form_responses_file', 'wufoo_entries.db')
    display_gui()


if __name__ == '__main__':
    main()
