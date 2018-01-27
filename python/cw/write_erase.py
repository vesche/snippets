#!/usr/bin/env python

import socket
import sys

shit = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], int(sys.argv[2])))
data = s.recv(128)

while data:
    data = s.recv(128)
    try:
        data = str(data).split()
        for x in data:
            shit.append(x)
    except: pass

for i in shit[::-1]:
    if ('CWN' in i) and ('}' in i):
        print i
        break
