# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize)
from PySide6.QtWidgets import (QHBoxLayout, QLineEdit, QMenuBar, QPushButton, QStatusBar,
                               QToolBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(987, 627)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toolBox = QToolBox(self.centralwidget)
        self.toolBox.setObjectName(u"toolBox")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 969, 504))
        self.toolBox.addItem(self.page_2, u"Page 2")

        self.verticalLayout.addWidget(self.toolBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.le_export_path = QLineEdit(self.centralwidget)
        self.le_export_path.setObjectName(u"le_export_path")

        self.horizontalLayout.addWidget(self.le_export_path)

        self.bu_select_path = QPushButton(self.centralwidget)
        self.bu_select_path.setObjectName(u"bu_select_path")
        self.bu_select_path.setMaximumSize(QSize(24, 16777215))

        self.horizontalLayout.addWidget(self.bu_select_path)

        self.bu_run = QPushButton(self.centralwidget)
        self.bu_run.setObjectName(u"bu_run")

        self.horizontalLayout.addWidget(self.bu_run)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 987, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2),
                                 QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.le_export_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"export path", None))
        self.bu_select_path.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.bu_run.setText(QCoreApplication.translate("MainWindow", u"Run", None))
    # retranslateUi

