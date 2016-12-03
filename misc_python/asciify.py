#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#####################################################################
# asciify.py
# Turns an image into ASCII art.
# Essentially a rewrite of - https://gist.github.com/cdiener/10491632
# https://github.com/vesche
#####################################################################

import sys
from PIL import Image
import numpy as np


def asciify(f):
    scale, factor, wcf = 0.02, 1, 7/4
    chars = np.asarray(list(" .,:;irsXA253hMHGS#9B&@"))
    img = Image.open(f)
    s = (round(img.size[0]*scale*wcf), round(img.size[1]*scale))
    img = np.sum(np.asarray(img.resize(s)), axis=2)
    img -= img.min()
    img = (1.0 - img/img.max())**factor*(chars.size-1)
    return '\n'.join((''.join(r) for r in chars[img.astype(int)]))


def main():
    image_file = sys.argv[1]
    print(asciify(image_file))


if __name__ == "__main__":
    main()
