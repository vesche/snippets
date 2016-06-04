#!/usr/bin/env python2

import ast
import getpass
import os
import socket
import sys
from time import sleep

from common import *

def menu():
    while 1:
        os.system('clear')
        print menu_text
        menu_choice = raw_input('> ')

        if menu_choice == '1':
            return
        elif menu_choice == '2':
            print about_text
            raw_input('Press RETURN to continue...')
        elif menu_choice == '3':
            sys.exit(0)
        else: pass

def login():
    while 1:
        username = raw_input('Username: ')
        password = getpass.getpass()

        user_exists, pass_correct = False, False
        with open('data.db') as db:
            for line in db:
                u, p, char, coords = line.split(':')
                if username == u:
                    user_exists = True
                    if password == p:
                        pass_correct = True
                        break

        if (user_exists == True) and (pass_correct == True):
            return line
        elif (user_exists == True) and (pass_correct == False):
            print 'Password incorrect, try again.'
        else:
            print 'Username doesn\'t exist! Create new account (y/n)?'
            new_user_choice = raw_input()
            if new_user_choice.lower()[0] == 'y':
                print 'ok...'
                # create new user here
            else:
                sys.exit(0)

def game(line):
    host, port = 'localhost', 1337

    s = socket.socket()
    s.connect((host, port))
    grid = list(' '*18)

    while 1:
        s.sendall('get_coords')
        data = s.recv(1024)

        locations = ast.literal_eval(data)
        for c in locations:
            x, y = map(int, locations[c].split(','))
            grid[x+y*6] = c

        print '+------+'
        print '|%s|' % ''.join(grid[:6])
        print '|%s|' % ''.join(grid[6:12])
        print '|%s|' % ''.join(grid[12:18])
        print '+------+'

        move = raw_input('> ')
        #if move == 's':
        #    print line.rstrip()
        #    s.sendall('move_south!%s' % line.rstrip())
        #    sleep(3)
        #    print 'done'

if __name__ == "__main__":
    menu()
    line = login()
    game(line)
