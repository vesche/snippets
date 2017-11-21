#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#
# hackerrank, time-conversion
# https://github.com/vesche
#


def main():
	line = raw_input()
	h, m, x = line.split(':')
	s, t, h = x[0:2], x[2:4], int(h)

	if t == "PM":
		if h == 12:
            h = 12
		else:
            h += 12
	else:
		if h == 12:
            h = 0
		if h < 10:
            h = '0' + str(h)

	print ':'.join([str(h), m, s])


if __name__ == "__main__":
	main()
