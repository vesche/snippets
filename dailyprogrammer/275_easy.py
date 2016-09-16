#!/usr/bin/env python

from string import ascii_lowercase
from itertools import product

def test(element, symbol):
    print "%s, %s ->" % (element, symbol),
    try:
        index_a = element.lower().index(symbol[0].lower())
        index_b = element.lower().rindex(symbol[1].lower())
        if index_a < index_b:
            print "true"
        else:
            raise
    except:
            print "false"

def bonus1(element):
    e_chop = element[:-1].lower()
    index_a = e_chop.rindex(''.join(sorted(e_chop))[0])
    e_chop = element[index_a+1:]
    index_b = e_chop.rindex(''.join(sorted(e_chop))[0]) + index_a + 1
    symbol = element[index_a].upper() + element[index_b]
    print "%s -> %s" % (element, symbol)

def bonus2(element):
    pairs = list(set([''.join(i) for i in product(element, repeat=2)]))
    for p in pairs:
        if element.index(p[0]) < element.index(p[1]):
            continue
        else:
            pairs.remove(p)
    print pairs
    print "%s -> %s" % (element, str(len(pairs)))

if __name__ == "__main__":
    test("Spenglerium", "Ee")
    test("Zeddemorium", "Zr")
    test("Venkmine", "Kn")
    test("Stantzon", "Zt")
    test("Melintzum", "Nn")
    test("Tullium", "Ty")

    bonus1("Gozerium")
    bonus1("Slimyrine")

    bonus2("Zuulon")
