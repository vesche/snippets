#!/usr/bin/env python2
# -*- coding: utf-8 -*-

######################################
# Google Code Jam 2016, Counting Sheep
# https://github.com/vesche
######################################

import sys
import time


def main():
    data = map(int, open(sys.argv[1]).read().splitlines())
    del data[0]
    max_time = 1

    with open("output.txt", 'w') as f:
        for case in range(len(data)):
            N = data[case]
            N_current = N

            numbs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            i = 2
            start_time = time.time()

            while (time.time() - start_time < max_time):
                for digit in str(N_current):
                    try:
                        numbs.remove(int(digit))
                    except: pass

                if len(numbs) == 0:
                    answer = N_current
                    break

                N_current = i * N
                i += 1
            else:
                answer = "INSOMNIA"

            f.write("Case #{}: {}\n".format(case + 1, answer))


if __name__ == "__main__":
    main()
