#!/usr/bin/env python

# o rune

#def clear(_):
#    from os import system
#    system('clear')
#    return ""

def info(_):
    help_text  = "[o]jar rune\n"
    help_text += "actions: quit, version"
    return help_text

def version(_):
    return "ojar v0.0"

def quit(_):
    from sys import exit
    exit(0)
