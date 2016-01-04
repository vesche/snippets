import os
import shutil

def parse(i, f):
    line = i.split()
    if line[1] == "->":
        try:    a = int(line[0])
        except: pass
        try:    a = signals[line[0]]
        except: pass
        try:    signals[line[2]] = a
        except: f.write(i + '\n')

    elif line[0] == "NOT":
        try:    a = abs(~int(line[1]))
        except: pass
        try:    a = abs(~signals[line[1]])
        except: pass
        try:    signals[line[3]] = 65536 - a
        except: f.write(i + '\n')
    else:
        try:    a = int(line[0])
        except: pass
        try:    a = signals[line[0]]
        except: pass
        try:    b = int(line[2])
        except: pass
        try:    b = signals[line[2]]
        except: pass
        try:
            if      line[1] == "AND":       signals[line[4]] = a & b
            elif    line[1] == "OR":        signals[line[4]] = a | b
            elif    line[1] == "LSHIFT":    signals[line[4]] = a << b
            elif    line[1] == "RSHIFT":    signals[line[4]] = a >> b
        except: f.write(i + '\n')

def main():
    shutil.copy("07_input.txt", "tmp.txt")

    while True:
        instructions = open("tmp.txt", 'r').read().splitlines()
        if not instructions:
            break

        with open("tmp.txt", 'w') as f:
            for i in instructions:
                parse(i, f)

    for s in sorted(signals):
        if s == 'a':
            return signals[s]

if __name__ == "__main__":
    signals = {}
    print main()

    # cleanup
    os.remove("tmp.txt")
