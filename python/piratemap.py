import random

m = ['']
tiles = ['|', '/', '\\', '_']
small_islands = random.randint(1,4)

def display():
    print "{0}{1}{2}".format(' ', '_'*80, ' ')
    print "{0}{1}{2}".format('/', ' '*80, '\\')
    for i in range(1,41):
        print "{0}{1}{2}".format('|', ''.join(m[i]), '|')
    print "{0}{1}{2}".format('\\', '_'*80, '/')

def insert(x, y, foo):
    m[y][x] = foo

if __name__ == "__main__":
    for i in range(1,41):
        m.append(list(' '*80))
    
    # refs, delete later
    insert(10,  5, '+') # NW
    insert(10, 35, '+') # NE
    insert(70,  5, '+') # SW
    insert(70, 35, '+') # SE
    
    insert(20, 10, '.') # NW
    insert(20, 30, '.') # NE
    insert(60, 10, '.') # SW
    insert(60, 30, '.') # SE
    
    # random corners
    nw_x = random.randint(10, 20)
    nw_y = random.randint( 5, 10)
    ne_x = random.randint(60, 70)
    ne_y = random.randint( 5, 10)
    sw_x = random.randint(10, 20)
    sw_y = random.randint(30, 35)
    se_x = random.randint(60, 70)
    se_y = random.randint(30, 35)
    
    insert(nw_x, nw_y, '/')
    insert(ne_x, ne_y, '\\')
    insert(sw_x, sw_y, '\\')
    insert(se_x, se_y, '/')
    
    tmp_x = ne_x
    tmp_y = ne_y
    tmp_t = '/'
    for i in range(tmp_x):
        tmp_x -= 1
        while 1:
            hop = random.choice([-1, 1])
            tmp_y += hop
            if tmp_y > 5:
                break
        if '/' == tmp_t and hop == 1:
            tmp_t = random.choice(['_', '|'])
        elif '\\' == tmp_t and hop == -1:
            tmp_t = random.choice(['\\', '|'])
        elif '|' == tmp_t and hop == -1:
            tmp_t = '\\'
        elif '|' == tmp_t and hop == 1:
            tmp_t = '/'
        else:
            tmp_x -= 1
        insert(tmp_x, tmp_y, tmp_t)
    
    
    display()