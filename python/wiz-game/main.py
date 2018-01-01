#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyglet
import sys
from pyglet.window import key

# window = pyglet.window.Window(width=600, height=800, caption="Game Name", resizable=True)

window = pyglet.window.Window(800, 200)
image  = pyglet.image.load("wizard.png")
sprite = pyglet.sprite.Sprite(image)

music = pyglet.resource.media("awake.mp3")
music.play()

@window.event
def on_draw():
    window.clear()
    sprite.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.RIGHT:
        sprite.x += 10
    elif symbol == key.LEFT:
        sprite.x -= 10
    elif symbol == key.Q:
        sys.exit(0)

pyglet.app.run()
