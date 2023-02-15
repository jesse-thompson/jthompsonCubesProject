# TODO: Add basic GUI functionality
# TODO: GUI shows list of entries with short versions
# TODO: GUI shows selected entry
# TODO: Ensure widgets are not editable

import PyQt5
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

cubes_app = QApplication([])

# palette = QPalette()
# palette.setColor(QPalette.ButtonText, Qt.red)
# cubes_app.setPalette(palette)
# cubes_app.setStyleSheet("QLabel { margin: 0.5ex; }")
# cubes_app.setStyleSheet("QPushButton { margin: ex; }")
#
# label = QLabel('CUBES Database')
#
# layout = QVBoxLayout()
# layout.addWidget(label)
# layout.addWidget(QPushButton('Entry1'))
# layout.addWidget(QPushButton('Entry2'))

button = QPushButton('Click')


def on_click_button():
    alert = QMessageBox()
    alert.setText("Clicked!")
    alert.exec()


button.click()
button.show()
# window = QWidget()
# window.setLayout(layout)
# window.show()

cubes_app.exec()
