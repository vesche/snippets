# -*- coding: utf-8 -*-

import base64
from string import ascii_lowercase


def decrypt_base64(enc_data):
    try:
        return base64.b64decode(enc_data)
    except:
        return "ERROR"


def decrypt_rotn(enc_data, n):
    dec = ''
    for i in enc_data.lower():
        try:
            offset = n + ascii_lowercase.index(i)
            if offset >= 25:
                offset -= 26
            char = ascii_lowercase[offset]
        except:
            char = i
        dec += char
    return dec
