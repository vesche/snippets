#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    data = f.read().splitlines()

# checks:
# length at least 8 char
# at least 1 upper, lower, digit, and speical
# cant be over 20

for password in data:
    l = 0
    u = 0
    d = 0
    s = 0

    failed = 0

    length = len(password)

    for c in password:
        if c.isalpha():
            if c == c.lower():
                l += 1
            if c == c.upper():
                u += 1
        elif c.isdigit():
            d += 1
        else:
            s += 1

    if (length < 8) or (length > 20):
        failed += 1
    if u == 0:
        failed += 1
    if l == 0:
        failed += 1
    if s == 0:
        failed += 1
    if d == 0:
        failed += 1

    if failed == 0:
        text = "Passed all checks!"
    elif failed == 1:
        text = "Failed 1 check"
    else:
        text = "Failed {} checks".format(failed)

    print('Password: ({}) {:20}  Status: {}'.format(format(length, "02"), password[:20], text))
