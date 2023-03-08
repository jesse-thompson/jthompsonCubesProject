# Code2 from Dr. John F. Santore's Sprint 3 Instructor Demo used as basis for Sprint 4

import sys

import PySide6

import DisplayWufooWindow
from DatabaseStuff import open_db, close_db
import DatabaseStuff
import getData

db_name = "cubesProject.sqlite"


def sprint2():  # comment for force workflow
    json_response = getData.get_wufoo_data()
    entries_list = json_response["Entries"]
    # print(entries_list[10])
    conn, cursor = open_db(db_name)
    DatabaseStuff.create_entries_table(cursor)
    DatabaseStuff.add_entries_to_db(cursor, entries_list)
    close_db(conn)


def sprint3():
    qt_app = PySide6.QtWidgets.QApplication(sys.argv)  # sys.argv is the list of command line arguments
    my_window = DisplayWufooWindow.WuFooEntriesWindow()
    my_window.setWindowTitle("CUBES Project")
    sys.exit(qt_app.exec())


def show_options():
    print("=======================================")
    print("[1] Update the database with wufoo data")
    print("[2] Run the Graphical Program")
    print("=======================================")


def main():
    show_options()
    answer = input("Please enter your choice: ")
    if answer == "1":
        sprint2()
    elif answer == "2":
        sprint3()
    else:
        print("Invalid Entry, ending program...")
        sys.exit(0)  # exit successfully


if __name__ == "__main__":
    main()
