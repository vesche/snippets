line = list(''.join(raw_input().split()))
score = 0

for i in range(len(line)):
    if line[i] == 'X':
        line[i] = 10
    elif line[i] == '-':
        line[i] = 0
    elif line[i] == '/':
        continue
    else:
        line[i] = int(line[i])

for x in range(len(line)):
    ball = line[x]
    if len(line) - 3 <= x:
        if ball == '/':
            score += (10 - line[x-1])
        else:
            score += ball
        continue
    elif ball == 10:
        score += ball
        score += line[x+1]
        if line[x+2] == '/':
            score += (10 - line[x+1])
        else:
            score += line[x+2]
    elif ball == '/':
        score += (10 - line[x-1])
        score += line[x+1]
    else:
        score += ball

print score
