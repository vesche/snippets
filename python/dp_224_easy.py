import random

def shuff(l):
    s = []
    while len(l) != 0:
        x = random.choice(l)
        s.append(x)
        l.remove(x)
    return ' '.join(s)

print shuff(raw_input().split())
