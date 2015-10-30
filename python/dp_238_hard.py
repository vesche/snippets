# unfinished, need to work on reverse solve alg...

def get_dung(data):
    dung = {}
    level, line = (0, 0)
    for raw_line in data:
        if raw_line == '\n':
            line = 0
            level += 1
            continue
        dung[(level, line)] = list(raw_line)
        try: dung[(level, line)].remove('\n')
        except: pass
        line += 1
    return dung

def print_dung(dung):
    for _ in sorted(dung):
        print ''.join(dung[_])

def get_pos(dung):
    up_pos, down_pos = [], []
    for x,y in sorted(dung):
        for i in range(len(dung[x,y])):
            char = dung[x,y][i]
            if char == 'S':
                start_pos = [x,y,i]
            elif char == 'G':
                goal_pos = [x,y,i]
            elif char == 'U':
                up_pos.append([x,y,i])
            elif char == 'D':
                down_pos.append([x,y,i])
    return start_pos, goal_pos, up_pos, down_pos

def reverse_solve(dung, s, g, u, d):
    
    return dung

if __name__ == "__main__":
    data = open('input.txt', 'r').readlines()
    dung = get_dung(data)
    s, g, u, d = get_pos(dung)
    dung = reverse_solve(dung, s, g, u, d)
    print_dung(dung)