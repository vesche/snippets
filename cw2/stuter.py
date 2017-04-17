#!/usr/bin/env python

import sys
from itertools import groupby

with open(sys.argv[1]) as f:
    data = f.read().splitlines()

for line in data:
    print ' '.join([a for a,b in groupby(line.split())])