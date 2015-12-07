coords = {}

for x in range(1000):
    for y in range(1000):
        coords[(x,y)] = 'off'

def lights(update, a, b, c, d):
    for X in range(int(a), int(c)+1):
        for Y in range(int(b), int(d)+1):
            if update == 'on':
                coords[(X,Y)] = 'on'
            elif update == 'off':
                coords[(X,Y)] = 'off'
            else:
                if coords[(X,Y)] == 'on':
                    coords[(X,Y)] = 'off'
                else:
                    coords[(X,Y)] = 'on'

if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        for i in f.readlines():
            i = i.rstrip().split()
            
            if i[0] == 'turn':
                update = i[1]
                a, b = i[2].split(',')
                c, d = i[4].split(',')
                lights(update, a, b, c, d)
            else:
                update = i[0]
                a, b = i[1].split(',')
                c, d = i[3].split(',')
                lights(update, a, b, c, d)

    count_on = 0
    for i in coords:
        if coords[i] == 'on':
            count_on += 1
    print count_on