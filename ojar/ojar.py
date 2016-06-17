#!/usr/bin/env python

import readline
from string import ascii_lowercase

help_text  = '''ojar (Oh, Just Another REPL) - https://github.com/vesche/ojar

Welcome to ojar, a little toolkit for doing simple tasks. It uses runes \
(single letters) as categories, actions (words with meaning) to define what \
you want to do, and arguments (supplied data).

How do I use this thing?
It's as easy as rune, action, argument. For example, let's say you wanted to \
know the length of a string. Well then use the [s]tring rune, the 'length' \
action, and supply it an argument. Check it out:
> s length Hello, world!
13

Hmm, nifty. So how do I know what rune does what?
The [o]jar rune is used for these admin sorts of things. Run 'o runelist' to \
get a list of all the runes and their purpose.

Cool, but how do I know what I can do with a rune?
When in doubt use '?'. For example, if you wanted to know all the actions you \
could do with the [s]tring rune see 's ?'.
'''

invalid_text = "Invalid {}.\n"

if __name__ == "__main__":

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
