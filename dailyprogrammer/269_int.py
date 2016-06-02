#!/usr/bin/env python

from string import ascii_lowercase, ascii_uppercase

all_letters = ascii_lowercase + ascii_uppercase
top, right = ascii_lowercase[:13], ascii_lowercase[13:]
left, bottom = ascii_uppercase[:13], ascii_uppercase[13:]

move = [-16, 16, -1, 1]

ciphertext = 'TpnQSjdmZdpoohd'
plaintext = ''

if __name__ == '__main__':
    with open('269_int_input.txt') as f:
        data = list(f.read())
    
    for cipherletter in ciphertext:
        if cipherletter in bottom:
            direction = 0
        elif cipherletter in top:
            direction = 1
        elif cipherletter in right:
            direction = 2
        elif cipherletter in left:
            direction = 3
        
        location = data.index(cipherletter)
        
        while True:
            location += move[direction]
            tile = data[location]
            
            if tile in all_letters:
                plaintext += tile
                break
            elif tile == '/':
                direction = 3 - direction
            elif tile == '\\':
                direction ^= 2

    print plaintext
