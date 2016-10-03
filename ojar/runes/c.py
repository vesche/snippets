#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ojar - [c]rypto rune


def info(_):
    from common import list_functions
    return "[c]rypto rune\nactions: {}".format(list_functions(__name__))


def hashall(file_path):
    from os.path import isfile
    if isfile(file_path):
        return  "md5: {}\nsha1: {}\nsha224: {}\nsha256: {}\nsha384: {}\nsha5" \
                "12: {}".format(md5(file_path), sha1(file_path),
                sha224(file_path), sha256(file_path), sha384(file_path),
                sha512(file_path))
    else:
        return "Invalid path."


def md5(file_path):
    from hashlib import md5 as getmd5
    from os.path import isfile
    if isfile(file_path):
        return getmd5(open(file_path, 'rb').read()).hexdigest()
    else:
        return "Invalid path."


def sha1(file_path):
    from hashlib import sha1 as getsha1
    from os.path import isfile
    if isfile(file_path):
        return getsha1(open(file_path, 'rb').read()).hexdigest()
    else:
        return "Invalid path."


def sha224(file_path):
    from hashlib import sha224 as getsha224
    from os.path import isfile
    if isfile(file_path):
        return getsha224(open(file_path, 'rb').read()).hexdigest()
    else:
        return "Invalid path."


def sha256(file_path):
    from hashlib import sha256 as getsha256
    from os.path import isfile
    if isfile(file_path):
        return getsha256(open(file_path, 'rb').read()).hexdigest()
    else:
        return "Invalid path."


def sha384(file_path):
    from hashlib import sha384 as getsha384
    from os.path import isfile
    if isfile(file_path):
        return getsha384(open(file_path, 'rb').read()).hexdigest()
    else:
        return "Invalid path."


def sha512(file_path):
    from hashlib import sha512 as getsha512
    from os.path import isfile
    if isfile(file_path):
        return getsha512(open(file_path, 'rb').read()).hexdigest()
    else:
        return "Invalid path."
