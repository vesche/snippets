#!/usr/bin/env python

import socket
import sys

if len(sys.argv) == 2:
    port = int(sys.argv[1])
else:
    print('Usage: ./echoserver.py <port>')
    sys.exit(1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', port))
s.listen(1)

while 1:
    client, address = s.accept()
    data = client.recv(1024)
    if data:
        client.send(data)
    client.close()
