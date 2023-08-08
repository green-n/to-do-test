import sys
import os

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QTextEdit, QCheckBox, \
    QPushButton, QHBoxLayout
from shiboken6 import delete

from src.py.to_do_list import Ui_MainWindow

import uuid


# from src.py.testtest import Ui_MainWindow


class uiDesignWrapper(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create an instance of the UI class
        self.ui = Ui_MainWindow()  # Use the correct class name
        self.ui.setupUi(self)

        # Connect your own custom signals and slots here if needed
        self.ui.pushButton.clicked.connect(self.on_button_add_new_task_clicked)
        self.container = self.ui.kastul
        # self.container.setStyleSheet("background: blue")

        # self.container.setLayout()
        # self.container_layout = QVBoxLayout(self.container)

    def on_button_add_new_task_clicked(self):

        id = str(uuid.uuid4())
        temp_task_text = self.ui.textEdit.toPlainText()
        if temp_task_text == "":
            return 0
        new_text_field = QTextEdit(self.container)
        new_text_field.setObjectName("textField" + id)
        new_text_field.setReadOnly(True)
        new_text_field.setText(temp_task_text)
        new_text_field.setMaximumSize(QSize(150, 50))
        new_text_field.setMinimumSize(QSize(100, 50))
        verticalLayout = QVBoxLayout(self.container)


        checkBoxButton = QCheckBox(self.container)
        checkBoxButton.setText("task complite")
        checkBoxButton.setObjectName("checkTaskComplition" + id)

        verticalLayout.addWidget(checkBoxButton)

        deleteButton = QPushButton(self.container)
        deleteButton.setText("DELETE")
        deleteButton.setObjectName("deleteTack" + id)
        deleteButton.setMaximumSize(QSize(50, 20))
        deleteButton.setMinimumSize(QSize(50, 20))
        deleteButton.clicked.connect(lambda: self.delete_child_by_id(id))

        verticalLayout.addWidget(deleteButton)

        task_widget = QWidget(self.container)

        horisontalLayout = QHBoxLayout(task_widget)
        horisontalLayout.addWidget(new_text_field)
        horisontalLayout.addLayout(verticalLayout)
        task_widget.setObjectName("final container" + id)
        checkBoxButton.stateChanged.connect(lambda: self.confirm_task_complition(new_text_field,checkBoxButton,horisontalLayout))

        if self.ui.urgent_check.checkState() == Qt.Checked:
            task_widget.setStyleSheet("background-color: rgba(170,50,0,0.1);")

        if self.ui.important_check.checkState() == Qt.Checked:
            task_widget.setStyleSheet("background-color: rgba(255,0,0,0.1);")


        self.container.layout().addWidget(task_widget)
        # print(self.container.layout().children())

        self.ui.textEdit.setText("")
        self.ui.urgent_check.setChecked(False)
        self.ui.important_check.setChecked(False)

    def delete_child_by_id(self, id):
        # print(id)
        # obj_for_deletion: QHBoxLayout = self.container.layout().findChild(QHBoxLayout, "final container" + str(id))

        all_children = []
        # all_children.append(obj_for_deletion)

        for child in self.container.children():
            if isinstance(child, QWidget) and id in child.objectName():
                print(child)
                all_children.append(child)
            if isinstance(child, QHBoxLayout) and id in child.objectName():
                # print(child)
                all_children.append(child)
            if isinstance(child, QVBoxLayout) and id in child.objectName():
                # print(child)
                all_children.append(child)

        for child in self.container.layout().children():
            if isinstance(child, QWidget) and id in child.objectName():
                # print(child)
                all_children.append(child)
            if isinstance(child, QHBoxLayout) and id in child.objectName():
                # print(child)
                all_children.append(child)
            if isinstance(child, QVBoxLayout) and id in child.objectName():
                # print(child)
                all_children.append(child)

        print(all_children)

        for item in all_children:
            item.deleteLater()

    def confirm_task_complition(self,textfield,checker,container):
        state = checker.checkState()
        font = textfield.font()
        font.setStrikeOut(state == Qt.Checked)
        textfield.setFont(font)

        if state == Qt.Checked:
            textfield.setStyleSheet("background: rgba(0,255,0,0.1)")
