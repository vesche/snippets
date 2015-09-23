import random

data = [line.rstrip('\n') for line in open('input.txt')]
grid = [list(('{:%ds}'%(max([len(i) for i in data]))).format(j)) for j in data]
c = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

for i in range(len(grid)):
    new_line = []
    
    for j in range(len(grid[i])):
        n, friends = 0, []
        for case in c:
            a, b = (i + case[0]), (j + case[1])
            if (a >= 0) and (b >= 0):
                try:
                    if grid[a][b] != ' ':
                        n += 1
                        friends.append(grid[a][b])
                except:
                    continue
        
        alive = (grid[i][j] != ' ')
        if alive and (2 <= n <= 3):
            new_line.append(grid[i][j])
        elif not alive and (n == 3):
            new_line.append(random.choice(friends))
        else:
            new_line.append(' ')

    print ''.join(new_line)