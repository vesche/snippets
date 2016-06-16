#!/usr/bin/env python

from string import ascii_lowercase

if __name__ == "__main__":
    while True:
        command = raw_input("> ").split()

        try:
            rune = command[0]
            if (rune not in ascii_lowercase) or (len(rune) != 1): raise
            rune = getattr(__import__("runes", globals(), locals(), [rune], -1), rune)
        except:
            print "Invalid rune."
            continue

        try:
            action = command[1]
            if action == '?':
                action = "help"
            action = getattr(rune, action)
        except:
            print "Invalid action."
            continue

        try:
            argument = ' '.join(command[2:])
        except:
            print "Invalid argument."
            continue

        print str(action(argument)) + '\n'
