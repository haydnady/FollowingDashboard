# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 514)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelInsta = QLabel(self.centralwidget)
        self.labelInsta.setObjectName(u"labelInsta")
        self.labelInsta.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.labelInsta, 1, 1, 1, 1)

        self.lcdTwitter = QLCDNumber(self.centralwidget)
        self.lcdTwitter.setObjectName(u"lcdTwitter")
        self.lcdTwitter.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.lcdTwitter, 2, 0, 1, 1)

        self.labelTwitter = QLabel(self.centralwidget)
        self.labelTwitter.setObjectName(u"labelTwitter")
        self.labelTwitter.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.labelTwitter, 2, 1, 1, 1)

        self.lcdInsta = QLCDNumber(self.centralwidget)
        self.lcdInsta.setObjectName(u"lcdInsta")
        self.lcdInsta.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.lcdInsta, 1, 0, 1, 1)

        self.lcdYoutube = QLCDNumber(self.centralwidget)
        self.lcdYoutube.setObjectName(u"lcdYoutube")
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        self.lcdYoutube.setFont(font)
        self.lcdYoutube.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.lcdYoutube, 0, 0, 1, 1)

        self.labelYoutube = QLabel(self.centralwidget)
        self.labelYoutube.setObjectName(u"labelYoutube")
        self.labelYoutube.setAutoFillBackground(False)
        self.labelYoutube.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.labelYoutube, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 5)
        self.gridLayout.setColumnStretch(1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Followind Dashboard", None))
        self.labelInsta.setText(QCoreApplication.translate("MainWindow", u"Insta", None))
        self.labelTwitter.setText(QCoreApplication.translate("MainWindow", u"Twitter", None))
        self.labelYoutube.setText(QCoreApplication.translate("MainWindow", u"YouTube", None))
    # retranslateUi