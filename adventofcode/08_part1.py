#!/usr/bin/env python

def main():
    literal, actual = 0, 0

    with open("08_input.txt") as f:
        lines = f.read().splitlines()

    for line in lines:
        literal += len(line)
        actual  += len(eval(line))

    return literal - actual

if __name__ == "__main__":
    print main()
