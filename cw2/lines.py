#!/usr/bin/env python
import sys
with open(sys.argv[1]) as f:print' '.join(filter(lambda a:a!='',f.read().splitlines()))