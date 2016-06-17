#!/usr/bin/env python

# [o]jar rune

def clear(_):
    from os import system, name
    system('cls' if name == 'nt' else 'clear')
    return _
    
def info(_):
    help_text  = "[o]jar rune\n"
    help_text += "actions: clear, quit, runelist, version"
    return help_text

def runelist(_):
    runes = ["crypto", "evil", "ojar", "random", "string", "unit"]
    return ''.join(["[{0}]{1}\n".format(rune[0], rune[1:]) for rune in runes])

def version(_):
    return "ojar v0.0"

def quit(_):
    from sys import exit
    exit(0)
