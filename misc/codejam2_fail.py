#!/usr/bin/env python2

import random
import sys
import time

data = open(sys.argv[1]).read().splitlines()
del data[0]

with open('output.txt', 'w') as f:
    for case in range(len(data)):
        S = data[case]
        moves = []

        current_moves = 0
        S_copy = S

        while S_copy != len(S_copy)*'+':


            top = S_copy[:index][::-1]
            bot = S_copy[index:]
            new_top = ""
            for i in top:
                if i == '+':
                    new_top += '-'
                else:
                    new_top += '+'
            S_copy = new_top + bot
            current_moves += 1
            raw_input(S_copy)
        moves.append(current_moves)

        answer = min(moves)
        print 'Case #{}: {}\n'.format(case + 1, answer)
        #f.write('Case #{}: {}\n'.format(case + 1, answer))
