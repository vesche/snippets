date = raw_input()

try:
    a, b, c = date.split()
    if len(a) == 4:
        y, m, d = a, b, c
    else:
        y, m, d = c, a, b
except: pass

try:
    a, b, c = date.split('/')
    if len(a) == 4:
        y, m, d = a, b, c
    else:
        y, m, d = c, a, b
except: pass

try:
    a, b, c = date.split('-')
    if len(a) == 4:
        y, m, d = a, b, c
    else:
        y, m, d = c, b, a
except: pass

new_line = '20{0}-{1}-{2}'.format(y, m, d)
print new_line
