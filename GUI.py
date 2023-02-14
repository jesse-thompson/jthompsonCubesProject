# TODO: Add basic GUI functionality
# TODO: GUI shows list of entries with short versions
# TODO: GUI shows selected entry
# TODO: Ensure widgets are not editable

import PyQt5
from PyQt5.QtWidgets import QApplication, QLabel

cubes_app = QApplication([])

label = QLabel('CUBES Database')

label.show()

cubes_app.exec()
