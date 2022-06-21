from PyQt5 import QtCore, QtGui, QtWidgets
from styles import *
from config import *
from encrypt import encrypt_files
import threading


class DecryptDialogUI(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.setObjectName("decrypt_dialog")
        self.setFixedSize(477, 170)
        self.setStyleSheet("QPushButton{\n"
                           "    \n"
                           "    background-color: rgb(0, 0, 0);\n"
                           "    color: rgb(0, 255, 0);\n"
                           "\n"
                           "\n"
                           "}\n"
                           "\n"
                           "\n"
                           "\n"
                           "\n"
                           "QLabel{\n"
                           "    color: rgb(0, 255, 0);\n"
                           "}\n"
                           "\n"
                           "\n"
                           "QWidget#decrypt_dialog{\n"
                           "    background-color: rgb(0, 0, 0);\n"
                           "}\n"
                           "\n"
                           "QPushButton:hover{\n"
                           "    border: 1px solid rgb(0, 255, 0);\n"
                           "}\n"
                           "\n"
                           "QPushButton:pressed{\n"
                           "    \n"
                           "    background-color: rgb(130, 130, 130);\n"
                           "}\n"
                           "\n"
                           "QLineEdit{\n"
                           "    \n"
                           "    background-color: rgb(0, 0, 0);\n"
                           "    border: 1px dashed rgb(255, 255, 255);\n"
                           "    color: rgb(0, 255, 0);\n"
                           "    \n"
                           "}\n"
                           "\n"
                           "QLineEdit:hover{\n"
                           "    border: 1px solid rgb(255, 255, 255);\n"
                           "}\n"
                           "\n"
                           "\n"
                           "QListWidget{\n"
                           "    color: rgb(0, 255, 0);\n"
                           "    background-color: rgb(0, 0, 0);\n"
                           "    font: 8pt \"Segoe Print\";\n"
                           "    border: 1px dashed rgb(255, 255, 255);\n"
                           "\n"
                           "}\n"
                           "\n"
                           "")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(250, 10, 221, 41))
        self.pushButton.setStyleSheet("font: 8pt \"Segoe Print\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 221, 41))
        self.pushButton_2.setStyleSheet("font: 8pt \"Segoe Print\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(10, 80, 461, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 60, 81, 16))
        self.label.setStyleSheet("font: 8pt \"Segoe Print\";")
        self.label.setObjectName("label")
        self.btn_encrypt = QtWidgets.QPushButton(self)
        self.btn_encrypt.setGeometry(QtCore.QRect(10, 110, 461, 51))
        self.btn_encrypt.setStyleSheet("font: 8pt \"Segoe Print\";")
        self.btn_encrypt.setObjectName("btn_encrypt")

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("decrypt_dialog", "Dialog"))
        self.pushButton.setText(_translate("decrypt_dialog", "Select password file"))
        self.pushButton_2.setText(_translate("decrypt_dialog", "Select encrypted file"))
        self.label.setText(_translate("decrypt_dialog", "Password 1"))
        self.btn_encrypt.setText(_translate("decrypt_dialog", "Encrypt"))
