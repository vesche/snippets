#!/usr/bin/env python

import random
import socket
import sys
import time

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((sys.argv[1], int(sys.argv[2])))
    
    _ = s.recv(4500)
    
    for i in range(5000):
        print i
        data = s.recv(1024)
        if not data:
            continue
    
        if 'You got it!' in data:
            for line in data.split('\n'):
                if 'CWN' in line:
                    print line
                    sys.exit(0)
        
        r = random.randint(10000,99999)
        s.sendall(str(r)+'\n')
