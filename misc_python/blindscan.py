#!/usr/bin/env python2

import random
import socket
import sys


def main(ip):
    ports = [21, 22, 53, 80, 443, 445, 8080]
    random.shuffle(ports)

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip, port))

        try:
            banner = s.recv(1024).rstrip()
        except socket.error:
            banner = ''

        if result == 0:
            state = "open"
        else:
            state = "closed"

        print "{:>5}/tcp {:>7} {}".format(port, state, banner)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: ./blindscan.py <ip>"
    ip = sys.argv[1]
    main(ip)
