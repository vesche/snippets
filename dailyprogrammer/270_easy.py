#!/usr/bin/env python

if __name__ == "__main__":
    data = open('270_easy_input.txt').read().splitlines()

    for i in range(len(max(data, key=len))):
        for j in data:
            try:
                print(j[i], end='')
            except:
                print(' ', end='')
        print()
