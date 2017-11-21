#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#
# dailyprogrammer 240 easy
# https://github.com/vesche
#

import random


def main():
    scram_words = []
    with open('input.txt', 'r') as f:
        words = [list(_) for _ in f.read().split()]

    for word in words:
        if len(word) < 3:
            scram_words.append(''.join(word))
        else:
            first, scram, last = word.pop(0), "", word.pop()
            while len(word):
                letter = random.choice(word)
                scram += letter
                word.remove(letter)
            scram_words.append(first + scram + last)

    print ' '.join(scram_words)


if __name__ == "__main__":
    main()
