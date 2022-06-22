from PyQt5 import QtCore, QtGui, QtWidgets
from styles import *
from config import *
from decryption_worker import *
from text import *


class DecryptionDialogUI(QtWidgets.QDialog):
    def __init__(self, filepath: str | None = "/"):
        super().__init__()
        self.btn_select_pwd_file: None | QtWidgets.QPushButton = None
        self.btn_select_encrypted_file: None | QtWidgets.QPushButton = None
        self.edit_password1: None | QtWidgets.QLineEdit = None
        self.txt_password1: None | QtWidgets.QLabel = None
        self.btn_decrypt: None | QtWidgets.QPushButton = None
        self.btn_select_extraction_dir: None | QtWidgets.QPushButton = None
        self.decryption_thread: None | QtCore.QThread = None
        self.decryption_worker: None | DecryptionWorker = None

        self.encrypted_filepath = filepath
        self.password2 = b""
        self.extraction_dir = "/"

        self.worker_status = 0

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

    def check_values(self):
        password1 = self.edit_password1.text()

        if self.encrypted_filepath == "/" or not self.encrypted_filepath:
            show_critical("Specify the path to the encrypted file")
            return

        elif not self.password2:
            show_critical("Specify the path to the password file")
            return

        elif self.extraction_dir == "/" or not self.extraction_dir:
            show_critical("Specify the path to the extraction dir")
            return

        elif not password1:
            show_critical("Enter the first password")
            return

        return True

    def decrypt(self):
        if not self.check_values():
            return

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

        self.decryption_worker.status.connect(self.set_worker_status)

        self.decryption_thread.start()

        window = QtWidgets.QDialog()
        window.setWindowIcon(QtGui.QIcon("resources/logo.ico"))
        self.decryption_thread.finished.connect(
            self.handle_decryption_finish
        )

    def handle_decryption_finish(self):
        if self.worker_status == 0:
            self.reject()
            self.decryption_thread.quit()
            show_info("Files decrypted")

    def set_worker_status(self, status: int):
        self.worker_status = status

        if status == 1:
            show_critical("Some password is wrong")

        if self.worker_status != 0:
            self.decryption_thread.quit()

    def select_extraction_dir(self):
        self.extraction_dir = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            "Select a directory",
            self.extraction_dir
        )

        if self.extraction_dir:
            self.btn_select_extraction_dir.setText(reduce_text(self.extraction_dir))

    def select_encrypted_file(self):
        self.encrypted_filepath = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Select a file",
            self.encrypted_filepath,
            filter="*.sf")[0]

        if self.encrypted_filepath:
            self.btn_select_encrypted_file.setText(reduce_text(self.encrypted_filepath))

    def select_pwd_file(self):
        password2_file = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Select a password file",
            "/",
            filter="*.pwd"
        )[0]

        if not password2_file:
            return

        with open(password2_file, "rb") as pwd2file:
            self.password2 = pwd2file.read()

        if self.password2:
            self.btn_select_pwd_file.setText(reduce_text(self.password2.decode()))

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowIcon(QtGui.QIcon('resources/logo.ico'))
        self.setWindowTitle(_translate("decrypt_dialog", "Dialog"))
        self.btn_select_pwd_file.setText(_translate("decrypt_dialog", "Select password file"))
        self.btn_select_encrypted_file.setText(_translate(
            "decrypt_dialog",
            "Select encrypted file"
            if self.encrypted_filepath == "/" else reduce_text(self.encrypted_filepath)))
        self.setWindowTitle(_translate("decrypt_dialog", f"Safe V{VERSION} - decryption"))
        self.txt_password1.setText(_translate("decrypt_dialog", "Password 1"))
        self.btn_decrypt.setText(_translate("decrypt_dialog", "Decrypt"))
        self.btn_select_extraction_dir.setText(_translate("decrypt_dialog", "Select extraction directory"))
