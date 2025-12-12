# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'downloader_ver1.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.file_type = QComboBox(self.centralwidget)
        self.file_type.addItem("")
        self.file_type.addItem("")
        self.file_type.setObjectName(u"file_type")
        self.file_type.setGeometry(QRect(320, 150, 69, 22))
        self.youtube_link = QLineEdit(self.centralwidget)
        self.youtube_link.setObjectName(u"youtube_link")
        self.youtube_link.setGeometry(QRect(200, 150, 113, 20))
        self.folder_path = QLineEdit(self.centralwidget)
        self.folder_path.setObjectName(u"folder_path")
        self.folder_path.setGeometry(QRect(200, 180, 113, 20))
        self.Browse = QPushButton(self.centralwidget)
        self.Browse.setObjectName(u"Browse")
        self.Browse.setGeometry(QRect(320, 180, 75, 23))
        self.download_button = QPushButton(self.centralwidget)
        self.download_button.setObjectName(u"download_button")
        self.download_button.setGeometry(QRect(250, 310, 75, 23))
        self.Title = QTextBrowser(self.centralwidget)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(80, 70, 431, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.file_type.setItemText(0, QCoreApplication.translate("MainWindow", u"m4a", None))
        self.file_type.setItemText(1, QCoreApplication.translate("MainWindow", u"mp3", None))

        self.folder_path.setInputMask("")
        self.folder_path.setText("")
        self.Browse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.download_button.setText(QCoreApplication.translate("MainWindow", u"DownLoad", None))
        self.Title.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">YT-Music-Downloader</span></p></body></html>", None))
    # retranslateUi

