# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainAtrCze.ui'
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

import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(862, 862)
        font = QFont()
        font.setFamily(u"Segoe UI")
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icon/cgv_icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame{\n"
"	\n"
"	\n"
"	background-color: rgb(48, 53, 103);\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 10px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(30, 20, 61, 20))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(40)
        self.label_title.setFont(font1)
        self.label_title.setStyleSheet(u"color: rgb(255, 170, 255);")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.quitButton = QPushButton(self.dropShadowFrame)
        self.quitButton.setObjectName(u"quitButton")
        self.quitButton.setGeometry(QRect(810, 10, 21, 21))
        self.quitButton.setStyleSheet(u"background-color: rgb(48, 53, 103);")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons8-close-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.quitButton.setIcon(icon1)
        self.quitButton.setIconSize(QSize(24, 24))
        self.quitButton.setFlat(True)
        self.frame = QFrame(self.dropShadowFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 40, 341, 361))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lineEdit_id = QLineEdit(self.frame)
        self.lineEdit_id.setObjectName(u"lineEdit_id")
        self.lineEdit_id.setGeometry(QRect(90, 30, 240, 30))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Semibold")
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.lineEdit_id.setFont(font2)
        self.lineEdit_id.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(88, 98, 188);\n"
"	border-radius: 10px;\n"
"	color: #FFF;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color: rgb(52, 57, 111);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(62, 68, 132);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(72, 144, 216);\n"
"	background-color: rgb(64, 72, 139);\n"
"}")
        self.lineEdit_id.setFrame(False)
        self.lineEdit_id.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_id.setPlaceholderText(u"ID")
        self.lineEdit_id.setClearButtonEnabled(False)
        self.lineEdit_pw = QLineEdit(self.frame)
        self.lineEdit_pw.setObjectName(u"lineEdit_pw")
        self.lineEdit_pw.setGeometry(QRect(90, 80, 240, 30))
        self.lineEdit_pw.setFont(font2)
        self.lineEdit_pw.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(88, 98, 188);\n"
"	border-radius: 10px;\n"
"	color: #FFF;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color: rgb(52, 57, 111);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(62, 68, 132);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(72, 144, 216);\n"
"	background-color: rgb(64, 72, 139);\n"
"}")
        self.lineEdit_pw.setFrame(False)
        self.lineEdit_pw.setEchoMode(QLineEdit.Password)
        self.lineEdit_pw.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_pw.setPlaceholderText(u"PASSWORD")
        self.lineEdit_pw.setClearButtonEnabled(False)
        self.lineEdit_name = QLineEdit(self.frame)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setGeometry(QRect(90, 130, 240, 30))
        font3 = QFont()
        font3.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(75)
        self.lineEdit_name.setFont(font3)
        self.lineEdit_name.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(88, 98, 188);\n"
"	border-radius: 10px;\n"
"	color: #FFF;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color: rgb(52, 57, 111);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(62, 68, 132);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(72, 144, 216);\n"
"	background-color: rgb(64, 72, 139);\n"
"}")
        self.lineEdit_name.setFrame(False)
        self.lineEdit_name.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_name.setPlaceholderText(u"\uc601\ud654\uc81c\ubaa9")
        self.lineEdit_name.setClearButtonEnabled(False)
        self.lineEdit_mode = QLineEdit(self.frame)
        self.lineEdit_mode.setObjectName(u"lineEdit_mode")
        self.lineEdit_mode.setGeometry(QRect(90, 180, 240, 30))
        self.lineEdit_mode.setFont(font3)
        self.lineEdit_mode.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(88, 98, 188);\n"
