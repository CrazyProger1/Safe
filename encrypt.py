from typing import Iterable
import subprocess
from Crypto.Cipher import AES
import os
import struct
from Crypto import Random


def encrypt_file(key: bytes | str, in_filename: str, out_filename: str | None = None, chunk_size: int = 64 * 1024):
    """ Encrypts a file using AES (CBC mode) with the
        given key.

        key:
            The encryption key - a string that must be
            either 16, 24 or 32 bytes long. Longer keys
            are more secure.

        in_filename:
            Name of the input file

        out_filename:
            If None, '<in_filename>.enc' will be used.

        chunksize:
            Sets the size of the chunk which the function
            uses to read and encrypt the file. Larger chunk
            sizes can be faster for some files and machines.
            chunksize must be divisible by 16.
    """
    if not out_filename:
        out_filename = in_filename + '.enc'

    if type(key) is str:
        key = key.encode("utf-8")

    # iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    iv = Random.new().read(AES.block_size)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    # 1234567890qwertyuiopasdfghjklzxc
    file_size = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', file_size))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunk_size)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' '.encode() * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))


def encrypt_files(files: Iterable[str], password1: str, password2: str, out_filepath: str):
    command = f'''7z a -t7z encrypted.7z "{'" "'.join(files)}" -p"{password1}"'''
    code = subprocess.call(command)

    print("7z exited with code: " + str(code))

    encrypt_file(password2, "encrypted.7z", out_filepath)
    print("Files encrypted. Cleaning up")

    os.remove("encrypted.7z")
    # print(code)
