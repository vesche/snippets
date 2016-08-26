#!/usr/bin/env python

def main():
    final_floor = 0
    moves = 0

    with open("01_input.txt", 'r') as f:
        for floor in f.read():
            if floor == '(':
                final_floor += 1
            elif floor == ')':
                final_floor -= 1

            moves += 1
            if final_floor == -1:
                return moves

if __name__ == "__main__":
    print main()
