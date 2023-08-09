import uuid

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QTextEdit, QVBoxLayout, QCheckBox, QPushButton, QWidget, QHBoxLayout, QMainWindow

from src.py.to_do_list import Ui_MainWindow


class TaskCreation(QWidget):
    def __init__(self, container):
        super().__init__()

        self.temp_id = str(uuid.uuid4())
        self.temp_task_text = ""
        self.new_text_field = QTextEdit(container)
        self.new_text_field.setObjectName("textField" + self.temp_id)
        self.new_text_field.setReadOnly(True)

        self.new_text_field.setMaximumSize(QSize(150, 50))
        self.new_text_field.setMinimumSize(QSize(100, 50))
        self.verticalLayout = QVBoxLayout(container)

        self.checkBoxButton = QCheckBox(container)
        self.checkBoxButton.setText("task complite")
        self.checkBoxButton.setObjectName("checkTaskComplition" + self.temp_id)

        self.verticalLayout.addWidget(self.checkBoxButton)

        self.deleteButton = QPushButton(container)
        self.deleteButton.setText("DELETE")
        self.deleteButton.setObjectName("deleteTack" + self.temp_id)
        self.deleteButton.setMaximumSize(QSize(50, 20))
        self.deleteButton.setMinimumSize(QSize(50, 20))
        self.deleteButton.clicked.connect(lambda: self.delete_child_by_id(self.temp_id, container))

        self.verticalLayout.addWidget(self.deleteButton)

        self.task_widget = QWidget(container)

        self.horisontalLayout = QHBoxLayout(self.task_widget)
        self.horisontalLayout.addWidget(self.new_text_field)
        self.horisontalLayout.addLayout(self.verticalLayout)
        self.task_widget.setObjectName("final container" + self.temp_id)
        self.checkBoxButton.stateChanged.connect(
            lambda: self.confirm_task_complition(self.new_text_field, self.checkBoxButton))
        #self.ui = Ui_MainWindow()  # Use the correct class name
        # self.ui.setupUi(self)
        print("dffff")

        # Connect your own custom signals and slots here if needed
        # self.ui.pushButton.clicked.connect(task_creation.create_new_task())
        #self.container = self.ui.kastul
        #print(self.container)

    def set_text(self, text):
        self.new_text_field.setText(text)
        # self.temp_task_text = text
        # print( self.temp_task_text)
        # if  self.temp_task_text == "":
        #     return 0


        # if self.ui.urgent_check.checkState() == Qt.Checked:
        #     task_widget.setStyleSheet("background-color: rgba(170,50,0,0.1);")
        #
        # if self.ui.important_check.checkState() == Qt.Checked:
        #     task_widget.setStyleSheet("background-color: rgba(255,0,0,0.1);")
        return self.task_widget

    def set_style_sheet(self, style):
        self.task_widget.setStyleSheet(style)
    def delete_child_by_id(self, id,container):
        # print(id)
        # obj_for_deletion: QHBoxLayout = self.container.layout().findChild(QHBoxLayout, "final container" + str(id))

        all_children = []
        container.layout().update()
        # all_children.append(obj_for_deletion)
        print(container.children())
        for child in container.children():
            if isinstance(child, QWidget) and id in child.objectName():

                all_children.append(child)
            if isinstance(child, QHBoxLayout) and id in child.objectName():
                # print(child)
                all_children.append(child)
            if isinstance(child, QVBoxLayout) and id in child.objectName():
                # print(child)
                all_children.append(child)

        for child in container.layout().children():
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

    def confirm_task_complition(self, textfield, checker):
        state = checker.checkState()
        font = textfield.font()
        font.setStrikeOut(state == Qt.Checked)
        textfield.setFont(font)

        if state == Qt.Checked:
            textfield.setStyleSheet("background: rgba(0,255,0,0.1)")
        else:
            textfield.setStyleSheet("background: rgba(0,255,0,0)")
