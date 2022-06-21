from PyQt5 import QtCore, QtGui, QtWidgets

from encrypt_dialog import *
from config import *
from styles import *


class MainWindowUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_widget: None | QtWidgets.QWidget = None
        self.version_info: None | QtWidgets.QLabel = None
        self.btn_decrypt: None | QtWidgets.QPushButton = None
        self.btn_encrypt: None | QtWidgets.QPushButton = None
        self.encrypt_dialog: None | EncryptDialogUI = None
        self.setup()

    def setup(self):

        self.setObjectName("main_window")
        self.setFixedSize(479, 183)
        self.setStyleSheet(MAIN_WINDOW_STYLE)

        self.central_widget = QtWidgets.QWidget(self)
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

        self.setCentralWidget(self.central_widget)
        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def encrypt(self):
        self.encrypt_dialog = EncryptDialogUI()
        self.encrypt_dialog.show()

    def decrypt(self):
        pass

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowIcon(QtGui.QIcon('resources/logo.ico'))
        self.setWindowTitle(_translate("main_window", f"Safe V{VERSION}"))
        self.version_info.setText(_translate("main_window", f"Safe V{VERSION} by crazyproger1"))
        self.btn_decrypt.setText(_translate("main_window", "Decrypt"))
        self.btn_encrypt.setText(_translate("main_window", "Encrypt"))
