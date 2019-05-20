#!/usr/bin/env python

# part 1
data = open('day05.input').read()

def react(data):
    while True:
        done = True
        for i, a in enumerate(data):
            try:
                b = data[i+1]
            except IndexError: break
            if (a.lower() == b.lower()) and \
            ((a.islower() and b.isupper()) or (a.isupper() and b.islower())):
                data = data.replace(a+b, '', 1)
                done = False
        if done:
            break
    return data

polymer = react(data)
print(len(polymer))

# part 2
from string import ascii_lowercase

lengths = []
for letter in ascii_lowercase:
    p = polymer.replace(letter.lower(), '').replace(letter.upper(), '')
    lengths.append(len(react(p)))
print(min(lengths))
