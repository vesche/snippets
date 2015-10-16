#!/usr/bin/python
import optparse

def create_box(height, width):
    for i in range(int(height)):
        print int(width) * '.'

def main():
    p = optparse.OptionParser(description = 'ASCII box creator.',
                              prog        = 'boxify',
                              version     = '0.1',
                              usage       = 'boxify -x <width> -y <height>')
    p.add_option('-x', action='store_true', dest='width', help='width')
    p.add_option('-y', action='store_true', dest='height', help='height')
    opt, arg = p.parse_args()

    if (opt.width is None) or (opt.height is None):
        p.error('One or more mandatory switch options are not defined.')

    create_box(width=arg[0], height=arg[1])

if __name__ == "__main__":
    main()
