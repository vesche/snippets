n = input()

for i in range(n):
    line = raw_input()
    if 'p' in line:
        a = line.index('p')
        break

if (i != 0): out = 'DOWN'
else: out = 'UP'
if (a != 0): out += '\nRIGHT'
else: out += '\nLEFT'

print '\n'.join(out for _ in range(n-2))