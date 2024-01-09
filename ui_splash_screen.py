# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenFCSBaa.ui'
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

class Ui_Splash_Screen(object):
    def setupUi(self, Splash_Screen):
        if Splash_Screen.objectName():
            Splash_Screen.setObjectName(u"Splash_Screen")
        Splash_Screen.resize(680, 400)
        font = QFont()
        font.setFamily(u"Segoe UI")
        Splash_Screen.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icon/cgv_icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Splash_Screen.setWindowIcon(icon)
        self.centralwidget = QWidget(Splash_Screen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
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
        self.label_title.setGeometry(QRect(0, 90, 661, 71))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(40)
        self.label_title.setFont(font1)
        self.label_title.setStyleSheet(u"color: rgb(255, 170, 255);")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.dropShadowFrame)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(0, 150, 661, 31))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(14)
        font2.setItalic(True)
        self.label_description.setFont(font2)
        self.label_description.setStyleSheet(u"color: rgb(99, 105, 182);")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(70, 280, 531, 31))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	\n"
"	background-color: rgb(87, 105, 182);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.511, x2:1, y2:0.511, stop:0 rgba(255, 170, 255, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}")
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.label_loading = QLabel(self.dropShadowFrame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(0, 320, 661, 31))
        self.label_loading.setFont(font2)
        self.label_loading.setStyleSheet(u"color: rgb(99, 105, 182);")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label_credits = QLabel(self.dropShadowFrame)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(60, 350, 591, 21))
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(99, 105, 182);")
        self.label_credits.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        Splash_Screen.setCentralWidget(self.centralwidget)

        self.retranslateUi(Splash_Screen)

        QMetaObject.connectSlotsByName(Splash_Screen)
    # setupUi

    def retranslateUi(self, Splash_Screen):
        Splash_Screen.setWindowTitle(QCoreApplication.translate("Splash_Screen", u"CGV ATS", None))
        self.label_title.setText(QCoreApplication.translate("Splash_Screen", u"<html><head/><body><p><span style=\" font-weight:600;\">CGV ATS</span></p></body></html>", None))
        self.label_description.setText(QCoreApplication.translate("Splash_Screen", u"<html><head/><body><p><span style=\" font-weight:600;\">cgv auto ticketing service</span></p></body></html>", None))
        self.label_loading.setText(QCoreApplication.translate("Splash_Screen", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:normal;\">loading...</span></p></body></html>", None))
        self.label_credits.setText(QCoreApplication.translate("Splash_Screen", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:normal;\">Created By BALERION</span></p></body></html>", None))
    # retranslateUi

