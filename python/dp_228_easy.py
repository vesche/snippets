import string

letters = string.ascii_uppercase

def sauce(word):
    order = []

    for i in word:
        order.append(letters.index(i))

    if order == sorted(order, key=int):
        return "IN ORDER"
    if order == sorted(order, key=int, reverse=True):
    	return "REVERSE ORDER"
    else:
        return "NOT IN ORDER"

def main():
    f = open('input.txt')

    for word in f.read().splitlines():
        print word, sauce(word.upper())

if __name__ == "__main__":
    main()