# -*- coding: utf-8 -*-

#
# ojar - [?] rune
# https://github.com/vesche/ojar
#


def info(_):
    from runes.common import list_functions
    return '[?] rune\nactions: {}'.format(list_functions(__name__))
