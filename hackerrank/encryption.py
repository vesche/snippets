import math

STDIN = raw_input()
rows = int(math.floor(math.sqrt(len(STDIN))))
cols = int(math.ceil(math.sqrt(len(STDIN))))
li = []

for i in range(len(STDIN)):
    if i % cols == 0:
        try:    li.append(STDIN[i:i+cols])
        except: li.append(STDIN[i:])

blob = []
for i in range(len(li[0])):
    blob.append('')

for i in range(len(li)):
    for j in range(len(li[i])):
        blob[j] += li[i][j]

print ' '.join(blob)
