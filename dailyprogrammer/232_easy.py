#!/usr/bin/env python2
# -*- coding: utf-8 -*-

###########################
# dailyprogrammer 232 easy
# https://github.com/vesche
###########################

from string import ascii_lowercase as letters


def main():
	s = ''
	for i in range(input()):
		for letter in raw_input():
			letter = letter.lower()
			if letter in letters:
				s += letter

	if s == s[::-1]:
		print "Palindrome"
	else:
		print "Not a palindrome"


if __name__ == "__main__":
	main()
