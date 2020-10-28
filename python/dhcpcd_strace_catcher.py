#!/usr/bin/env python

import os
import time
import psutil

def check_for_dhcpcd():
    return [p.pid for p in psutil.process_iter() if 'dhcpcd' in p.name()]

while True:
    pids = check_for_dhcpcd()
    if pids:
        break
    time.sleep(0.01)

for pid in pids:
    os.system(f'strace -p {pid} 2> {pid}_strace.txt &')
    print(f'[+] Running strace on {pid}...')

input('Press ENTER to stop...')
os.system('pkill strace')
