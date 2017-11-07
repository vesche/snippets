#!/usr/bin/env python

import socket
import sys
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], int(sys.argv[2])))
s.settimeout(1)

while True:
    data = s.recv(1024)
    try:
        n = data.rstrip().split()[-1]
    except: continue
    
    try:
        s.sendall(str(int(n)+1)+'\n')
    except:
        print n
        break
