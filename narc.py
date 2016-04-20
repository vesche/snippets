def narc_test(n):
    digits = map(int, list(str(n)))
    if n == sum([i**len(digits) for i in digits]):
        print n,

if __name__ == "__main__":
    for n in range(1000000):
        narc_test(n)
