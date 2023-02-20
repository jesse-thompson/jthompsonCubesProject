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

# db = QSqlDatabase.addDatabase("QSQLITE")
# db.setDatabaseName("wufoo_entries.db")
# query = QtSql.QSqlQuery()
# entries = query.exec('SELECT * FROM entries')

def initializeModel(model):
   model.setTable('sportsmen')
   model.setEditStrategy(QSqlTableModel.OnFieldChange)
   model.select()
   model.setHeaderData(0, Qt.Horizontal, "ID")
   model.setHeaderData(1, Qt.Horizontal, "First name")
   model.setHeaderData(2, Qt.Horizontal, "Last name")

def createView(title, model):
   view = QTableView()
   view.setModel(model)
   view.setWindowTitle(title)
   return view

def addrow():
   print (model.rowCount())
   ret = model.insertRows(model.rowCount(), 1)
   print (ret)

def findrow(i):
   delrow = i.row()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   db = QSqlDatabase.addDatabase('QSQLITE')
   db.setDatabaseName('sportsdatabase.db')
   model = QSqlTableModel()
   delrow = -1
   initializeModel(model)

   view1 = createView("Table Model (View 1)", model)
   view1.clicked.connect(findrow)

   dlg = QDialog()
   layout = QVBoxLayout()
   layout.addWidget(view1)

   button = QPushButton("Add a row")
   button.clicked.connect(addrow)
   layout.addWidget(button)

   btn1 = QPushButton("del a row")
   btn1.clicked.connect(lambda: model.removeRow(view1.currentIndex().row()))
   layout.addWidget(btn1)

   dlg.setLayout(layout)
   dlg.setWindowTitle("Database Demo")
   dlg.show()
   sys.exit(app.exec_())


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


# cubes_app = QApplication([])
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
