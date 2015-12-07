import itertools

nice_count = 0

with open("input.txt", 'r') as f:
    for s in f.readlines():
        s = s.rstrip()
        nice = True

        # pair occurs twice without overlapping
        pair_count = 0
        for i in range(len(s)):
            li = []
            pair = s[i:i+2]
            dupe = s[:i]+s[i+2:]
            for j in range(len(dupe)):
                li.append(dupe[j:j+2])
            li.append(pair)
            if li.count(pair) >= 2:
                pair_count += 1
        if pair_count == 0:
            nice = False

        # letter x letter
        count = 0
        for i in range(len(s)):
            triple = s[i:i+3]
            if len(triple) == 3:
                if triple[0] == triple[2]:
                    count += 1
        if count < 1:
            nice = False

        # naughty or nice
        if nice:
            nice_count += 1

print nice_count
