#!/usr/bin/env python

def main():
    loc = 0
    locations = {0:1}

    with open("03_input.txt", 'r') as f:
        for direction in f.read():
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
            except:
                locations[loc] = 1

    return len(locations)

if __name__ == "__main__":
    print main()
