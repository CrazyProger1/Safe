from PyQt5 import QtCore, QtGui, QtWidgets
from config import *


def show_critical(message: str):
    window = QtWidgets.QDialog()
    window.setWindowIcon(QtGui.QIcon(ICO_PATH))
    QtWidgets.QMessageBox.critical(window, "Safe", message, QtWidgets.QMessageBox.Ok)


def show_info(message: str):
    window = QtWidgets.QDialog()
    window.setWindowIcon(QtGui.QIcon(ICO_PATH))
    QtWidgets.QMessageBox.information(window, "Safe", message, QtWidgets.QMessageBox.Ok)
