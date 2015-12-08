encoded, literal = 0, 0

with open('input.txt') as f:
    lines = f.read().splitlines()

for line in lines:
    extra = 4
    for char in line[1:-1]:
        if char == "\\" or char == '"':
            extra += 1
    
    encoded += len(line) + extra
    literal += len(line)

print encoded - literal