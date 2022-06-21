from PyQt5 import QtCore, QtGui, QtWidgets


def show_critical(message: str):
    window = QtWidgets.QDialog()
    window.setWindowIcon(QtGui.QIcon("resources/logo.ico"))
    QtWidgets.QMessageBox.critical(window, "Safe", message, QtWidgets.QMessageBox.Ok)


def show_info(message: str):
    window = QtWidgets.QDialog()
    window.setWindowIcon(QtGui.QIcon("resources/logo.ico"))
    QtWidgets.QMessageBox.information(window, "Safe", message, QtWidgets.QMessageBox.Ok)
