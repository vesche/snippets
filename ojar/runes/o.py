#
# ojar - [o]jar rune
# https://github.com/vesche/ojar
#


def clear(_):
    from os import system, name
    system('cls' if name == 'nt' else 'clear')
    return _


def info(_):
    from runes.common import list_functions
    return '[o]jar rune\nactions: {}'.format(list_functions(__name__))


def runelist(_):
    runes = [ 'crypto', 'evil', 'ojar', 'random', 'string', 'unit' ]
    return ''.join(['[{0}]{1}\n'.format(rune[0], rune[1:]) \
    for rune in runes]).rstrip()


def version(_):
    return 'ojar v0.1'


def quit(_):
    from sys import exit
    exit(0)
