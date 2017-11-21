#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#
# Advent of Code 2016, Day 05 - Part 2
# https://github.com/vesche
#

import itertools
import hashlib


def md5hash(string):
    m = hashlib.md5()
    m.update(string)
    return m.hexdigest()


def show(password):
    print "\033c" + ''.join(password)


def main():
    door_id = "ojvtpuvg"
    password = list("________")
    show(password)

    for n in itertools.count():

        h = md5hash(door_id + str(n))

        if h[:5] == "00000":
            try:
                if password[int(h[5])] == '_':
                    password[int(h[5])] = h[6]
            except:
                pass

            show(password)

            if '_' not in password:
                break


if __name__ == "__main__":
    main()
