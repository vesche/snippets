#!/usr/bin/env python

import os
import sys

li = []
path = sys.argv[1]

if path[-1] != '/':
    path += '/'

for b in os.listdir(path):
    data = os.popen(path+b).read().rstrip()
    li.append(data)

print 'CWN{' + '_'.join(li) + '}'