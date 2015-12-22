santa_data, rsanta_data = '', ''
with open("input.txt", 'r') as f:
    data = f.read()
    for i in range(len(data)):
        if i % 2 == 0:
            santa_data += data[i]
        else:
            rsanta_data += data[i]

def run(li):
    loc = 0
    locations = {0:1}
    for direction in li:
        if direction == '^':
            loc += 1000
        elif direction == 'v':
            loc -= 1000
        elif direction == '>':
            loc += 1
        elif direction == '<':
            loc -= 1
        try:
            locations[loc] += 1
        except:
            locations[loc] = 1
    return locations

santa = run(santa_data)
rsanta = run(rsanta_data)

combine = santa.copy()
combine.update(rsanta)

print len(combine)
