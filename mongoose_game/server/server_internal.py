#!/usr/bin/env python

import json
import redis

from sanic import Sanic, response

app = Sanic(name='internal')
r = redis.Redis(host='127.0.0.1', port=6379, db=0)


@app.route('/set_key/<username>/<key>', methods=['GET',])
async def set_key(request, username, key):
    r.set(f'key.{username.lower()}', key)
    return response.text("set")


def main():
    app.run(host='127.0.0.1', port=41337)


if __name__ == '__main__':
    main()
