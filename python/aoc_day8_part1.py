literal, actual = 0, 0

with open('input.txt') as f:
    lines = f.read().splitlines()

for line in lines:
    literal += len(line)
    actual  += len(eval(line))

print literal - actual