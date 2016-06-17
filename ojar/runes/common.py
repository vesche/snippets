#!/usr/bin/env python

# common functions for runes

def list_functions(rune_module):
    from sys import modules
    functions = dir(modules[rune_module])
    return ', '.join([f for f in functions if '__' not in f])
