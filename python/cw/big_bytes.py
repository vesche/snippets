#!/usr/bin/env python3

import binascii
import sys

with open(sys.argv[1]) as f:
    data = f.read()

n = int(data, 2)
print(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())
