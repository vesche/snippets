#!/usr/bin/env python

import os
import sys
import time
from stat import S_ISREG, ST_CTIME, ST_MTIME, ST_MODE

dirpath = sys.argv[1]

entries = (os.path.join(dirpath, fn) for fn in os.listdir(dirpath))
entries = ((os.stat(path), path) for path in entries)

entries = ((stat[ST_CTIME], stat[ST_MTIME], path)
          for stat, path in entries if S_ISREG(stat[ST_MODE]))

flen = max([len(i) for i in os.listdir(dirpath)])
print '{:<{x}}  {:<24}  {:<24}'.format('FILENAME', 'MODIFIED TIME', 'CREATION TIME', x=flen).rstrip()

for cdate, mdate, path in sorted(entries)[::-1]:
    if flen < 8:
        flen = 8
    
    print '{:<{x}}  {}  {}'.format(os.path.basename(path), time.ctime(mdate), time.ctime(cdate), x=flen)
