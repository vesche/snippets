#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    data = f.read().splitlines()

def triangle(n_rows):
    results = []
    for _ in range(n_rows): 
        row = [1]
        if results:
            last_row = results[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        results.append(row)
    return results

for line in data:
    row, col = map(int, line.split())
    print triangle(row+1)[-1][col]