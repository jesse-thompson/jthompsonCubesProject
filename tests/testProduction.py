import DisplayWufooWindow
from PySide6 import QtCore


def test_entry_selected(qtbot):  # using qubot requires the pytest-qt plugin (I added it to requirements.txt)
    """this test was built using
    https://stackoverflow.com/questions/58136462/selecting-qlistwidgetitem-with-qtbot-mouseclick
    and
    https://pytest-qt.readthedocs.io/en/latest/tutorial.html"""
    window = DisplayWufooWindow.WuFooEntriesWindow()
    window.show()
    qtbot.addWidget(window)
    row = 9  # assume 0 start, get 10th item change to update test
    target_item = window.list_control.item(row)
    rectangle = window.list_control.visualItemRect(target_item)
    click_point = rectangle.center()
    qtbot.mouseClick(window.list_control.viewport(), QtCore.Qt.LeftButton, pos=click_point)
    assert window.prefix_box.text() == "Mrs."
    assert window.title_box.text() == "Ate"
    assert window.project_check.isChecked() is True
    assert window.visit_check.isChecked() is False