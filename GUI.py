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


class WufooEntries(QListWidget):

    def on_click(self, item):

        QMessageBox.warning(self, "ListWidget", "clicked: " + item.text())


cubes_app = QApplication([])    # empty list to prevent configurations of PyQt from terminal
if not make_connection():
    sys.exit(1)

view = WufooEntries()
view.resize(1000, 500)

query = QSqlQuery('SELECT * FROM entries')
index = query.record().indexOf('org_name')
while query.next():
    view.addItem(str(query.value(index)))



view.setWindowTitle('Cubes Project List')
view.itemClicked.connect(view.on_click)

view.show()

sys.exit(cubes_app.exec_())
