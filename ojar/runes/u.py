#!/usr/bin/env python

# [u]nit rune

def ftoc(f):
    #from __future__ import division
    return 5/9 * (int(f) - 32)

def info(_):
    help_text  = "[u]nit rune\n"
    help_text += "actions: ftoc"
    return help_text
