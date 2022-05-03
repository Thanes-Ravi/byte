from __future__ import print_function, unicode_literals
from Cryptodome.Cipher import AES

import random
import string
import click
filepath = ""
datapath = ""


@click.group()
def main():
    pass

@main.command()
@click.argument('filepath', required=True)
@click.argument('filename', default="data")
def encrypt(filepath, filename):
    """encrypt your file"""
    with open(filepath, "rb") as filepath:
        f = filepath.read()
        data = bytearray(f)

        digits = random.choices(string.digits, k=7)
        letters = random.choices(string.ascii_uppercase, k=9)
        key = random.sample(digits + letters, 16)
        key = ''.join(key)
        key = bytes(key, 'utf-8')
        dataname = (filename, "bin" )
        dataname = ".".join(dataname)

        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(data)
        file_out = open(dataname, "wb")

        [ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
        file_out.close()
        print("Key:",key)

@main.command()
@click.argument('datapath', required=True)
@click.argument('filename', required=True)
def decrypt(datapath, filename):
    """decrypt your bin file"""
    file_in = open(datapath, "rb")
    nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
    passstr = input("Key:")
    key = passstr.encode('utf-8')

    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    with open(filename, 'wb') as f:
        f.write(data)

if __name__ == "__main__":
    main()