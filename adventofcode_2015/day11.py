#!/usr/bin/env python

from string import ascii_lowercase

password = "hepxcrrq"

def check(password):
    req_one = req_thr = False
    req_two = True

    for tok in [password[i:i+3] for i in range(6)]:
        if tok in ascii_lowercase:
            req_one = True

    for letter in password:
        if letter in ['i', 'o', 'l']:
            req_two = False

    count = 0
    used = []
    for tok in [password[i:i+2] for i in range(0,8,2)]:
        if tok[0] == tok[1] and (tok[0] not in used):
            count += 1
            used.append(tok[0])
    if count >= 2:
        req_thr = True

    if req_one and req_two and req_thr:
        return True
    else:
        return False

col = 0
hold = ''
while True:
    if check(password):
        print(password)
        break

    password = list(password[::-1])

    if hold == 'a':
        col += 1

    letter = password[col]
    ind = ascii_lowercase.index(letter)
    if ind==25: ind=-1
    new_letter = ascii_lowercase[ind + 1]
    password[col] = new_letter

    if col > 0:
        col = 0

    hold = new_letter

    password = ''.join(password)[::-1]
