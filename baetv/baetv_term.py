
import os
from blessed import Terminal

# update auth code here
cmd = 'pyvizio --ip=192.168.1.4:7345 --auth=foo {x} > /dev/null 2>&1 &'
term = Terminal()

s = 0

while True:
    with term.cbreak():
        user_input = term.inkey()

    if user_input == '1':
        os.system(cmd.format(x='volume up'))
    if user_input == '2':
        os.system(cmd.format(x='volume down'))

    if repr(user_input) == 'KEY_UP':
        os.system(cmd.format(x='key-press up2'))
    if repr(user_input) == 'KEY_DOWN':
        os.system(cmd.format(x='key-press down'))
    if repr(user_input) == 'KEY_LEFT':
        os.system(cmd.format(x='key-press left'))
    if repr(user_input) == 'KEY_RIGHT':
        os.system(cmd.format(x='key-press right2'))

    if repr(user_input) == 'KEY_DELETE':
        os.system(cmd.format(x='key-press back'))
    if repr(user_input) == 'KEY_ENTER':
        os.system(cmd.format(x='key-press ok'))
    if user_input == '3':
        os.system(cmd.format(x='mute'))

    if repr(user_input) == 'KEY_TAB':
        if s:
            os.system(cmd.format(x='play'))
            s = 0
        else:
            os.system(cmd.format(x='pause'))
            s = 1
