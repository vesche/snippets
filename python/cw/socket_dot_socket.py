#!/usr/bin/env python

import socket
import sys

flag = ""
'''
length = None

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], int(sys.argv[2])))

_ = s.recv(1024) # banner
data = s.recv(1024) # init ask

# get length
for line in data.splitlines():
    if 'chars' in line:
        for i in line.split():
            if i.isdigit():
                length = int(i)
s.close()
'''

for n in range(100):
    #success = False
    #while not success:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((sys.argv[1], int(sys.argv[2])))

    _ = s.recv(1024) # banner
    _ = s.recv(1024) # init ask

    n = str(n)
    s.send(n + '\n')

    port_line = s.recv(1024)
    for x in port_line.split():
        x = str(x).strip()
        if x.isdigit():
            port = int(x)

    try:
        s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s2.connect((sys.argv[1], port))
        response = s2.recv(1024)
        flag += str(response.rstrip()).split()[-1]
        # success = True
    except: break

    try:
        s.close()
        s2.close()
    except: pass

print flag
