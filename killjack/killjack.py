#!/usr/bin/env python

#
# killjack - Headphone jack monitor kill-switch.
# https://github.com/vesche
#

import argparse
import os
import sys
import time


def _get_jacks():
    status = []

    # read ALSA card0
    with open('/proc/asound/card0/codec#0') as f:
        for line in f.readlines():
            if 'Power:' in line:
                status.append(line)

    return status


def _preflight_killjack():
    # check for root
    if not os.geteuid() == 0:
        print('Error: This program needs to be run as root.\n')
        sys.exit(1)

    # check for sound card 0 directory
    if not os.path.isdir('/proc/asound/card0'):
        print('Error: Sound card 0 not found.')
        sys.exit(1)

    # check for intel sound card codec file
    if not os.path.exists('/proc/asound/card0/codec#0'):
        print('Error: Sound card 0 codec file not found.')
        sys.exit(1)


def get_parser():
    parser = argparse.ArgumentParser(description='headphone jack monitor kill-switch')
    parser.add_argument('-i', '--interval',
                        help='monitor interval in seconds (default 1 sec)',
                        default=1, type=float)
    parser.add_argument('-t', '--testing',
                        help='testing mode, system will not shutdown',
                        default=False, action='store_true')
    return parser


def run_killjack():
    parser = get_parser()
    args = vars(parser.parse_args())

    sleep_time = args['interval']
    testing_mode = args['testing']

    # ladies and gentlemen this is your captain speaking
    _preflight_killjack()

    # get initial state of jacks
    initial_state = _get_jacks()

    print('killjack is running...')

    # begin monitoring jacks for changes
    while True:
        # get current state of jacks
        current_state = _get_jacks()

        # check if jacks changed state
        if current_state != initial_state:
            if not testing_mode:
                os.system('poweroff -f')
            else:
                print('Alert: A jack has changed state.')

        # pause before repeating
        time.sleep(sleep_time)


if __name__ == '__main__':
    run_killjack()
