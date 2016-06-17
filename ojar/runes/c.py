#!/usr/bin/env python

# [c]rypto rune

def info(_):
    help_text  = "[c]rypto rune\n"
    help_text += "actions: md5"
    return help_text

def md5(fpath):
    from hashlib import md5 as getmd5hash
    from os import path
    if path.exists(fpath):
        return getmd5hash(open(fpath, 'rb').read()).hexdigest()
    else:
        return "Invalid path."