_, sticks = input(), map(int, raw_input().split())
while len(sticks) != 0:
    print len(sticks)
    cut = min(sticks)
    for i in sticks:
        if i == cut:
            sticks = [x for x in sticks if x != cut]
