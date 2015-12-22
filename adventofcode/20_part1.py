# break on 36,000,000

houses = dict()
h = 1

while 1:
    for x in range(1000001):
        if int(x) % h == 0:
            try:
                houses[x] += h*10
            except:
                houses[x] = h*10

    for k, v in houses.iteritems():
        if v >= 36000000:
            print k, v
            break

    h += 1
