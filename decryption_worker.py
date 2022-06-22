from message_boxes import *
from AES import *
from PyQt5 import QtCore
import subprocess


class DecryptionWorker(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    status = QtCore.pyqtSignal(int)

    def decrypt_files(self, encrypted_filepath: str, password1: str | bytes, password2: str | bytes,
                      extraction_dir: str):

        decrypt_file(password2, encrypted_filepath, "encrypted.7z")
        command = f'''7z e -t7z encrypted.7z -o"{extraction_dir}" -p"{password1}" -y'''
        code = subprocess.call(command)

        if os.path.exists("encrypted.7z"):
            os.remove("encrypted.7z")

        if code != 0:
            self.status.emit(1)
            self.finished.emit()
            return

        self.status.emit(0)
        self.finished.emit()
