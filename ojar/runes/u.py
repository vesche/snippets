# -*- coding: utf-8 -*-

#
# ojar - [u]nit rune
# https://github.com/vesche/ojar
#


def ftoc(f):
    try:
        f = float(f)
    except ValueError:
        return 'Invalid argument.'
    return float(5) / float(9) * (f - 32)


def info(_):
    from runes.common import list_functions
    return '[u]nit rune\nactions: {}'.format(list_functions(__name__))
