def narc_test(n):
    digits = map(int, list(str(n)))
    if n == sum([_**len(digits) for _ in digits]):
        print n,

for n in range(1000000):
    narc_test(n)