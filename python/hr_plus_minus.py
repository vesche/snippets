def theshit(x, numbs):
	x = float(x)
	numbs = numbs.split(' ')

	pos, neg, zer = 0, 0, 0

	for n in numbs:
		if n[0] == '-':
			neg += 1
		elif n[0] == '0':
			zer += 1
		else:
			pos += 1

	print '%.3f' % (pos / x)
	print '%.3f' % (neg / x)
	print '%.3f' % (zer / x)

theshit('6', '-2 -1 0 1 2 3')
theshit('12', '-2 -1 0 1 2 3 4 5 6 7 8 9 10')
