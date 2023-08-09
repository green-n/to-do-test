import sys
import os

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QTextEdit, QCheckBox, \
    QPushButton, QHBoxLayout
from shiboken6 import delete

from src.Classes.task_creation import TaskCreation
from src.py.to_do_list import Ui_MainWindow

import uuid


# from src.py.testtest import Ui_MainWindow


class uiDesignWrapper(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.container = self.kastul
        self.task_creation_instance = TaskCreation()
        self.pushButton.clicked.connect(self.call_task_creation)

    def call_task_creation(self):

        temp_task_text = self.textEdit.toPlainText()
        #self.task_creation_instance.set_text(temp_task_text)
        #task = self.task_creation_instance.create_new_task(temp_task_text,container)
        self.container.layout().addWidget(  self.task_creation_instance.new_task(temp_task_text,self.container) )
        #container.layout().update()
        print(self.container.children())
        self.textEdit.setText("")
        self.urgent_check.setChecked(False)
        self.important_check.setChecked(False)
