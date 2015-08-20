letters = 'abcdefghijklmnopqrstuvwxyz'
cases = input()
for i in range(cases):
    word = raw_input()
    li = []
    for letter in word: li.append(letters.index(letter))
    x = len(li) / 2
    inner, outer = li[0:x], li[::-1][0:x]
    total = 0
    for i in range(len(inner)):
        count = 0
        while inner[i] != outer[i]:
            if inner[i] > outer[i]: inner[i] -= 1
            if outer[i] > inner[i]: outer[i] -= 1
            count += 1
        total += count
    print total
