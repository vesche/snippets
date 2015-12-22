import string

s = ''
alpha = string.ascii_lowercase

for i in range(input()):
	for letter in raw_input():
		letter = letter.lower()
		if letter in alpha:
			s += letter

if s == s[::-1]:
	print "Palindrome"
else:
	print "Not a palindrome"