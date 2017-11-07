#!/usr/bin/env python

import socket
import sys
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], int(sys.argv[2])))
s.settimeout(1)

prompt = s.recv(1024)

a, b = map(int, prompt.split()[-1].split('-'))

for i in range(a, b+1):
    s.sendall(str(i)+'\n')
    
    data = s.recv(1024)
    
    if data != prompt:
        print data
        break