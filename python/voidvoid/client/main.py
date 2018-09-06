#!/usr/bin/env python

import argparse
import requests

def game_loop(server, username):
    i = input("{username} > ".format(username=username))
    if i.startswith('/'):
        i = i[1:]
    r = requests.get("http://{server}/{uri}".format(server=server, uri=i))
    print(r.text)

# this will be in pygame later
def get_parser():
    parser = argparse.ArgumentParser(description='pygwip')
    parser.add_argument('-s', '--server', help='server ip',
                        required=True, type=str)
    parser.add_argument('-u', '--username', help='username',
                        required=True, type=str)
    return parser

def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    server = args['server']
    username = args['username']

    try:
        r = requests.get("http://{server}/init/{username}".format(
            server=server,
            username=username))
    except requests.exceptions.ConnectionError:
        print("Server not found.")
        return

    while True:
        game_loop(server, username)

if __name__ == "__main__":
    main()