total = 0

with open("input.txt", 'r') as f:
    for present in f.readlines():
        dim = [l, w, h] = map(int, present.split('x'))
        ribbon = 2*sorted(dim)[0] + 2*sorted(dim)[1]
        bow = l*w*h
        present_total = ribbon + bow
        total += present_total

print total
