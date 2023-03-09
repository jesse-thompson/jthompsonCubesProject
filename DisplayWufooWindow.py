# Code from Dr. John F. Santore's Sprint 3 Instructor Demo used as basis for Sprint 4

import sys

import requests
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QListWidget,
    QApplication,
    QListWidgetItem,
    QHBoxLayout,
    QVBoxLayout,
    QLayout,
    QGridLayout,
    QPlainTextEdit,
    QLabel,
    QLineEdit,
    QCheckBox,
    QInputDialog
)

import DatabaseStuff
from main import db_name
from serverDB import CubesDB
from DatabaseStuff import add_claims_to_db


class WuFooEntriesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.wufoo_data = self.get_cubes_data_from_db()
        self.claim_data = self.get_claim_data_from_db()
        self.list_control: QListWidget = None
        self.data_window = None
        self.prefix_box: QLineEdit = None
        self.fname_box: QLineEdit = None
        self.lname_box: QLineEdit = None
        self.title_box: QLineEdit = None
        self.org_box: QLineEdit = None
        self.email_box: QLineEdit = None
        self.website_box: QLineEdit = None
        self.project_check: QCheckBox = None
        self.speaker_check: QCheckBox = None
        self.visit_check: QCheckBox = None
        self.shadow_check: QCheckBox = None
        self.internship_check: QCheckBox = None
        self.panel_check: QCheckBox = None
        self.network_even_check: QCheckBox = None
        self.summer2022_check: QCheckBox = None
        self.fall2022_check: QCheckBox = None
        self.spring2023_check: QCheckBox = None
        self.summer2023_check: QCheckBox = None
        self.other_check: QCheckBox = None
        self.permission_granted: QLineEdit = None
        self.claimed_by: QLabel = None
        self.claim_button = QPushButton("Click to claim proposal")

        self.fname_box_claims: QInputDialog = None
        self.lname_box_claims: QInputDialog = None
        self.title_box_claims: QInputDialog = None
        self.email_box_claims: QInputDialog = None
        self.department_box: QInputDialog = None

        self.setup_window()

    def setup_window(self):
        main_layout = QHBoxLayout()
        self.list_control = QListWidget()
        left_pane = QVBoxLayout()
        main_layout.addLayout(left_pane)
        left_pane.addWidget(self.list_control)
        right_pane = self.build_right_pane()
        self.list_control.resize(400, 400)
        self.list_control.currentItemChanged.connect(self.wufoo_entry_selected)
        self.put_data_in_list(self.wufoo_data)
        quit_button = QPushButton("Quit")
        quit_button.clicked.connect(QApplication.instance().quit)
        left_pane.addWidget(quit_button)
        main_layout.addLayout(right_pane)
        bottom_pane = self.build_bottom_pane()
        main_layout.addLayout(bottom_pane)
        self.setLayout(main_layout)
        self.show()

    def build_right_pane(self) -> QLayout:
        right_pane = QVBoxLayout()
        one_liners_pane = QGridLayout()
        right_pane.addLayout(one_liners_pane)
        one_liners_pane.addWidget(QLabel("Prefix:"), 0, 0)
        self.prefix_box = QLineEdit()
        self.prefix_box.setReadOnly(True)
        one_liners_pane.addWidget(self.prefix_box, 0, 1)
        one_liners_pane.addWidget(QLabel("Name:"), 0, 2)
        self.fname_box = QLineEdit()
        self.fname_box.setReadOnly(True)
        one_liners_pane.addWidget(self.fname_box, 0, 3)
        self.lname_box = QLineEdit()
        self.lname_box.setReadOnly(True)
        one_liners_pane.addWidget(self.lname_box, 0, 4)
        one_liners_pane.addWidget(QLabel("Title:"), 0, 5)
        self.title_box = QLineEdit()
        self.title_box.setReadOnly(True)
        one_liners_pane.addWidget(self.title_box, 0, 6)
        one_liners_pane.addWidget(QLabel("Organization:"), 1, 0)
        self.org_box = QLineEdit()
        self.org_box.setReadOnly(True)
        one_liners_pane.addWidget(self.org_box, 1, 1)
        one_liners_pane.addWidget(QLabel("Email & Website:"), 1, 2)
        self.email_box = QLineEdit()
        self.email_box.setReadOnly(True)
        self.website_box = QLineEdit()
        self.website_box.setReadOnly(True)
        one_liners_pane.addWidget(self.email_box, 1, 3)
        one_liners_pane.addWidget(self.website_box, 1, 4)
        self.project_check = QCheckBox("Course Project")
        self.project_check.setAttribute(Qt.WA_TransparentForMouseEvents)  # don't accept editing
        self.project_check.setFocusPolicy(Qt.NoFocus)  # or keyboard focus
        one_liners_pane.addWidget(self.project_check, 2, 0)
        self.speaker_check = QCheckBox("Guest Speaker")
        self.speaker_check.setAttribute(Qt.WA_TransparentForMouseEvents)  # don't accept editing
        one_liners_pane.addWidget(self.speaker_check, 2, 1)
        self.visit_check = QCheckBox("Site Visit")
        self.visit_check.setAttribute(Qt.WA_TransparentForMouseEvents)  # don't accept editing
        one_liners_pane.addWidget(self.visit_check, 2, 5)
        self.shadow_check = QCheckBox("Job Shadow")
        self.shadow_check.setAttribute(Qt.WA_TransparentForMouseEvents)  # don't accept editing
        one_liners_pane.addWidget(self.shadow_check, 2, 3)
        self.internship_check = QCheckBox("Internship")
        self.internship_check.setAttribute(Qt.WA_TransparentForMouseEvents)  # don't accept editing
        one_liners_pane.addWidget(self.internship_check, 2, 4)
        self.panel_check = QCheckBox("Career Panel")
        self.panel_check.setAttribute(Qt.WA_TransparentForMouseEvents)  # don't accept editing
        one_liners_pane.addWidget(self.panel_check, 2, 2)
        self.network_even_check = QCheckBox("Networking Event")
        self.network_even_check.setAttribute(Qt.WA_TransparentForMouseEvents)  # don't accept editing
        one_liners_pane.addWidget(self.network_even_check, 2, 6)
        self.summer2022_check = QCheckBox("Summer 2022")
        self.summer2022_check.setAttribute(Qt.WA_TransparentForMouseEvents)
        one_liners_pane.addWidget(self.summer2022_check, 3, 0)
        self.fall2022_check = QCheckBox("Fall 2022")
        self.fall2022_check.setAttribute(Qt.WA_TransparentForMouseEvents)
        one_liners_pane.addWidget(self.fall2022_check, 3, 1)
        self.spring2023_check = QCheckBox("Spring 2023")
        self.spring2023_check.setAttribute(Qt.WA_TransparentForMouseEvents)
        one_liners_pane.addWidget(self.spring2023_check, 3, 2)
        self.summer2023_check = QCheckBox("Summer 2023")
        self.summer2023_check.setAttribute(Qt.WA_TransparentForMouseEvents)
        one_liners_pane.addWidget(self.summer2023_check, 3, 3)
        self.other_check = QCheckBox("Other")
        self.other_check.setAttribute(Qt.WA_TransparentForMouseEvents)
        one_liners_pane.addWidget(self.other_check, 3, 4)
        one_liners_pane.addWidget(QLabel("Permission Granted?"), 4, 0)
        self.permission_granted = QLineEdit()
        self.permission_granted.setReadOnly(True)
        one_liners_pane.addWidget(self.permission_granted, 4, 1)

        return right_pane

    def build_bottom_pane(self) -> QLayout:  # not actually on the bottom, at least not yet
        bottom_pane = QVBoxLayout()
        b_pane_layout = QGridLayout()
        bottom_pane.addLayout(b_pane_layout)
        b_pane_layout.addWidget(QLabel("Claimed By"), 0, 1)
        b_pane_layout.addWidget(self.claim_button, 0, 2)
        # self.claim_button.clicked.connect(DatabaseStuff.add_claims_to_db("email", self.email_box_claims.text()))
        b_pane_layout.addWidget(QLabel("Name:"), 1, 0)
        self.fname_box_claims = QLineEdit()
        b_pane_layout.addWidget(self.fname_box_claims, 1, 1)
        self.lname_box_claims = QLineEdit()
        b_pane_layout.addWidget(self.lname_box_claims, 1, 2)
        b_pane_layout.addWidget(QLabel("Title:"), 2, 0)
        self.title_box_claims = QLineEdit()
        b_pane_layout.addWidget(self.title_box_claims, 2, 1)
        b_pane_layout.addWidget(QLabel("Email:"), 3, 0)
        self.email_box_claims = QLineEdit()
        b_pane_layout.addWidget(self.email_box_claims, 3, 1)
        b_pane_layout.addWidget(QLabel("Department:"), 4, 0)
        self.department_box = QLineEdit()
        b_pane_layout.addWidget(self.department_box, 4, 1)

        return bottom_pane

    def get_cubes_data_from_db(self) -> list:
        with CubesDB(db_name) as cursor:
            cursor.execute("""SELECT * FROM WuFooData""")
            return cursor.fetchall()

    def get_claim_data_from_db(self) -> list:
        with CubesDB(db_name) as cursor:
            cursor.execute("""SELECT * FROM Claims""")
            return cursor.fetchall()

    def put_data_in_list(self, data_to_add):
        for item in data_to_add:
            display_text = f"{item['first_name']}  {item['last_name']} : {item['org']}"
            list_item = QListWidgetItem(display_text, listview=self.list_control)
            list_item.setData(1, item)  # let's put the dictionary for later use

    def wufoo_entry_selected(self, current: QListWidgetItem, previous: QListWidgetItem):
        selected_data = current.data(1)  # we put the full record in data role 1
        self.prefix_box.setText(selected_data["prefix"])
        self.fname_box.setText(selected_data["first_name"])
        self.lname_box.setText(selected_data["last_name"])
        self.title_box.setText(selected_data["title"])
        self.org_box.setText(selected_data["org"])
        self.email_box.setText(selected_data["email"])
        self.website_box.setText(selected_data["website"])
        self.project_check.setChecked(not not selected_data["course_project"])
        self.speaker_check.setChecked(not not selected_data["guest_speaker"])
        self.visit_check.setChecked(not not selected_data["site_visit"])
        self.shadow_check.setChecked(not not selected_data["job_shadow"])
        self.internship_check.setChecked(not not selected_data["internship"])
        self.panel_check.setChecked(not not selected_data["career_panel"])
        self.network_even_check.setChecked(not not selected_data["networking_event"])
        self.summer2022_check.setChecked(not not selected_data["summer2022"])
        self.fall2022_check.setChecked(not not selected_data["fall2022"])
        self.spring2023_check.setChecked(not not selected_data["spring2023"])
        self.summer2023_check.setChecked(not not selected_data["summer2023"])
        self.other_check.setChecked(not not selected_data["other"])
        self.permission_granted.setText(selected_data["permission_granted"])

    def claim_data_selected(self, current: QListWidgetItem, previous: QListWidgetItem):
        selected_data = current.data(2)
        self.claimed_by.setText(selected_data["claimed_by"])

    # def get_text(self):
    #     self.
