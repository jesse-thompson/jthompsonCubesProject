# TODO: GUI shows list of entries with short versions
# TODO: Ensure widgets are not editable
import subprocess
import sys
from PyQt5 import QtSql
from PyQt5.QtSql import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from database import open_db, close_db


# establish connection to SQL db
def make_connection():
    db_connection = QSqlDatabase.addDatabase("QSQLITE")   # QSQLITE is the name of the driver
    db_connection.setDatabaseName("wufoo_entries.db")

    # Tries to open the connection. Handles errors with an error message
    if not db_connection.open():
        QMessageBox.critical(None, "Cubes Project List - Error!",
                             "Database Error: %s" % db_connection.lastError().databaseText(),)
        return False
    return True


class WufooEntries(QWidget):

    def __init__(self):
        super().__init__()
        self.db = QSqlQuery('SELECT * FROM entries')
        self.make_window()

    def on_click(self, item):
        click_query = QSqlQuery('SELECT * FROM entries')
        click_query.next()
        while str(click_query.value('org_name')) != item.text():
            click_query.next()
        position = str(click_query.value('title'))
        prefix = str(click_query.value('prefix'))
        f_name = str(click_query.value('f_name'))
        l_name = str(click_query.value('l_name'))
        org_name = str(click_query.value('org_name'))
        email = str(click_query.value('email'))
        QMessageBox.information(self, "ListWidget", f"{position} {prefix} {f_name} {l_name} {org_name} {email}")
        print(f"{position} {prefix} {f_name} {l_name} {org_name} {email}")

    def make_window(self):
        self.setWindowTitle("Cubes Project List")
        self.setGeometry(750, 100, 900, 500)

        # building the selection based on org names
        list_of_orgs = QListWidget(self)
        build_query = QSqlQuery('SELECT * FROM entries')
        index = build_query.record().indexOf('org_name')
        while build_query.next():
            list_of_orgs.addItem(str(build_query.value(index)))
        list_of_orgs.itemClicked.connect(self.on_click)
        list_of_orgs.move(10, 10)

        # table_of_details = QListWidget
        # position = QLabel('Position')


