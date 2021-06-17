#!/usr/bin/env python

"""
pyxel library testing <3
https://github.com/vesche
https://github.com/kitao/pyxel/
"""

import pyxel
from random import randint

def clamp(n):
    return max(min(184, n), 0)

class App:
    def __init__(self):
        pyxel.init(200, 200, caption='cat game')
        pyxel.image(0).load(0, 0, 'cat.png')

        self.score = 0
        self.speed = 2
        self.player_x = 100
        self.player_y = 100
        self.facing_left = True
        self.eating = False
        self.eating_frame_count = 4
        self.random_locations = [(randint(0,184), randint(0,184)) for i in range(4)]

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btn(pyxel.KEY_LEFT):
            self.player_x = clamp(self.player_x - self.speed)
            self.facing_left = True
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player_x = clamp(self.player_x + self.speed)
            self.facing_left = False
        if pyxel.btn(pyxel.KEY_UP):
            self.player_y = clamp(self.player_y - self.speed)
        if pyxel.btn(pyxel.KEY_DOWN):
            self.player_y = clamp(self.player_y + self.speed)

        # pick up an apple if close enough
        for location in self.random_locations:
            delta_x, delta_y = tuple(abs(i-j) for i, j in \
                zip((self.player_x, self.player_y), location))

            if delta_x < 10 and delta_y < 10:
                self.score += 10
                self.eating = True
                self.random_locations.remove(location)
                break

    def draw(self):
        # clear screen
        pyxel.cls(5)

        # draw title
        pyxel.text(60, 10, "best cat game ever", 12)

        # draw cat coordinates
        coords = "({}, {})".format(self.player_x, self.player_y)
        pyxel.text(10, 10, coords, 7)

        # draw score
        score = "score: {}".format(self.score)
        pyxel.text(150, 10, score, 7)

        # draw frame count
        frames = "frames: {}".format(pyxel.frame_count)
        pyxel.text(150, 190, frames, 7)

        # draw apples
        for location in self.random_locations:
            x, y = location[0], location[1]
            pyxel.blt(x, y, 0, 16, 0, 16, 16, 5)
        
        # color chart :D
        for i in range(1, 17*10, 10):
            pyxel.text(i, 2, "{}".format(i//10), 2)
            for j in range(10):
                pyxel.pix(i+j, 0, i/10)

        # draw cat
        if self.facing_left:
            m = 1
        else:
            m = -1

        if not self.eating:
            pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 16*m, 16, 5)
            self.hold_frame = pyxel.frame_count
    
        if self.eating:
            if self.hold_frame + self.eating_frame_count > pyxel.frame_count:
                pyxel.blt(self.player_x, self.player_y, 0, 0, 16, 16*m, 16, 5)
            elif self.hold_frame + self.eating_frame_count * 2 > pyxel.frame_count:
                pyxel.blt(self.player_x, self.player_y, 0, 0, 32, 16*m, 16, 5)
            else:
                self.eating = False

App()
