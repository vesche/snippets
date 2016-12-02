#!/usr/bin/env python2
# -*- coding: utf-8 -*-

######################################
# Advent of Code 2016, Day 02 - Part 2
# https://github.com/vesche
######################################

def main():
    x, y = 1, 3
    
    grid = ['       ',
            '   1   ',
            '  234  ',
            ' 56789 ',
            '  ABC  ',
            '   D   ',
            '       ']
    
    with open("day02_input.txt") as f:
        for line in f.read().splitlines():
            for move in line:
                if move == 'U' and grid[y-1][x] != ' ':
                    y -= 1
                elif move == 'D' and grid[y+1][x] != ' ':
                    y += 1
                elif move == 'L' and grid[y][x-1] != ' ':
                    x -= 1
                elif move == 'R' and grid[y][x+1] != ' ':
                    x += 1
            print grid[y][x],


if __name__ == "__main__":
    main()