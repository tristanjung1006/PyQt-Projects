# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_tennisOygIxx.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import tennis_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 603)
        icon = QIcon()
        icon.addFile(u":/image/tennis_icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(50, 50))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 701, 741))
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(152, 206, 142);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(30, 30, 281, 311))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(86, 101, 200);\n"
"	border-radius: 10px;\n"
"	border: 4px solid rgb(255, 255, 255);\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.browserBox = QComboBox(self.frame_2)
        self.browserBox.addItem("")
        self.browserBox.addItem("")
        self.browserBox.addItem("")
        self.browserBox.setObjectName(u"browserBox")
        self.browserBox.setGeometry(QRect(50, 30, 185, 25))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.browserBox.setFont(font)
        self.browserBox.setStyleSheet(u"QComboBox {\n"
"	border: 1px solid rgb(88, 98, 188);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QComboBox:hover {\n"
"	border: 2px solid rgb(110, 129, 255);\n"
"}\n"
"QComboBox:focus {\n"
"	border: 2px solid rgb(72, 144, 216);\n"
"}\n"
"QListView {\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.idEdit = QLineEdit(self.frame_2)
        self.idEdit.setObjectName(u"idEdit")
        self.idEdit.setGeometry(QRect(50, 70, 185, 25))
        self.idEdit.setFont(font)
        self.idEdit.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(88, 98, 188);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(110, 129, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(72, 144, 216);\n"
"}")
        self.pwEdit = QLineEdit(self.frame_2)
        self.pwEdit.setObjectName(u"pwEdit")
        self.pwEdit.setGeometry(QRect(50, 100, 185, 25))
        self.pwEdit.setFont(font)
        self.pwEdit.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(88, 98, 188);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(110, 129, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(72, 144, 216);\n"
"}")
        self.pwEdit.setEchoMode(QLineEdit.Normal)
        self.courtBox = QComboBox(self.frame_2)
        self.courtBox.addItem("")
        self.courtBox.addItem("")
        self.courtBox.addItem("")
        self.courtBox.addItem("")
        self.courtBox.addItem("")
        self.courtBox.addItem("")
        self.courtBox.addItem("")
        self.courtBox.addItem("")
        self.courtBox.addItem("")
        self.courtBox.addItem("")
        self.courtBox.setObjectName(u"courtBox")
        self.courtBox.setGeometry(QRect(50, 140, 185, 25))
        font1 = QFont()
        font1.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font1.setPointSize(9)
        self.courtBox.setFont(font1)
        self.courtBox.setStyleSheet(u"QComboBox {\n"
"	border: 1px solid rgb(88, 98, 188);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox:hover {\n"
"	border: 2px solid rgb(110, 129, 255);\n"
"}\n"
"QComboBox:focus {\n"
"	border: 2px solid rgb(72, 144, 216);\n"
"}\n"
"QListView {\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.timeBox = QComboBox(self.frame_2)
        self.timeBox.addItem("")
        self.timeBox.addItem("")
        self.timeBox.addItem("")
        self.timeBox.addItem("")
        self.timeBox.addItem("")
        self.timeBox.addItem("")
        self.timeBox.addItem("")
        self.timeBox.addItem("")
        self.timeBox.setObjectName(u"timeBox")
        self.timeBox.setGeometry(QRect(50, 210, 185, 25))
        self.timeBox.setFont(font)
        self.timeBox.setStyleSheet(u"QComboBox {\n"
"	border: 1px solid rgb(88, 98, 188);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox:hover {\n"
"	border: 2px solid rgb(110, 129, 255);\n"
"}\n"
"QComboBox:focus {\n"
"	border: 2px solid rgb(72, 144, 216);\n"
"}\n"
"QListView {\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.infoButton = QPushButton(self.frame_2)
        self.infoButton.setObjectName(u"infoButton")
        self.infoButton.setGeometry(QRect(50, 250, 185, 31))
        font2 = QFont()
        font2.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.infoButton.setFont(font2)
        self.infoButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(249, 249, 249);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(110, 129, 255);\n"
"}")
        self.dateEdit = QLineEdit(self.frame_2)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(50, 180, 185, 25))
        font3 = QFont()
        font3.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setWeight(50)
        self.dateEdit.setFont(font3)
        self.dateEdit.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(88, 98, 188);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(110, 129, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(72, 144, 216);\n"
"}")
        self.infoBrowser = QTextBrowser(self.frame)
        self.infoBrowser.setObjectName(u"infoBrowser")
        self.infoBrowser.setGeometry(QRect(340, 30, 331, 471))
        self.infoBrowser.setStyleSheet(u"QTextBrowser {\n"
"	background-color: rgb(86, 101, 200);\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	border: 4px solid rgb(255, 255, 255);\n"
"	padding-left: 5px;\n"
"}")
        self.progressBrowser = QTextBrowser(self.frame)
        self.progressBrowser.setObjectName(u"progressBrowser")
        self.progressBrowser.setGeometry(QRect(30, 360, 281, 211))
        self.progressBrowser.setStyleSheet(u"QTextBrowser {\n"
"	background-color: rgb(86, 101, 200);\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	border: 4px solid rgb(255, 255, 255);\n"
"	padding-left: 5px;\n"
"}")
        self.chromeButton = QPushButton(self.frame)
        self.chromeButton.setObjectName(u"chromeButton")
        self.chromeButton.setGeometry(QRect(340, 540, 91, 31))
        self.chromeButton.setFont(font2)
        self.chromeButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(249, 249, 249);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(189, 255, 176);\n"
"}")
        self.firefoxButton = QPushButton(self.frame)
        self.firefoxButton.setObjectName(u"firefoxButton")
        self.firefoxButton.setGeometry(QRect(460, 540, 91, 31))
        self.firefoxButton.setFont(font2)
        self.firefoxButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(249, 249, 249);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(189, 255, 176);\n"
