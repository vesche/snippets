number = input()
print number,

divisor_sum = 0
for i in range(1, number+1):
	if number % i == 0:
		divisor_sum += i

if divisor_sum < number * 2:
	print "deficient"
elif divisor_sum > number * 2:
	abundancy = divisor_sum - number * 2
	print "abundant by", abundancy
else:
	print "neither"