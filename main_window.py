from PyQt5 import QtCore, QtGui, QtWidgets
from config import *
from styles import *


class MainWindowUI(object):
    def __init__(self):
        self.central_widget: None | QtWidgets.QWidget = None
        self.version_info: None | QtWidgets.QLabel = None
        self.btn_decrypt: None | QtWidgets.QPushButton = None
        self.btn_encrypt: None | QtWidgets.QPushButton = None

    def setup(self, main_window: QtWidgets.QWidget):
        main_window.setWindowIcon(QtGui.QIcon('resources/logo.ico'))
        main_window.setObjectName("MainWindow")
        main_window.setFixedSize(479, 183)
        main_window.setStyleSheet(MAIN_WINDOW_STYLE)

        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("centralwidget")

        self.version_info = QtWidgets.QLabel(self.central_widget)
        self.version_info.setGeometry(QtCore.QRect(10, 10, 231, 21))
        self.version_info.setStyleSheet(TEXT_STYLE)
        self.version_info.setObjectName("version_info")

        self.btn_decrypt = QtWidgets.QPushButton(self.central_widget)
        self.btn_decrypt.setGeometry(QtCore.QRect(10, 110, 461, 61))
        self.btn_decrypt.setStyleSheet(TEXT_STYLE)
        self.btn_decrypt.setObjectName("btn_decrypt")
        self.btn_decrypt.clicked.connect(self.decrypt)

        self.btn_encrypt = QtWidgets.QPushButton(self.central_widget)
        self.btn_encrypt.setGeometry(QtCore.QRect(10, 40, 461, 61))
        self.btn_encrypt.setStyleSheet(TEXT_STYLE)
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.btn_encrypt.clicked.connect(self.encrypt)

        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def encrypt(self):
        print("encrypt")

    def decrypt(self):
        print("decrypt")

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", f"Safe V{VERSION}"))
        self.version_info.setText(_translate("MainWindow", f"Safe V{VERSION} by crazyproger1"))
        self.btn_decrypt.setText(_translate("MainWindow", "Decrypt"))
        self.btn_encrypt.setText(_translate("MainWindow", "Encrypt"))
