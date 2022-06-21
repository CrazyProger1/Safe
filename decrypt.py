from Crypto.Cipher import AES
import os
import random
import struct
from Crypto import Random
import subprocess
import string


def decrypt_file(key: str | bytes, in_filename: str, out_filename: str | None = None, chunk_size: int = 64 * 1024):
    """ Decrypts a file using AES (CBC mode) with the
        given key. Parameters are similar to encrypt_file,
        with one difference: out_filename, if not supplied
        will be in_filename without its last extension
        (i.e. if in_filename is 'aaa.zip.enc' then
        out_filename will be 'aaa.zip')
    """
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]

    if type(key) is str:
        key = key.encode("utf-8")

    with open(in_filename, 'rb') as infile:
        original_size = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunk_size)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(original_size)


def decrypt_files(encrypted_filepath: str, password1: str, password2: str, extraction_dir: str):
    if extraction_dir in string.ascii_uppercase:
        extraction_dir += ":/"

    decrypt_file(password2, encrypted_filepath, "encrypted.7z")
    command = f'''7z e -t7z encrypted.7z -o"{extraction_dir}" -p"{password1}"'''
    code = subprocess.call(command)
    print("7z exited with code: " + str(code))
    os.remove("encrypted.7z")
    print("Decrypted")
