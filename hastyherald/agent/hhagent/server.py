import json
import asyncio
import threading

from sanic import Sanic, response
from sanic.websocket import WebSocketProtocol

from hhagent.meta import BANNER
from hhagent.tools import manifest

app = Sanic(name='hhagent')


async def _consumer_handler(ws):
    while True:
        # TODO: do things here interactively
        data = await ws.recv()
        json_data = json.loads(data)

        target_func = None
        command = json_data['command']
        # args = json_data['args']

        if command in manifest:
            target_func = manifest[command]

        if target_func:
            # TODO: comeback to this, fix args
            t = threading.Thread(target=target_func) #, args=[*args.values()])
            t.daemon = True
            t.start()


async def _producer_handler(ws):
    # TODO: send data back to the websocket
    await ws.send('hello')
    await asyncio.sleep(1)


@app.websocket('/hhagent_connect')
async def hhagent_connect(request, ws):
    # TODO: do things here for initial connect

    while True:
        consumer_task = asyncio.ensure_future(_consumer_handler(ws))
        producer_task = asyncio.ensure_future(_producer_handler(ws))
        done, pending = await asyncio.wait(
            [consumer_task, producer_task],
            return_when=asyncio.FIRST_COMPLETED
        )
        for task in pending:
            task.cancel()


def start_server():
    print(BANNER)
    app.run('0.0.0.0', port=1337, protocol=WebSocketProtocol)
