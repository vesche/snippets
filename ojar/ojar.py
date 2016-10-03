#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ojar (Oh, Just Another REPL)
# https://github.com/vesche/ojar


import readline
from string import ascii_lowercase


help_text  = '''ojar (Oh, Just Another REPL)
https://github.com/vesche/ojar

Syntax:
<rune> <action> <argument>

Example:
> s ?
[s]tring rune
actions: info, length

> s length Hello, world!
13

See `o runelist` for a list of runes.
'''
invalid_text = "Invalid {}.\n"


def main():

    while True:

        # input
        command = raw_input("> ").split()

        # noop
        if command == []:
            continue

        # help
        elif command == ['?']:
            print help_text
            continue

        # get rune
        try:
            rune = command[0]
            if (rune not in ascii_lowercase) or (len(rune) != 1): raise
            rune = getattr(__import__("runes", globals(), locals(), \
            [rune], -1), rune)
        except:
            print invalid_text.format("rune")
            continue

        # get action
        try:
            action = command[1]
            if action == '?':
                action = "info"
            action = getattr(rune, action)
        except:
            print invalid_text.format("action")
            continue

        # get argument
        try:
            argument = ' '.join(command[2:])
        except:
            print invalid_text.format("argument")
            continue

        # output
        print str(action(argument)) + '\n'


if __name__ == "__main__":
    main()
