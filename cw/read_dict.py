#!/usr/bin/env python

import sys
import ast

with open(sys.argv[1]) as f:
    data = f.read().rstrip()

d = ast.literal_eval(data)
d2 = {}

for k,v in d.items():
    d2[int(k)] = v

li = []
for _,v in sorted(d2.items()):
    li.append(v)

for line in ' '.join(li).split('\n'):
    if line:
        print line.strip()