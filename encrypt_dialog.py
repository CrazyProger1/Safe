from PyQt5 import QtCore, QtGui, QtWidgets
from styles import *
from config import *
from encrypt import *
import threading


class EncryptDialogUI(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.btn_add_file: None | QtWidgets.QPushButton = None
        self.btn_delete_file: None | QtWidgets.QPushButton = None
        self.btn_clear_list: None | QtWidgets.QPushButton = None
        self.lst_file_list: None | QtWidgets.QListWidget = None
        self.edit_password1: None | QtWidgets.QLineEdit = None
        self.txt_password1: None | QtWidgets.QLabel = None
        self.edit_password2: None | QtWidgets.QLineEdit = None
        self.txt_password2: None | QtWidgets.QLabel = None
        self.btn_select_out_file: None | QtWidgets.QPushButton = None
        self.btn_encrypt: None | QtWidgets.QPushButton = None
        self.btn_select_out_pwd_file: None | QtWidgets.QPushButton = None
        self.encryption_thread: None | QtCore.QThread = None
        self.encryption_worker: None | EncryptionWorker = None

        self.output_filepath = ""
        self.output_password_filepath = ""
        self.setup()

    def setup(self):
        self.setObjectName("encrypt_dialog")
        self.setFixedSize(481, 734)
        self.setStyleSheet(ENCRYPT_DIALOG_STYLE)

        self.btn_add_file = QtWidgets.QPushButton(self)
        self.btn_add_file.setGeometry(QtCore.QRect(10, 450, 131, 41))
        self.btn_add_file.setStyleSheet(TEXT_STYLE)
        self.btn_add_file.setObjectName("btn_add_file")
        self.btn_add_file.clicked.connect(self.add_file)

        self.btn_delete_file = QtWidgets.QPushButton(self)
        self.btn_delete_file.setGeometry(QtCore.QRect(150, 450, 131, 41))
        self.btn_delete_file.setStyleSheet(TEXT_STYLE)
        self.btn_delete_file.setObjectName("btn_delete_file")
        self.btn_delete_file.clicked.connect(self.delete_file)

        self.btn_clear_list = QtWidgets.QPushButton(self)
        self.btn_clear_list.setGeometry(QtCore.QRect(290, 450, 181, 41))
        self.btn_clear_list.setStyleSheet(TEXT_STYLE)
        self.btn_clear_list.setObjectName("btn_clear_list")
        self.btn_clear_list.clicked.connect(self.clear_file_list)

        self.lst_file_list = QtWidgets.QListWidget(self)
        self.lst_file_list.setGeometry(QtCore.QRect(10, 10, 461, 421))
        self.lst_file_list.setObjectName("lst_file_list")

        self.edit_password1 = QtWidgets.QLineEdit(self)
        self.edit_password1.setGeometry(QtCore.QRect(10, 530, 461, 21))
        self.edit_password1.setText("")
        self.edit_password1.setObjectName("edit_password1")

        self.txt_password1 = QtWidgets.QLabel(self)
        self.txt_password1.setGeometry(QtCore.QRect(10, 510, 241, 16))
        self.txt_password1.setStyleSheet(TEXT_STYLE)
        self.txt_password1.setObjectName("txt_password1")

        self.edit_password2 = QtWidgets.QLineEdit(self)
        self.edit_password2.setGeometry(QtCore.QRect(10, 580, 461, 21))
        self.edit_password2.setText("")
        self.edit_password2.setObjectName("edit_password2")

        self.txt_password2 = QtWidgets.QLabel(self)
        self.txt_password2.setGeometry(QtCore.QRect(10, 560, 410, 16))
        self.txt_password2.setStyleSheet(TEXT_STYLE)
        self.txt_password2.setObjectName("txt_password2")

        self.btn_select_out_file = QtWidgets.QPushButton(self)
        self.btn_select_out_file.setGeometry(QtCore.QRect(10, 610, 221, 41))
        self.btn_select_out_file.setStyleSheet(TEXT_STYLE)
        self.btn_select_out_file.setObjectName("btn_select_out_file")
        self.btn_select_out_file.clicked.connect(self.select_output_file)

        self.btn_select_out_pwd_file = QtWidgets.QPushButton(self)
        self.btn_select_out_pwd_file.setGeometry(QtCore.QRect(250, 610, 221, 41))
        self.btn_select_out_pwd_file.setStyleSheet(TEXT_STYLE)
        self.btn_select_out_pwd_file.setObjectName("btn_select_out_pwd_file")
        self.btn_select_out_pwd_file.clicked.connect(self.select_output_password_file)

        self.btn_encrypt = QtWidgets.QPushButton(self)
        self.btn_encrypt.setGeometry(QtCore.QRect(10, 670, 461, 51))
        self.btn_encrypt.setStyleSheet(TEXT_STYLE)
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.btn_encrypt.clicked.connect(self.encrypt)

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def add_file(self):
        filepath = QtWidgets.QFileDialog.getOpenFileName(self, "Select a file", "/")[0]
        item = QtWidgets.QListWidgetItem()
        item.setText(filepath)
        self.lst_file_list.addItem(item)

    def delete_file(self):
        selected_items = self.lst_file_list.selectedItems()
        if len(selected_items) > 0:
            selected_item = selected_items[0]
            self.lst_file_list.takeItem(self.lst_file_list.indexFromItem(selected_item).row())

    def clear_file_list(self):
        self.lst_file_list.clear()

    def select_output_file(self):
        self.output_filepath = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Select an output file",
            "/",
            filter="*.sf"
        )[0]

    def select_output_password_file(self):
        self.output_password_filepath = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Select an output password file",
            "/", filter="*.pwd"
        )[0]

    def encrypt(self):
        password1 = self.edit_password1.text()
        password2 = self.edit_password2.text()
        files = []
        for index in range(self.lst_file_list.count()):
            files.append(self.lst_file_list.item(index).text())

        self.encryption_thread = QtCore.QThread()
        self.encryption_worker = EncryptionWorker()

        self.encryption_worker.moveToThread(self.encryption_thread)
        self.encryption_worker.finished.connect(self.encryption_thread.quit)

        self.encryption_thread.started.connect(
            lambda: self.encryption_worker.encrypt_files(files, password1, password2, self.output_filepath)
        )

        self.encryption_thread.start()

        window = QtWidgets.QDialog()
        window.setWindowIcon(QtGui.QIcon("resources/logo.ico"))
        self.encryption_thread.finished.connect(
            lambda: QtWidgets.QMessageBox.information(window, "Safe", "Files encrypted", QtWidgets.QMessageBox.Ok)
        )

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowIcon(QtGui.QIcon('resources/logo.ico'))
        self.setWindowTitle(_translate("encrypt_dialog", "Dialog"))
        self.btn_add_file.setText(_translate("encrypt_dialog", "+ File"))
        self.btn_delete_file.setText(_translate("encrypt_dialog", "- File"))
        self.btn_clear_list.setText(_translate("encrypt_dialog", "Clear list"))
        self.setWindowTitle(_translate("encrypt_dialog", f"Safe V{VERSION} - encryption"))
        __sortingEnabled = self.lst_file_list.isSortingEnabled()
        self.lst_file_list.setSortingEnabled(False)
        self.lst_file_list.setSortingEnabled(__sortingEnabled)
        self.txt_password1.setText(_translate("encrypt_dialog", "Password 1 (remember it)"))
        self.txt_password2.setText(
            _translate("encrypt_dialog", "Password 2 (will be saved to a file, you can store it on USB)"))
        self.btn_select_out_file.setText(_translate("encrypt_dialog", "Select output file"))
        self.btn_select_out_pwd_file.setText(_translate("encrypt_dialog", "Select output password file"))
        self.btn_encrypt.setText(_translate("encrypt_dialog", "Encrypt"))
