#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    data = filter(lambda a: a != '', f.read().splitlines())

for line in data:
    line = line.lstrip('1')
    
    if not line:
        print 'False'
        continue
    
    zero_count = 0
    one_count = 0
    state = ''
    status = True
    
    for n in line:
        if n == '0':
            if state == '1':
                if zero_count != one_count:
                    status = 'False'
                    break
            
            state = '0'
            zero_count += 1
        
        if n == '1':
            state = '1'
            one_count += 1
    
    if zero_count != one_count:
        print 'False'
    else:
        print 'True'