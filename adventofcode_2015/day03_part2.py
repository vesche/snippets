#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#################################
# Advent of Code, Day 03 - Part 2
# https://github.com/vesche
#################################


def run(li):
    loc = 0
    locations = {0:1}

    for direction in li:
        if direction == '^':
            loc += 1000
        elif direction == 'v':
            loc -= 1000
        elif direction == '>':
            loc += 1
        elif direction == '<':
            loc -= 1
        try:
            locations[loc] += 1
        except KeyError:
            locations[loc] = 1

    return locations


def main():
    santa_data, rsanta_data = '', ''

    with open("day03_input.txt", 'r') as f:
        data = f.read()
        for i in range(len(data)):
            if i % 2 == 0:
                santa_data += data[i]
            else:
                rsanta_data += data[i]

    santa = run(santa_data)
    rsanta = run(rsanta_data)
    combine = santa.copy()
    combine.update(rsanta)

    print len(combine)


if __name__ == "__main__":
    main()
