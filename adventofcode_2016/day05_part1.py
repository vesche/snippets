#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#
# Advent of Code 2016, Day 05 - Part 1
# https://github.com/vesche
#

import itertools
import hashlib


def md5hash(string):
    m = hashlib.md5()
    m.update(string)
    return m.hexdigest()


def main():
    door_id = "ojvtpuvg"
    password = ''

    for n in itertools.count():

        h = md5hash(door_id + str(n))

        if h[:5] == "00000":
            password += h[5]

            if len(password) == 8:
                break

    return password


if __name__ == "__main__":
    print main()
