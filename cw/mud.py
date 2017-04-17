#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    data = f.read()

print \
(data.count('U') * 2)   + \
(data.count('u'))       + \
(data.count('MH') * 6)  + \
(data.count('mh') * 3)  + \
(data.count('D') * -2)  + \
(data.count('d') * -1)  + \
(data.count('SL') * -6) + \
(data.count('sl') * -3)