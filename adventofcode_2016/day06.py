#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#############################
# Advent of Code 2016, Day 06
# https://github.com/vesche
#############################

def main():
    d = [{}, {}, {}, {}, {}, {}, {}, {}]

    with open("day06_input.txt") as f:
        for word in f.read().splitlines():
            for i in range(len(word)):
                letter = word[i]
                if letter in d[i]:
                    d[i][letter] += 1
                else:
                    d[i][letter] = 1

    most_common, least_common = '', ''
    for i in range(len(d)):
        most_common += max(d[i], key=d[i].get)
        least_common += min(d[i], key=d[i].get)

    print "Part One: {}, Part Two: {}".format(most_common, least_common)


if __name__ == "__main__":
    main()
