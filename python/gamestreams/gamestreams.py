#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
gamestreams.py
https://github.com/vesche
"""

import sys
import m3u8
import urllib
import argparse
import platform
import subprocess

if sys.version < '3':
    print('Error: Python 3.x is required to run.')
    sys.exit(1)

__version__ = '0.0.1'

def check_stream(stream_link):
    try:
        m3u8_obj = m3u8.load(stream_link)
        return True
    except urllib.error.HTTPError:
        return False

def start_vlc(stream_link):
    plat = platform.system().lower()

    if plat.startswith('linux') or plat.startswith('darwin'):
        try:
            subprocess.Popen(['vlc', stream_link])
        except FileNotFoundError:
            return 'Error: VLC not found.'
    elif plat.startswith('win'):
        try:
            subprocess.Popen(['C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe', stream_link])
        except FileNotFoundError:
            pass
        try:
            subprocess.Popen(['C:\\Program Files\\VideoLAN\\VLC\\vlc.exe', stream_link])
        except FileNotFoundError:
            return 'Error: VLC not found.'
    else:
        return 'Error: Unsupported platform.'

    return 'Stream has been closed or ended.'

def get_parser():
    parser = argparse.ArgumentParser(description='history for netstat')
    parser.add_argument('-s', '--stream', help='stream link', type=str)
    parser.add_argument('-v', '--version', help='display the current version',
                        default=False, action='store_true')
    return parser

def main():
    parser = get_parser()
    args = vars(parser.parse_args())

    if args['version']:
        print(__version__)
        sys.exit(0)

    stream_link = args['stream']

    if not check_stream(stream_link):
        print('Error: Stream not found.')
        sys.exit(1)

    print( start_vlc(stream_link) )

if __name__ == '__main__':
    main()
