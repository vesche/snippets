#!/usr/bin/env python

# [n]etwork rune

def externalip(_):
    from urllib2 import urlopen
    return urlopen("http://myexternalip.com/raw").read().strip()

def info(_):
    from common import list_functions
    return "[n]etwork rune\nactions: {}".format(list_functions(__name__))
