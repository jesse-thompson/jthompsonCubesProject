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

# establish connection to SQL db
db_connection = QSqlDatabase.addDatabase("QSQLITE")   # QSQLITE is the name of the driver
db_connection.setDatabaseName("wufoo_entries.db")

cubes_app = QApplication(sys.argv)


# Tries to open the connection. Handles errors with an error message
if not db_connection.open():
    QMessageBox.critical(None, "Cubes Project List - Error!",
                         "Database Error: %s" % db_connection.lastError().databaseText(),)
    sys.exit(1)
db_connection.close()


window = QLabel("Connection established")
window.setWindowTitle("Cubes Project List")
window.resize(500, 500)
window.show()
sys.exit(cubes_app.exec_())

# query = QtSql.QSqlQuery()
# entries = query.exec('SELECT * FROM entries')


# def setup_gui(self, main_window):
#     main_window.set

# def __init__(self):
#     super().__init__(parent=None)
#     self.setWindowTitle("Qubes Project List")
#
#
# def create_entry_list(self):
#     layout = QVBoxLayout()
#     layout.addWidget(QPushButton('Entry1'))
#     layout.addWidget(QPushButton('Entry2'))


# def greet():
#     if msgLabel.text():
#         msgLabel.setText("")
#     else:
#         msgLabel.setText("Hello, World!")


# window = QWidget()
# window.setWindowTitle("Cubes Project List")
# layout = QVBoxLayout()

# button = QPushButton("Greet")
# button.clicked.connect(greet)

# layout.addWidget(button)
# msgLabel = QLabel("")
# layout.addWidget(msgLabel)
# window.setLayout(layout)
# window.setGeometry(100, 100, 1920, 1080)

# palette = QPalette()
# palette.setColor(QPalette.ButtonText, Qt.red)
# cubes_app.setPalette(palette)
# cubes_app.setStyleSheet("QLabel { margin: 0.5ex; }")
# cubes_app.setStyleSheet("QPushButton { margin: ex; }")

# window.show()
# sys.exit(cubes_app.exec())
