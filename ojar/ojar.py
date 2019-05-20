#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# ojar (Oh, Just Another REPL)
# https://github.com/vesche/ojar
#

import importlib
import readline


__version__ = '0.1'
HELP_TEXT  = '''ojar (Oh, Just Another REPL)
https://github.com/vesche/ojar

Syntax:
    <rune> <action> <argument>

Example:
    ojar > s ?
    [s]tring rune
    actions: info, length

    ojar > s length Hello, world!
    13

See `o runelist` for a list of runes.'''


def ojar_loop():
    # input
    prompt = input('ojar > ').split()

    # noop
    if prompt == []:
        return

    # help
    elif prompt == ['?']:
        return HELP_TEXT

    # get rune
    try:
        rune = prompt[0]
        rune = importlib.import_module('runes.{}'.format(rune))
    except ImportError:
        return 'Invalid rune.'

    # get action
    try:
        action = prompt[1]
        if action == '?':
            action = 'info'
        action = getattr(rune, action)
    except (AttributeError, IndexError):
        return 'Invalid action.'

    # get argument
    argument = ' '.join(prompt[2:])

    # output
    return action(argument)


def main():
    print('ojar v{}\nType "?" for help.\n'.format(__version__))

    while True:
        result = ojar_loop()
        if result:
            print(str(result) + '\n')


if __name__ == '__main__':
    main()
