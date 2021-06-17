"""hhagent.cli"""

import argparse

from hhagent.meta import VERSION
from hhagent.server import start_server


def get_parser():
    parser = argparse.ArgumentParser(description='hhagent')
    parser.add_argument(
        '-s', '--server', help='start the server',
        default=False, action='store_true'
    )
    parser.add_argument(
        '-v', '--version', help='display the current version',
        default=False, action='store_true'
    )
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())

    if args['version']:
        print(VERSION)

    if args['server']:
        start_server()


if __name__ == '__main__':
    main()
