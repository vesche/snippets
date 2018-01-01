#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# a.py - Python structure.
#

import sys

def main(argc, argv):
    print('argc: {}, argv: {}'.format(argc, argv))
    return 0

if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv))
