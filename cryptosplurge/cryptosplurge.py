#!/usr/bin/env python2
# -*- coding: utf-8 -*-

##################################################################
# cryptosplurge
# https://github.com/vesche
##################################################################

import os
import sys
from decrypt import *


help_text = '''
Usage: ./cryptosplurge.py <file>

Cryptosplurge attempts to decrypt a file by attempting many common decryption
methods, and displaying the decrypted text to the user. By manually skimming
the decrypted data, the encryption method could be easily found.
'''


def display(dec_data, decryption):
    os.system("clear")
    print dec_data
    raw_input("\nDecryption: {} ---> ENTER TO CONTINUE".format(decryption))


def run():
    try:
        input_file = sys.argv[1]
        with open(input_file) as f:
            enc_data = f.read()
        return enc_data
    except:
        print help_text
        sys.exit(1)


def main():
    enc_data = run()

    display(decrypt_base64(enc_data), "base64")
    display(decrypt_rotn(enc_data, 13), "rot13")

    for n in range(1,13)[::-1]:
        display(decrypt_rotn(enc_data, n), "rot{}".format(n))


if __name__ == "__main__":
    main()