"	border-radius: 10px;\n"
"	color: #FFF;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color: rgb(52, 57, 111);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(62, 68, 132);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(72, 144, 216);\n"
"	background-color: rgb(64, 72, 139);\n"
"}")
        self.lineEdit_mode.setFrame(False)
        self.lineEdit_mode.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_mode.setPlaceholderText(u"\uc601\ud654\ubaa8\ub4dc(\uc804\uccb4, \ubb34\ub300\uc778\uc0ac \ub4f1)")
        self.lineEdit_mode.setClearButtonEnabled(False)
        self.lineEdit_city = QLineEdit(self.frame)
        self.lineEdit_city.setObjectName(u"lineEdit_city")
        self.lineEdit_city.setGeometry(QRect(90, 230, 240, 30))
        self.lineEdit_city.setFont(font3)
        self.lineEdit_city.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(88, 98, 188);\n"
"	border-radius: 10px;\n"
"	color: #FFF;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color: rgb(52, 57, 111);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(62, 68, 132);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(72, 144, 216);\n"
"	background-color: rgb(64, 72, 139);\n"
"}")
        self.lineEdit_city.setFrame(False)
        self.lineEdit_city.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_city.setPlaceholderText(u"\ub3c4\uc2dc")
        self.lineEdit_city.setClearButtonEnabled(False)
        self.lineEdit_hall = QLineEdit(self.frame)
        self.lineEdit_hall.setObjectName(u"lineEdit_hall")
        self.lineEdit_hall.setGeometry(QRect(90, 280, 240, 30))
        self.lineEdit_hall.setFont(font3)
        self.lineEdit_hall.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(88, 98, 188);\n"
"	border-radius: 10px;\n"
"	color: #FFF;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color: rgb(52, 57, 111);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(62, 68, 132);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(72, 144, 216);\n"
"	background-color: rgb(64, 72, 139);\n"
"}")
        self.lineEdit_hall.setFrame(False)
        self.lineEdit_hall.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_hall.setPlaceholderText(u"\uc0c1\uc601\uad00(\uac15\ub0a8, \ucc9c\ud638 \ub4f1)")
        self.lineEdit_hall.setClearButtonEnabled(False)
        self.lineEdit_date = QLineEdit(self.frame)
        self.lineEdit_date.setObjectName(u"lineEdit_date")
        self.lineEdit_date.setGeometry(QRect(90, 330, 110, 30))
        font4 = QFont()
        font4.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font4.setPointSize(8)
        font4.setBold(True)
        font4.setWeight(75)
        self.lineEdit_date.setFont(font4)
        self.lineEdit_date.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(88, 98, 188);\n"
"	border-radius: 10px;\n"
"	color: #FFF;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color: rgb(52, 57, 111);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(62, 68, 132);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(72, 144, 216);\n"
"	background-color: rgb(64, 72, 139);\n"
"}")
        self.lineEdit_date.setFrame(False)
        self.lineEdit_date.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_date.setPlaceholderText(u"\ub0a0\uc9dc(20XX0X0X)")
        self.lineEdit_date.setClearButtonEnabled(False)
        self.lineEdit_clock = QLineEdit(self.frame)
        self.lineEdit_clock.setObjectName(u"lineEdit_clock")
        self.lineEdit_clock.setGeometry(QRect(220, 330, 110, 30))
        self.lineEdit_clock.setFont(font4)
        self.lineEdit_clock.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(88, 98, 188);\n"
"	border-radius: 10px;\n"
"	color: #FFF;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color: rgb(52, 57, 111);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(62, 68, 132);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(72, 144, 216);\n"
"	background-color: rgb(64, 72, 139);\n"
"}")
        self.lineEdit_clock.setFrame(False)
        self.lineEdit_clock.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_clock.setPlaceholderText(u"\uc2dc\uac04(2145)")
        self.lineEdit_clock.setClearButtonEnabled(False)
        self.okButton = QPushButton(self.dropShadowFrame)
        self.okButton.setObjectName(u"okButton")
        self.okButton.setGeometry(QRect(110, 430, 241, 41))
        self.okButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 170, 255);\n"
