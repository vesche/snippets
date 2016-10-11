# -*- coding: utf-8 -*-

##################################
# dailyprogrammer 211 intermediate
# https://github.com/vesche
##################################


def ogre_maze(swamp):
    swamp = list(swamp.replace('\n', ''))
    good = ['.', '&', '@', '$']

    for i in range(len(swamp)):
        try:
            if (swamp[i] in good) and (swamp[i+1] in good) \
            and (swamp[i+10] in good) and (swamp[i+11] in good):
                swamp[i:i+2] = ['&', '&']
                swamp[i+10:i+12] = ['&', '&']
        except IndexError:
            continue

    for i in range(len(swamp)):
        if i % 10 == 0:
            print ''.join(swamp[i:i+10])
