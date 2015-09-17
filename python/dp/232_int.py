import itertools

data, combos, distances = [], [], []

for _ in range(input()):
    data.append(tuple(map(float, raw_input()[1:-1].split(', '))))

for a, b in itertools.combinations(data, 2):
    combos.append(str(a)+' '+str(b))
    distances.append(((a[0]-b[0])**2+(a[1]-b[1])**2)**(.5))

print combos[distances.index(min(distances))]