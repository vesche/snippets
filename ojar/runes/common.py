# -*- coding: utf-8 -*-

#
# ojar - common functions for runes
# https://github.com/vesche/ojar
#


def list_functions(rune_module):
    from sys import modules
    functions = dir(modules[rune_module])
    return ', '.join([f for f in functions if '__' not in f])
