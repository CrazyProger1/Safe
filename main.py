from main_window import *
from decryption_dialog import *
import sys


def main():
    app = QtWidgets.QApplication(sys.argv)

    if len(sys.argv) > 1:
        decrypt_dialog = DecryptionDialogUI(sys.argv[1])
        decrypt_dialog.show()
    else:
        main_window = MainWindowUI()
        main_window.show()

    app.exec()


if __name__ == '__main__':
    main()