"	font: 63 15pt \"Segoe UI Semibold\";\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 3px solid rgb(204, 136, 204);\n"
"}")
        self.okButton.setFlat(False)
        self.frame_2 = QFrame(self.dropShadowFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(80, 480, 291, 271))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.lineEdit_person = QLineEdit(self.frame_2)
        self.lineEdit_person.setObjectName(u"lineEdit_person")
        self.lineEdit_person.setGeometry(QRect(30, 70, 240, 30))
        self.lineEdit_person.setFont(font3)
        self.lineEdit_person.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(88, 98, 188);\n"
"	border-radius: 10px;\n"
"	color: #FFF;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color: rgb(52, 57, 111);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(62, 68, 132);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(72, 144, 216);\n"
"	background-color: rgb(64, 72, 139);\n"
"}")
        self.lineEdit_person.setFrame(False)
        self.lineEdit_person.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_person.setPlaceholderText(u"\uc778\uc6d0(\uba85)")
        self.lineEdit_person.setClearButtonEnabled(False)
        self.lineEdit_row = QLineEdit(self.frame_2)
        self.lineEdit_row.setObjectName(u"lineEdit_row")
        self.lineEdit_row.setGeometry(QRect(30, 120, 240, 30))
        self.lineEdit_row.setFont(font3)
        self.lineEdit_row.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(88, 98, 188);\n"
"	border-radius: 10px;\n"
"	color: #FFF;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color: rgb(52, 57, 111);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(62, 68, 132);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(72, 144, 216);\n"
"	background-color: rgb(64, 72, 139);\n"
"}")
        self.lineEdit_row.setFrame(False)
        self.lineEdit_row.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_row.setPlaceholderText(u"\uc5f4(\uc54c\ud30c\ubcb3 \ub300\ubb38\uc790)")
        self.lineEdit_row.setClearButtonEnabled(False)
        self.lineEdit_seat_1 = QLineEdit(self.frame_2)
        self.lineEdit_seat_1.setObjectName(u"lineEdit_seat_1")
        self.lineEdit_seat_1.setGeometry(QRect(30, 170, 240, 30))
        self.lineEdit_seat_1.setFont(font3)
        self.lineEdit_seat_1.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(88, 98, 188);\n"
"	border-radius: 10px;\n"
"	color: #FFF;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color: rgb(52, 57, 111);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(62, 68, 132);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(72, 144, 216);\n"
"	background-color: rgb(64, 72, 139);\n"
"}")
        self.lineEdit_seat_1.setFrame(False)
        self.lineEdit_seat_1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_seat_1.setPlaceholderText(u"\uc88c\uc11d\ubc88\ud638(\uc2dc\uc791\ubc88\ud638)")
        self.lineEdit_seat_1.setClearButtonEnabled(False)
        self.lineEdit_group = QLineEdit(self.frame_2)
        self.lineEdit_group.setObjectName(u"lineEdit_group")
        self.lineEdit_group.setGeometry(QRect(30, 20, 240, 30))
        self.lineEdit_group.setFont(font3)
        self.lineEdit_group.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(88, 98, 188);\n"
"	border-radius: 10px;\n"
"	color: #FFF;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color: rgb(52, 57, 111);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(62, 68, 132);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(72, 144, 216);\n"
"	background-color: rgb(64, 72, 139);\n"
"}")
        self.lineEdit_group.setFrame(False)
        self.lineEdit_group.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_group.setPlaceholderText(u"\uc778\uc6d0\uad6c\ubd84(\uc77c\ubc18/\uccad\uc18c\ub144)")
        self.lineEdit_group.setClearButtonEnabled(False)
        self.lineEdit_seat_2 = QLineEdit(self.frame_2)
        self.lineEdit_seat_2.setObjectName(u"lineEdit_seat_2")
        self.lineEdit_seat_2.setGeometry(QRect(30, 220, 240, 30))
        self.lineEdit_seat_2.setFont(font3)
        self.lineEdit_seat_2.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(88, 98, 188);\n"
