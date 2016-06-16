#!/usr/bin/env python

# o rune

def help(s):
    help_text  = "[o]jar rune\n"
    help_text += "actions: info, quit"
    return help_text

def info(_):
    return "ojar v0.0"

def quit(_):
    from sys import exit
    exit(0)
