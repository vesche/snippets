# -*- coding: utf-8 -*-

##################################
# dailyprogrammer 223 intermediate
# https://github.com/vesche
##################################


def problem(secret, offensive):
    for letter in offensive:
        try:
            p = secret.index(letter)
            secret = secret[p+1:]
        except:
            return False
    return True
