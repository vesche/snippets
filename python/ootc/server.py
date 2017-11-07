#!/usr/bin/env python2

import socket
import sys

def get_coords():
    with open('data.db') as db:
        d = {}
        for line in db:
            line = line.rstrip()
            _, _, char, coords = line.split(':')
            d[char] = coords
    return str(d)

if __name__ == '__main__':
    try:
        if 0 < int(sys.argv[1]) < 65536:
            pass
        else: raise Exception
    except:
        print 'OotC Server\nUsage: ./server <port>'
        sys.exit(1)

    host, port = '', int(sys.argv[1])

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        print 'Failed to create socket.'
        sys.exit(1)

    s.bind((host, port))
    s.listen(10)

    print 'OotC server started, listening on port {}'.format(port)

    while 1:
        conn, addr = s.accept()
        data = conn.recv(1024)
        if conn:
            if 'get_coords' in data:
                coords = get_coords()
                conn.send(coords)
        #elif 'move_south' in data:
        #        line = data.split('!')[1]
        #        u, p, char, coords = line.split(':')
        #        x, y = coords.split(',')
        #        y += 1
        #        line2 = ':'.join(u,p,char,coords)
        #        with open('data.db', 'rw') as f:
        #            for l in f:
        #                if line == l:
        #                    f.write(line2)
        #                else:
        #                    f.write(l)

    s.close()
