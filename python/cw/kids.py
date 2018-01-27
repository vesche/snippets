#!/usr/bin/env python3

import os
import subprocess
import sys
from subprocess import DEVNULL

# os.system("./{} &> /dev/null".format(sys.argv[1]))
subprocess.call(["./{}".format(sys.argv[1])], stdout=DEVNULL)
data = os.popen('find / -type f -printf "%T@ %p\n" 2> /dev/null | sort -n | cut -d" " -f 2- | tail -n 10000').read().split()[::-1]

for f in data:
    if not (f.startswith('/sys') or f.startswith('/proc')):
        print(f); break
