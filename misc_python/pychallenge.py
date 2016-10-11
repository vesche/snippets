#!/usr/bin/env python2
# -*- coding: utf-8 -*-

##################################################################
# http://www.pythonchallenge.com/
# My solutions to the first few challenges before I lost interest.
# https://github.com/vesche
##################################################################

import pickle
import urllib2
import zipfile
from PIL import Image
import ImageDraw
from string import ascii_lowercase


def levelseven():
    load = Image.open('oxygen2.png')
    data = load.tostring()
    data = data.split('\xff')
    return data


def levelsix():
    z = zipfile.ZipFile('channel.zip')
    li = []

    numb = '90052'
    while True:
        try:
            data = z.read('{}.txt'.format(numb))
            numb = data.split()[3]
            li.append(z.getinfo('{}.txt'.format(numb)).comment)
        except:
            print ''.join(li)
            break


def levelfive():
    data = pickle.load(open('banner.p', 'rb'))
    for i in data:
        line = ''
        for j in i:
            line += j[0] * j[1]
        print line


def levelfour(numb):
    while True:
        try:
            response = urllib2.urlopen('http://www.pythonchallenge.com\
            /pc/def/linkedlist.php?nothing={}'.format(str(numb)))
            numb = response.read().split()[5]
            print numb
            response.close()
        except:
            break


def levelthree(blob):
    string = ''
    blob = blob.replace('\n', '')
    for i in range(len(blob)):
        try:
            if blob[i] == blob[i].lower():
                if blob[i+1:i+4] == blob[i+1:i+4].upper():
                    if blob[i+4] == blob[i+4].lower():
                        if blob[i+5:i+8] == blob[i+5:i+8].upper():
                            if blob[i+8] == blob[i+8].lower():
                                string += blob[i+4]
        except:
            break
    return string


def leveltwo(blob):
    chars = {}
    for i in blob:
        if i in chars:
            chars[i] += 1
            continue
        chars[i] = 1
    return chars


def rotn(n, blob):
    decrypted = ''
    letters = ascii_lowercase
    for i in blob:
        try:
            offset = n + letters.index(i)
            if offset >= 25:
                offset -= 26
            blurp = letters[offset]
        except:
            blurp = i
        decrypted += blurp
    return decrypted
