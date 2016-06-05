#!/usr/bin/env python

# histstat.py - Netstat history for Linux

import time
from datetime import datetime
from subprocess import check_output

outline = '{:4} {:5} {:5} {:20} {:20} {:5} {:5} {:12} {:5} {:12} {:8} {:10}'

def get_netstat():
    netstat_raw = check_output(['/bin/netstat', '-natup'])
    netstat_lines = netstat_raw[netstat_raw.find('tcp'):].split('\n')
    return netstat_lines

def process(netstat_lines):
    date, time = str(datetime.now()).split()

    for line in netstat_lines:
        line = line.split()
        if len(line) == 7:
            protocol, recvQ, sendQ, local, foreign, state, pidproc = line
            state = state.lower()
        elif len(line) == 6:
            protocol, recvQ, sendQ, local, foreign, pidproc = line
            state = "-"
        else:
            continue
        try:
            l_addr, l_port = local.split(':')
        except:
            l_port = local.split(':')[-1]
            l_addr = local[:local.find(l_port)-1]
        try:
            f_addr, f_port = foreign.split(':')
        except:
            f_port = foreign.split(':')[-1]
            f_addr = foreign[:foreign.find(f_port)-1]
        try:
            pid, proc = pidproc.split('/')
        except:
            pid, proc = '-', '-'
        print outline.format(protocol, recvQ, sendQ, l_addr, f_addr, l_port, \
        f_port, state, pid, proc, time[:8], date)

if __name__ == "__main__":
    # start program
    print outline.format('pro', 'r', 's', 'laddr', 'faddr', 'lport', 'fport', \
    'state', 'pid', 'proc', 'time', 'date')
    netstat_A = get_netstat()
    process(netstat_A)

    # primary loop
    while True:
        time.sleep(1)
        netstat_B = get_netstat()

        for line in netstat_B:
            if line not in netstat_A:
                process([line])

        netstat_A = netstat_B
