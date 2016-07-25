#!/usr/bin/env python

from datetime import datetime
from psutil import net_connections
from time import sleep
from sys import version_info

line = "{:<15} {:<5} {:<15} {:<5} {:<11} {:<5} {:<8} {:<10}"

def process(c):
    date, time = str(datetime.now()).split()

    _, _, _, laddr, raddr, status, pid = c

    laddr, lport = laddr

    if raddr:
        raddr, rport = raddr
    else:
        raddr, rport = '', ''

    if not status:
        status = ''

    if not pid:
        pid = ''

    print(line.format(laddr, lport, raddr, rport, status, pid, time[:8], date))

def main():
    print(line.format('laddr', 'lport', 'raddr', 'rport', 'status', 'pid', \
    'time', 'date'))

    connections_A = net_connections()

    for c in connections_A:
        process(c)

    while True:
        sleep(1)
        connections_B = net_connections()

        for c in connections_B:
            if c not in connections_A:
                process(c)

        connections_A = connections_B

if __name__ == "__main__":
    main()
