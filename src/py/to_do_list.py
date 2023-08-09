# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'to_do_list.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QHBoxLayout,
    QMainWindow, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(345, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(40, 400, 251, 71))
        self.testContainer = QScrollArea(self.centralwidget)
        self.testContainer.setObjectName(u"testContainer")
        self.testContainer.setGeometry(QRect(30, 30, 281, 341))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testContainer.sizePolicy().hasHeightForWidth())
        self.testContainer.setSizePolicy(sizePolicy)
        font = QFont()
        font.setItalic(True)
        self.testContainer.setFont(font)
        self.testContainer.setAcceptDrops(True)
#if QT_CONFIG(whatsthis)
        self.testContainer.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.testContainer.setLayoutDirection(Qt.LeftToRight)
        self.testContainer.setAutoFillBackground(False)
        self.testContainer.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.testContainer.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.testContainer.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.testContainer.setWidgetResizable(True)
        self.testContainer.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 262, 339))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.kastul = QWidget(self.scrollAreaWidgetContents)
        self.kastul.setObjectName(u"kastul")
        sizePolicy.setHeightForWidth(self.kastul.sizePolicy().hasHeightForWidth())
        self.kastul.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.kastul)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.kastul)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.testContainer.setWidget(self.scrollAreaWidgetContents)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(90, 490, 161, 52))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.pushButton)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.important_check = QCheckBox(self.widget)
        self.important_check.setObjectName(u"important_check")

        self.verticalLayout_3.addWidget(self.important_check)

        self.urgent_check = QCheckBox(self.widget)
        self.urgent_check.setObjectName(u"urgent_check")

        self.verticalLayout_3.addWidget(self.urgent_check)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 345, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"add task", None))
        self.important_check.setText(QCoreApplication.translate("MainWindow", u"important", None))
        self.urgent_check.setText(QCoreApplication.translate("MainWindow", u"urgent", None))
    # retranslateUi

