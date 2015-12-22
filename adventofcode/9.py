import sys
import itertools

places = set()
links = dict()

with open('input.txt') as f:
    lines = f.read().splitlines()

for line in lines:
    locA, _, locB, _, distance = line.split()
    places.add(locA)
    places.add(locB)
    
    # bruteforce
    links.setdefault(locA, dict())[locB] = int(distance)
    links.setdefault(locB, dict())[locA] = int(distance)

shortest = sys.maxsize
longest = 0
for i in itertools.permutations(places):
    d = sum(map(lambda x, y: links[x][y], i[:-1], i[1:]))
    shortest = min(shortest, d)
    longest = max(longest, d)

print "shortest: {}".format(shortest)
print "longest: {}".format(longest)