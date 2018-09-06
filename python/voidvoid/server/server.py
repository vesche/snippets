#!/usr/bin/env python

import void

from sanic import Sanic
from sanic.response import json

app = Sanic()
game = void.State()

# from lib import player
# p = player.Player(name="Jackson")

@app.route('/')
async def test(request):
    return json({'hello': 'world'})

@app.route('/init/<username>')
async def init(request, username):
    game.add_player(username)
    return json({"username": username, "init": "success"})

@app.route('/move/<username>/<direction>')
async def move(request, username, direction):
    return json({"coords": })

"""
@app.websocket('/feed')
async def feed(request, ws):
    while True:
        data = json({'a':'b'})
        print('send: ' + data)
        await ws.send(data)
        data = await ws.recv()
        print('recv: ' + data)
"""

@app.websocket('/feed')
async def feed(request, ws):
    while True:
        data = 'hello!'
        print('Sending: ' + data)
        await ws.send(data)
        data = await ws.recv()
        print('Received: ' + data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
