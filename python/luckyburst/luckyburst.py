#!/usr/bin/env python2

#
# luckyburst
#

import os
import readline
import sys


banner = '''
 _,  _,_  _, _,_ , _ __, _,_ __,  _, ___
 |   | | / ` |_/ \ | |_) | | |_) (_   |
 | , | | \ , | \  \| |_) | | | \ , )  |
 ~~~ `~'  ~  ~ ~   ) ~   `~' ~ ~  ~   ~
                  ~'
I solemnly swear that I am up to no good.
'''
help_text = '''luckyburst - initial access tool
commands: ls, set, run, quit, help'''
running = True


def invalid(text):
    print "Invalid {}.".format(text)


def luckyburst_cli():
    platform = exploit = ''
    print banner

    while running:
        stdin = raw_input("{}-{}> ".format(platform, exploit)).lower().split()

        # noop
        if stdin == []:
            continue

        command, argument = stdin[0], ' '.join(stdin[1:])

        if command in ["quit", "exit"]:
            sys.exit(1)

        elif command in ["help", "info", '?']:
            print help_text

        elif command == "ls":
            path = "platform/" + platform + argument
            try:
                print '\t\n'.join([f for f in os.listdir(path)])
            except OSError:
                invalid("path")

        elif command == "set":
            try:
                var_name, var_value = [i.strip() for i in argument.split()]
            except ValueError:
                invalid("term"); continue

            ### this needs checks
            if var_name == "platform":
                platform = var_value
            elif var_name == "exploit":
                exploit = var_value

        else:
            invalid("command")


if __name__ == "__main__":
    luckyburst_cli()
