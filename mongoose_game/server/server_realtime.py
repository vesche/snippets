#!/usr/bin/env python

import rc4
import time
import redis
import asyncio
import threading

from sanic import Sanic
from sanic.websocket import WebSocketProtocol

inc1 = 0
inc2 = 0
app = Sanic(name='new_game')
r = redis.Redis(host='127.0.0.1', port=6379, db=0)

# encryption is hard fuck it man
ENCRYPTION = False


async def _consumer_handler(ws, key):
    global inc2
    ciphertext = await ws.recv()

    if ENCRYPTION:
        plaintext = rc4.decrypt(key, ciphertext)
    else:
        print(ciphertext)

    inc2 += 1
    await asyncio.sleep(.1)


async def _producer_handler(ws, key):
    global inc1
    inc1 += 1
    plaintext = str(inc1) + " testing hello friend :)"
    if ENCRYPTION:
        ciphertext = rc4.encrypt(key, plaintext)
    else:
        ciphertext = plaintext
    await ws.send(ciphertext)
    await asyncio.sleep(.1)


@app.websocket('/test/<username>')
async def test(request, ws, username):
    key = r.get(f'key.{username.lower()}').decode('utf-8')

    while True:
        consumer_task = asyncio.ensure_future(_consumer_handler(ws, key))
        producer_task = asyncio.ensure_future(_producer_handler(ws, key))
        done, pending = await asyncio.wait(
            [consumer_task, producer_task],
            return_when=asyncio.FIRST_COMPLETED,
        )
        for task in pending:
            task.cancel()


def main():
    app.run(host='0.0.0.0', port=1337, protocol=WebSocketProtocol)


if __name__ == '__main__':
    main()
