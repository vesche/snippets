#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#################################
# Advent of Code, Day 05 - Part 1
# https://github.com/vesche
#################################

from string import ascii_lowercase


def main():
    nice_count = 0
    bad_pairs = ['ab', 'cd', 'pq', 'xy']
    vowels = list('aeiou')

    with open("day05_input.txt", 'r') as f:
        for s in f.read().splitlines():
            nice = True
            for pair in bad_pairs:
                if pair in s:
                    nice = False

            vowel_count = 0
            for letter in s:
                if letter in vowels:
                    vowel_count += 1
            if vowel_count < 3:
                nice = False

            count = 0
            for letter in ascii_lowercase:
                if letter * 2 in s:
                    count += 1
            if count == 0:
                nice = False

            if nice:
                nice_count += 1

    print nice_count


if __name__ == "__main__":
    main()
