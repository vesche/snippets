#!/usr/bin/env python

import random
import requests

from sanic import Sanic, response
from string import ascii_lowercase as alphabet

app = Sanic(name='login')

# TEMP
CREDS = [
    {'username': 'jackson', 'password': 'toortoor'},
    {'username': 'crystal', 'password': 'catnip'}
]


def gen_random_key(length=16):
    """
    Returns a random n-length comprised of the 26 letters of the alphabet.
    Default is 16 characters in length.
    """
    return ''.join([random.choice(alphabet) for _ in range(length)])


@app.route('/login/<username>/<password>', methods=['GET',])
async def login(request, username, password):
    if {'username': username, 'password': password} in CREDS:
        key = gen_random_key()
        # send key to realtime server for rc4...
        # print(key)
        requests.get(f'http://127.0.0.1:41337/set_key/{username.lower()}/{key}')
        return response.text("success:" + key)
    else:
        return response.text("failure:gtfo")


def main():
    app.run(host='0.0.0.0', port=8123)


if __name__ == '__main__':
    main()
