from main_window import *
import sys


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindowUI()
    main_window.show()
    app.exec()


if __name__ == '__main__':
    main()
