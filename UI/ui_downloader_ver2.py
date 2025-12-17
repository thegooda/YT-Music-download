# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'downloader_ver2.ui'
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
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QStatusBar, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(612, 458)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.file_type = QComboBox(self.centralwidget)
        self.file_type.addItem("")
        self.file_type.addItem("")
        self.file_type.setObjectName(u"file_type")
        self.file_type.setGeometry(QRect(350, 140, 71, 22))
        self.youtube_link = QLineEdit(self.centralwidget)
        self.youtube_link.setObjectName(u"youtube_link")
        self.youtube_link.setGeometry(QRect(212, 140, 131, 20))
        self.folder_path = QLineEdit(self.centralwidget)
        self.folder_path.setObjectName(u"folder_path")
        self.folder_path.setGeometry(QRect(212, 170, 131, 20))
        self.Browse = QPushButton(self.centralwidget)
        self.Browse.setObjectName(u"Browse")
        self.Browse.setGeometry(QRect(350, 170, 71, 23))
        self.download_button = QPushButton(self.centralwidget)
        self.download_button.setObjectName(u"download_button")
        self.download_button.setGeometry(QRect(260, 330, 101, 41))
        self.Title = QTextBrowser(self.centralwidget)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(90, 40, 431, 41))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(180, 290, 271, 23))
        self.progressBar.setValue(0)
        self.status_label = QTextBrowser(self.centralwidget)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setGeometry(QRect(230, 260, 151, 21))
        self.Title_folder = QTextBrowser(self.centralwidget)
        self.Title_folder.setObjectName(u"Title_folder")
        self.Title_folder.setGeometry(QRect(160, 170, 51, 21))
        self.Title_link = QTextBrowser(self.centralwidget)
        self.Title_link.setObjectName(u"Title_link")
        self.Title_link.setGeometry(QRect(160, 140, 51, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 612, 21))
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
        self.status_label.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600;\">Status:</span></p></body></html>", None))
        self.Title_folder.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600;\">Folder:</span></p></body></html>", None))
        self.Title_link.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600;\">Link:</span></p></body></html>", None))
    # retranslateUi

