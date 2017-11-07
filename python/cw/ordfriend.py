#!/usr/bin/env python

import sys
from string import ascii_lowercase, ascii_uppercase

letters = ascii_lowercase + ascii_uppercase

with open(sys.argv[1]) as f:
    data = f.read().splitlines()

total = 0

for line in data:
    for letter in line:
        if letter in letters:
            total += ord(letter)

print total