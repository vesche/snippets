nice_count = 0

with open("input.txt", 'r') as f:
    for s in f.readlines():
        s = s.rstrip()
        nice = True

        # pair occurs twice without overlapping
        pair_count = 0
        for i in range(len(s) - 3):
            pair = s[i:i+2]
            if pair in s[i+2:]:
                pair_count += 1
        if pair_count == 0:
            nice = False

        # letter x letter
        lxl_count = 0
        for i in range(len(s) - 2):
            if s[i] == s[i + 2]:
                lxl_count += 1
        if lxl_count == 0:
            nice = False

        # naughty or nice
        if nice:
            nice_count += 1

print nice_count
