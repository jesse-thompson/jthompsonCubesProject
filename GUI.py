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
        # query1 = QSqlQuery('SELECT * FROM entries')
        # position = QLabel(query1.record())
        pass

    def make_window(self):
        self.setWindowTitle("Cubes Project List")
        self.setGeometry(750, 100, 900, 200)
        if not make_connection():
            sys.exit(1)

        view = QListWidget

        query = QSqlQuery('SELECT * FROM entries')
        index = query.record().indexOf('org_name')
        while query.next():
            view.addItem(str(query.value(index)))

        view.itemClicked.connect(view.on_click)

