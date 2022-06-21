from PyQt5 import QtCore, QtGui, QtWidgets
from styles import *
from config import *
from encrypt import encrypt_files
from decrypt import *
import threading
import PyQt5.QtCore as QtCore


class DecryptDialogUI(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.btn_select_pwd_file: None | QtWidgets.QPushButton = None
        self.btn_select_encrypted_file: None | QtWidgets.QPushButton = None
        self.edit_password1: None | QtWidgets.QLineEdit = None
        self.txt_password1: None | QtWidgets.QLabel = None
        self.btn_decrypt: None | QtWidgets.QPushButton = None
        self.btn_select_extraction_dir: None | QtWidgets.QPushButton = None
        self.decryption_thread: None | QtCore.QThread = None
        self.decryption_worker: None | DecryptionWorker = None

        self.encrypted_filepath = ""
        self.password2 = b""
        self.extraction_dir = ""

        self.setup()

    def setup(self):
        self.setObjectName("decrypt_dialog")
        self.resize(481, 240)
        self.setStyleSheet(DECRYPT_DIALOG_STYLE)

        self.btn_select_pwd_file = QtWidgets.QPushButton(self)
        self.btn_select_pwd_file.setGeometry(QtCore.QRect(250, 10, 221, 41))
        self.btn_select_pwd_file.setStyleSheet(TEXT_STYLE)
        self.btn_select_pwd_file.setObjectName("btn_select_pwd_file")
        self.btn_select_pwd_file.clicked.connect(self.select_pwd_file)

        self.btn_select_encrypted_file = QtWidgets.QPushButton(self)
        self.btn_select_encrypted_file.setGeometry(QtCore.QRect(10, 10, 221, 41))
        self.btn_select_encrypted_file.setStyleSheet(TEXT_STYLE)
        self.btn_select_encrypted_file.setObjectName("btn_select_encrypted_file")
        self.btn_select_encrypted_file.clicked.connect(self.select_encrypted_file)

        self.edit_password1 = QtWidgets.QLineEdit(self)
        self.edit_password1.setGeometry(QtCore.QRect(10, 150, 461, 22))
        self.edit_password1.setObjectName("edit_password1")

        self.txt_password1 = QtWidgets.QLabel(self)
        self.txt_password1.setGeometry(QtCore.QRect(10, 130, 81, 16))
        self.txt_password1.setStyleSheet(TEXT_STYLE)
        self.txt_password1.setObjectName("txt_password1")

        self.btn_decrypt = QtWidgets.QPushButton(self)
        self.btn_decrypt.setGeometry(QtCore.QRect(10, 180, 461, 51))
        self.btn_decrypt.setStyleSheet(TEXT_STYLE)
        self.btn_decrypt.setObjectName("btn_decrypt")
        self.btn_decrypt.clicked.connect(self.decrypt)

        self.btn_select_extraction_dir = QtWidgets.QPushButton(self)
        self.btn_select_extraction_dir.setGeometry(QtCore.QRect(10, 70, 461, 41))
        self.btn_select_extraction_dir.setStyleSheet(TEXT_STYLE)
        self.btn_select_extraction_dir.setObjectName("btn_select_extraction_dir")
        self.btn_select_extraction_dir.clicked.connect(self.select_extraction_dir)

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def decrypt(self):
        password1 = self.edit_password1.text()
        self.decryption_thread = QtCore.QThread()
        self.decryption_worker = DecryptionWorker()

        self.decryption_worker.moveToThread(self.decryption_thread)
        self.decryption_worker.finished.connect(self.decryption_thread.quit)

        self.decryption_thread.started.connect(
            lambda: self.decryption_worker.decrypt_files(
                self.encrypted_filepath,
                password1,
                self.password2,
                self.extraction_dir)
        )

        self.decryption_thread.start()

        window = QtWidgets.QDialog()
        window.setWindowIcon(QtGui.QIcon("resources/logo.ico"))
        self.decryption_thread.finished.connect(
            lambda: QtWidgets.QMessageBox.information(window, "Safe", "Files decrypted", QtWidgets.QMessageBox.Ok)
        )

    def select_extraction_dir(self):
        self.extraction_dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Select a directory", "/")[0]

    def select_encrypted_file(self):
        self.encrypted_filepath = QtWidgets.QFileDialog.getOpenFileName(self, "Select a file", "/", filter="*.sf")[0]

    def select_pwd_file(self):
        password2_file = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Select a password file",
            "/",
            filter="*.pwd"
        )[0]

        with open(password2_file, "rb") as pwd2file:
            self.password2 = pwd2file.read()

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowIcon(QtGui.QIcon('resources/logo.ico'))
        self.setWindowTitle(_translate("decrypt_dialog", "Dialog"))
        self.btn_select_pwd_file.setText(_translate("decrypt_dialog", "Select password file"))
        self.btn_select_encrypted_file.setText(_translate("decrypt_dialog", "Select encrypted file"))
        self.setWindowTitle(_translate("decrypt_dialog", f"Safe V{VERSION} - decryption"))
        self.txt_password1.setText(_translate("decrypt_dialog", "Password 1"))
        self.btn_decrypt.setText(_translate("decrypt_dialog", "Decrypt"))
        self.btn_select_extraction_dir.setText(_translate("decrypt_dialog", "Select extraction directory"))
