#!/usr/bin/env python

# [c]rypto rune

def info(_):
    from common import list_functions
    return "[c]rypto rune\nactions: {}".format(list_functions(__name__))

def md5(file_path):
    from hashlib import md5 as getmd5hash
    from os.path import isfile
    if isfile(file_path):
        return getmd5hash(open(file_path, 'rb').read()).hexdigest()
    else:
        return "Invalid path."