"	border-radius: 10px;\n"
"	color: #FFF;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color: rgb(52, 57, 111);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(62, 68, 132);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(72, 144, 216);\n"
"	background-color: rgb(64, 72, 139);\n"
"}")
        self.lineEdit_seat_2.setFrame(False)
        self.lineEdit_seat_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_seat_2.setPlaceholderText(u"\uc88c\uc11d\ubc88\ud638(\ub05d\ubc88\ud638)")
        self.lineEdit_seat_2.setClearButtonEnabled(False)
        self.okButton_2 = QPushButton(self.dropShadowFrame)
        self.okButton_2.setObjectName(u"okButton_2")
        self.okButton_2.setGeometry(QRect(110, 760, 241, 41))
        self.okButton_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 170, 255);\n"
"	font: 63 15pt \"Segoe UI Semibold\";\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 3px solid rgb(204, 136, 204);\n"
"}")
        self.okButton_2.setFlat(False)
        self.textBrowser = QTextBrowser(self.dropShadowFrame)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(400, 70, 361, 551))
        self.textBrowser.setStyleSheet(u"QTextBrowser {\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"	padding-left: 5px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.okButton_3 = QPushButton(self.dropShadowFrame)
        self.okButton_3.setObjectName(u"okButton_3")
        self.okButton_3.setGeometry(QRect(400, 640, 361, 41))
        self.okButton_3.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 170, 255);\n"
"	font: 63 15pt \"Segoe UI Semibold\";\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 3px solid rgb(204, 136, 204);\n"
"}")
        self.okButton_3.setFlat(False)
        self.pauseButton = QPushButton(self.dropShadowFrame)
        self.pauseButton.setObjectName(u"pauseButton")
        self.pauseButton.setGeometry(QRect(400, 760, 171, 41))
        self.pauseButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 170, 255);\n"
"	font: 63 15pt \"Segoe UI Semibold\";\n"
"	color: rgb(255, 0, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 3px solid rgb(204, 136, 204);\n"
"}")
        self.pauseButton.setFlat(False)
        self.resumeButton = QPushButton(self.dropShadowFrame)
        self.resumeButton.setObjectName(u"resumeButton")
        self.resumeButton.setGeometry(QRect(590, 760, 171, 41))
        self.resumeButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 170, 255);\n"
"	font: 63 15pt \"Segoe UI Semibold\";\n"
"	color: rgb(85, 255, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 3px solid rgb(204, 136, 204);\n"
"}")
        self.resumeButton.setFlat(False)
        self.lineEdit_delay = QLineEdit(self.dropShadowFrame)
        self.lineEdit_delay.setObjectName(u"lineEdit_delay")
        self.lineEdit_delay.setGeometry(QRect(400, 700, 171, 30))
        self.lineEdit_delay.setFont(font3)
        self.lineEdit_delay.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(88, 98, 188);\n"
"	border-radius: 10px;\n"
"	color: #FFF;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color: rgb(52, 57, 111);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(62, 68, 132);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(72, 144, 216);\n"
"	background-color: rgb(64, 72, 139);\n"
"}")
        self.lineEdit_delay.setFrame(False)
        self.lineEdit_delay.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_delay.setPlaceholderText(u"\uc2dc\uac04(\ucd08)")
        self.lineEdit_delay.setClearButtonEnabled(False)
        self.okButton_4 = QPushButton(self.dropShadowFrame)
        self.okButton_4.setObjectName(u"okButton_4")
        self.okButton_4.setGeometry(QRect(590, 700, 171, 31))
        self.okButton_4.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 170, 255);\n"
"	font: 63 15pt \"Segoe UI Semibold\";\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 3px solid rgb(204, 136, 204);\n"
"}")
        self.okButton_4.setFlat(False)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CGV ATS", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">CGV ATS</span></p></body></html>", None))
        self.quitButton.setText("")
        self.okButton.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.okButton_2.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.okButton_3.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.pauseButton.setText(QCoreApplication.translate("MainWindow", u"PAUSE", None))
        self.resumeButton.setText(QCoreApplication.translate("MainWindow", u"RESUME", None))
        self.okButton_4.setText(QCoreApplication.translate("MainWindow", u"OK", None))
    # retranslateUi

