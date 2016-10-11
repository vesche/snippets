#!/usr/bin/env python2
# -*- coding: utf-8 -*-

##################################
# blindscan.py
# https://github.com/vesche
##################################

import random
import socket
import sys


def scan(ip):
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


def main():
    if len(sys.argv) != 2:
        print "Usage: ./blindscan.py <ip>"
    ip = sys.argv[1]
    scan(ip)


if __name__ == "__main__":
    main()
