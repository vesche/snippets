import random

options = ['UP', 'LEFT', 'DOWN', 'RIGHT']

def main():
    #get input
    m = []
    m.append(raw_input())
    m.append(raw_input())
    m.append(raw_input())
    m.append(raw_input())

    #grab inputs
    up    = m[1][1]
    left  = m[2][0]
    right = m[2][2]
    down  = m[3][1]

    #grab sights
    up_left    = m[1][0]
    up_right   = m[1][2]
    down_left  = m[3][0]
    down_right = m[3][2]

    moves  = [up, down, left, right]
    sights = [up_left, up_right, down_left, down_right]

    #EVENT 1 - if exit in moves
    if 'e' in moves:
        case = moves.index('e')
        if case == 0: return 'UP'
        if case == 1: return 'DOWN'
        if case == 2: return 'LEFT'
        if case == 3: return 'RIGHT'

    #EVENT 2 - if exit in sights
    if 'e' in sights:
        case = sights.index('e')
        if case == 0:
            if left == '#': return 'UP'
            else: return 'LEFT'
        if case == 1:
            if right == '#': return 'UP'
            else: return 'RIGHT'
        if case == 2:
            if left == '#': return 'DOWN'
            else: return 'LEFT'
        if case == 3:
            if right == '#': return 'DOWN'
            else: return 'RIGHT'

    else:
        if up == '-':
            return 'UP'
        if right == '-':
            return 'RIGHT'
        if left == '-':
            return 'LEFT'

print main()
