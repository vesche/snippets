import itertools

data = []
for _ in range(input()):
    data.append(tuple(map(float, raw_input()[1:-1].split(', '))))

control = float('inf')
for a, b in itertools.combinations(data, 2):
    distance = ((a[0]-b[0])**2+(a[1]-b[1])**2)**(.5)
    if distance < control:
        control = distance
        combo = str(a) + ' ' + str(b)

print combo