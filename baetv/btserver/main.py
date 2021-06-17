#!/usr/bin/env python

import os
from sanic import Sanic, response

app = Sanic(name='btserver')
# update auth code here
cmd = '~/.local/bin/pyvizio --ip=192.168.1.4:7345 --auth=foo {x} > /dev/null 2>&1 &'

@app.route('/power')
async def power(request):
    os.system(cmd.format(x='power'))
    return response.text('OK')

@app.route('/vol_up')
async def volume_up(request):
    os.system(cmd.format(x='volume up'))
    return response.text('OK')

@app.route('/vol_down')
async def volume_down(request):
    os.system(cmd.format(x='volume down'))
    return response.text('OK')

@app.route('/mute')
async def mute(request):
    os.system(cmd.format(x='mute'))
    return response.text('OK')

@app.route('/up')
async def up(request):
    os.system(cmd.format(x='key-press up2'))
    return response.text('OK')

@app.route('/down')
async def down(request):
    os.system(cmd.format(x='key-press down'))
    return response.text('OK')

@app.route('/left')
async def left(request):
    os.system(cmd.format(x='key-press left'))
    return response.text('OK')

@app.route('/right')
async def right(request):
    os.system(cmd.format(x='key-press right2'))
    return response.text('OK')

@app.route('/play')
async def play(request):
    os.system(cmd.format(x='play'))
    return response.text('OK')

@app.route('/pause')
async def pause(request):
    os.system(cmd.format(x='pause'))
    return response.text('OK')

@app.route('/home')
async def plex(request):
    os.system(cmd.format(x='key-press home'))
    return response.text('OK')

@app.route('/back')
async def back(request):
    os.system(cmd.format(x='key-press back'))
    return response.text('OK')

@app.route('/ok')
async def ok(request):
    os.system(cmd.format(x='key-press ok'))
    return response.text('OK')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=54880)
