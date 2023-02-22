# TODO: Add basic GUI functionality
# TODO: GUI shows list of entries with short versions
# TODO: GUI shows selected entry
# TODO: Ensure widgets are not editable
import sys
from PyQt5 import QtSql
from PyQt5.QtSql import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class WufooEntries(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Cubes Project List")
        self.resize(500, 500)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout(self.centralWidget)
        query = QSqlQuery("""SELECT * from ENTRIES""")
        self.view = QTableWidget()

        index = query.record().indexOf('org_name')
        while query.next():
            self.button = QPushButton(str(query.value(index)), self)
            self.button.clicked.connect(self.on_click)
            self.layout.addWidget(self.button)

        self.show()

        # self.view.setColumnCount(21)
        # self.view.setHorizontalHeaderLabels(["Prefix", "First Name", "Last Name", "Title", "Org Name", "Email",
        #                                      "Org Site", "Phone", "int1", "int2", "int3", "int4", "int5", "in6",
        #                                      "int7", "col time1", "col time2", "col time3", "col time4",
        #                                      "col time5", "Permission"])
        # while query.next():
        #     rows = self.view.rowCount()
        #     self.view.setRowCount(rows + 1)
        #     self.view.setItem(rows, 0, QTableWidgetItem(str(query.value(0))))
        #     for col_num in range(1, 21):
        #         self.view.setItem(rows, col_num, QTableWidgetItem(query.value(col_num)))
        # self.view.resizeColumnsToContents()
        # self.setCentralWidget(self.view)

    @pyqtSlot()
    def on_click(self):
        print('clicked')


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


cubes_app = QApplication([])    # empty list to prevent configurations of PyQt from terminal
if not make_connection():
    sys.exit(1)
window = WufooEntries()
window.show()
sys.exit(cubes_app.exec_())


# table_query = QSqlQuery()
#
# table_query.exec("""SELECT f_name, l_name, email FROM entries""")
#
# print(table_query.seek(11, relative=False))
""" Old stuff
fname, lname, email = range(3)
print(table_query.value(fname))
print(table_query.value(lname))


def setup_gui(self, main_window):
    main_window.set

def __init__(self):
    super().__init__(parent=None)
    self.setWindowTitle("Qubes Project List")


def create_entry_list(self):
    layout = QVBoxLayout()
    layout.addWidget(QPushButton('Entry1'))
    layout.addWidget(QPushButton('Entry2'))


def greet():
    if msgLabel.text():
        msgLabel.setText("")
    else:
        msgLabel.setText("Hello, World!")


window = QWidget()
window.setWindowTitle("Cubes Project List")
layout = QVBoxLayout()

button = QPushButton("Greet")
button.clicked.connect(greet)

layout.addWidget(button)
msgLabel = QLabel("")
layout.addWidget(msgLabel)
window.setLayout(layout)
window.setGeometry(100, 100, 1920, 1080)

palette = QPalette()
palette.setColor(QPalette.ButtonText, Qt.red)
cubes_app.setPalette(palette)
cubes_app.setStyleSheet("QLabel { margin: 0.5ex; }")
cubes_app.setStyleSheet("QPushButton { margin: ex; }")

window.show()
sys.exit(cubes_app.exec())
"""
