from main_window import *
import sys


def main():
    app = QtWidgets.QApplication(sys.argv)
    window_form = QtWidgets.QWidget()

    safe_ui = MainWindowUI()
    safe_ui.setup(window_form)

    window_form.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
