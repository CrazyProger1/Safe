from message_boxes import *
from AES import *
from PyQt5 import QtCore
import string
import subprocess


class DecryptionWorker(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    status = QtCore.pyqtSignal(int)

    def decrypt_files(self, encrypted_filepath: str, password1: str | bytes, password2: str | bytes,
                      extraction_dir: str):

        if extraction_dir in string.ascii_uppercase:
            extraction_dir += ":/"

        decrypt_file(password2, encrypted_filepath, "encrypted.7z")
        command = f'''7z e -t7z encrypted.7z -o"{extraction_dir}" -p"{password1}" -y'''
        code = subprocess.call(command)

        if code != 0:
            self.status.emit(1)
            self.finished.emit()
            return

        if os.path.exists("encrypted.7z"):
            os.remove("encrypted.7z")

        self.status.emit(0)
        self.finished.emit()
