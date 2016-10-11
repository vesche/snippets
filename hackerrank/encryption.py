#!/usr/bin/env python2
# -*- coding: utf-8 -*-

######################################################
# hackerrank, encryption
# https://www.hackerrank.com/challenges/encryption
# https://github.com/vesche
######################################################

import math


def main():
    stdin = raw_input()
    rows = int(math.floor(math.sqrt(len(stdin))))
    cols = int(math.ceil(math.sqrt(len(stdin))))

    li = []
    for i in range(len(stdin)):
        if i % cols == 0:
            li.append(stdin[i:i+cols])

    blob = []
    for i in range(len(li[0])):
        blob.append('')

    for i in range(len(li)):
        for j in range(len(li[i])):
            blob[j] += li[i][j]

    print ' '.join(blob)


if __name__ == "__main__":
    main()
