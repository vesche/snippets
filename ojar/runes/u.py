#!/usr/bin/env python

# [u]nit rune

def ftoc(f):
    return float(5) / float(9) * (int(f) - 32)

def info(_):
    from common import list_functions
    return "[u]nit rune\nactions: {}".format(list_functions(__name__))
