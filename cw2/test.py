#!/usr/bin/env python

import sys
import zlib

#with open(sys.argv[1]) as f:
#    data = f.read().splitlines()

OFFSET = 0xd9a
SIZE   = 0xd7f
DSIZE  = 0x33486
d = open(sys.argv[1], "rb").read()[OFFSET:OFFSET+SIZE]

for m in [ "\x78\x01", "\x78\x9C", "\x78\xDA" ]:
    try:
        o = zlib.decompressobj().decompress(m + d, DSIZE)
        open("out.%.2x%.2x" % (ord(m[0]), ord(m[1])), "wb").write(o)
    except:
        pass