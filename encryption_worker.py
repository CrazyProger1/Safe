from typing import Iterable
from AES import *
import PyQt5.QtCore as QtCore
import subprocess


class EncryptionWorker(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    status = QtCore.pyqtSignal(int)

    def encrypt_files(self, files: Iterable[str], password1: str, password2: str, out_filepath: str):
        command = f'''7z a -t7z encrypted.7z "{'" "'.join(files)}" -p"{password1}" -y'''
        code = subprocess.call(command)

        if code != 0:
            self.status.emit(1)
            self.finished.emit()
            return

        encrypt_file(password2, "encrypted.7z", out_filepath)

        if os.path.exists("encrypted.7z"):
            os.remove("encrypted.7z")

        self.status.emit(0)
        self.finished.emit()