"}")
        self.edgeButton = QPushButton(self.frame)
        self.edgeButton.setObjectName(u"edgeButton")
        self.edgeButton.setGeometry(QRect(580, 540, 91, 31))
        self.edgeButton.setFont(font2)
        self.edgeButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(249, 249, 249);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(189, 255, 176);\n"
"}")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(490, 506, 31, 31))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(152, 206, 142);\n"
"	border-radius: 10px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/image/firefox_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(24, 24))
        self.pushButton.setFlat(True)
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(610, 506, 31, 31))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(152, 206, 142);\n"
"	border-radius: 10px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/image/edge_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(24, 24))
        self.pushButton_2.setFlat(True)
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(370, 506, 31, 31))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(152, 206, 142);\n"
"	border-radius: 10px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/image/chrome_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QSize(24, 24))
        self.pushButton_3.setFlat(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\ubd80\ucc9c\uc2dc \uacf5\uacf5\ud14c\ub2c8\uc2a4\uc7a5 \uc608\uc57d\ub9e4\ud06c\ub85c", None))
        self.browserBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Chrome", None))
        self.browserBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Firefox", None))
        self.browserBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Microsoft Edge", None))

        self.idEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.pwEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PW", None))
        self.courtBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\ub0a8\ubd80\uc218\uc790\uc6d0\ud14c\ub2c8\uc2a4\uc7a5", None))
        self.courtBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\uc885\ud569\uc6b4\ub3d9\uc7a5\ud14c\ub2c8\uc2a4\uc7a5", None))
        self.courtBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\ubd80\ucc9c\uccb4\uc721\uad00(\ud558\ub4dc)\ud14c\ub2c8\uc2a4\uc7a5", None))
        self.courtBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\uc131\uc8fc\uc0b0\uccb4\uc721\uacf5\uc6d0\ud14c\ub2c8\uc2a4\uc7a5", None))
        self.courtBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\uc6d0\ubbf8\ud14c\ub2c8\uc2a4\uc7a5", None))
        self.courtBox.setItemText(5, QCoreApplication.translate("MainWindow", u"\ubd80\ucc9c\uc2e4\ub0b4\ud14c\ub2c8\uc2a4\uc7a5", None))
        self.courtBox.setItemText(6, QCoreApplication.translate("MainWindow", u"\uc624\uc815\ub808\ud3ec\uce20\uc13c\ud130 \ud14c\ub2c8\uc2a4\uc7a5", None))
        self.courtBox.setItemText(7, QCoreApplication.translate("MainWindow", u"\uc18c\uc0ac\ubc30\uc218\uc9c0\ud14c\ub2c8\uc2a4\uc7a5", None))
        self.courtBox.setItemText(8, QCoreApplication.translate("MainWindow", u"\ubcf5\uc0ac\uace8\ud14c\ub2c8\uc2a4\uc7a5", None))
        self.courtBox.setItemText(9, QCoreApplication.translate("MainWindow", u"\ud574\uadf8\ub298\uccb4\uc721\uacf5\uc6d0 \ud14c\ub2c8\uc2a4\uc7a5", None))

        self.timeBox.setItemText(0, QCoreApplication.translate("MainWindow", u"06:00~08:00", None))
        self.timeBox.setItemText(1, QCoreApplication.translate("MainWindow", u"08:00~10:00", None))
        self.timeBox.setItemText(2, QCoreApplication.translate("MainWindow", u"10:00~12:00", None))
        self.timeBox.setItemText(3, QCoreApplication.translate("MainWindow", u"12:00~14:00", None))
        self.timeBox.setItemText(4, QCoreApplication.translate("MainWindow", u"14:00~16:00", None))
        self.timeBox.setItemText(5, QCoreApplication.translate("MainWindow", u"16:00~18:00", None))
        self.timeBox.setItemText(6, QCoreApplication.translate("MainWindow", u"18:00~20:00", None))
        self.timeBox.setItemText(7, QCoreApplication.translate("MainWindow", u"20:00~22:00", None))

        self.infoButton.setText(QCoreApplication.translate("MainWindow", u"\uc81c\ucd9c", None))
        self.dateEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\ub0a0\uc9dc(\uc608\uc2dc: 20230101)", None))
        self.chromeButton.setText(QCoreApplication.translate("MainWindow", u"\ub9e4\ud06c\ub85c \uc2dc\uc791", None))
        self.firefoxButton.setText(QCoreApplication.translate("MainWindow", u"\ub9e4\ud06c\ub85c \uc2dc\uc791", None))
        self.edgeButton.setText(QCoreApplication.translate("MainWindow", u"\ub9e4\ud06c\ub85c \uc2dc\uc791", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
    # retranslateUi

