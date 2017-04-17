#!/usr/bin/env python

import re
import socket
import struct
import sys

with open(sys.argv[1]) as f:
    orig_data = f.read()
    data = orig_data.split()

for i in data:
    try:
        if int(i) > 16777215:
            addr = socket.inet_ntoa(struct.pack("!I", int(i)))
        else: raise
    except:
        continue
    
    orig_data = orig_data.replace(i, addr)

print orig_data