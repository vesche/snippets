#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# evilreplay.py
# https://github.com/vesche
#

import datetime
import os
import readline
import sys


banner = '''
            _ _                _
  _____   _(_) |_ __ ___ _ __ | | __ _ _   _
 / _ \ \ / / | | '__/ _ \ '_ \| |/ _` | | | |
|  __/\ V /| | | | |  __/ |_) | | (_| | |_| |
 \___| \_/ |_|_|_|  \___| .__/|_|\__,_|\__, |
                        |_|            |___/
1. Replay PCAP
2. Read Log
3. About
4. Quit
'''


# converts file size to human readable
# sizeof_fmt function source - http://stackoverflow.com/a/1094933
def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


# prompt user to select interface
def select_int():
    # list interfaces
    interfaces = os.listdir("/sys/class/net")
    print
    for i in range(len(interfaces)):
        interface = interfaces[i]
        print "{}. {}".format(i+1, interface)

    # select interface
    select_int = raw_input("Which interface would you like to use? ")
    try:
        return interfaces[int(select_int)-1]
    except IndexError:
        return "invalid"


def select_speed():
    # list speeds
    speeds = ["half-speed", "normal", "double", "x10", "topspeed"]
    print
    for i in range(len(speeds)):
        speed = speeds[i]
        print "{}. {}".format(i+1, speed)

    # select speed
    select_speed = raw_input("Replay speed? ")
    if select_speed == '1':
        return "--multiplier=0.5"
    elif select_speed == '2':
        return ''
    elif select_speed == '3':
        return "--multiplier=2"
    elif select_speed == '4':
        return "--multiplier=10"
    elif select_speed == '5':
        return "--topspeed"
    else:
        return "invalid"


def replay_pcap(folder):
    # list pcap files
    files = sorted(os.listdir(folder))
    print
    for f in range(len(files)):
        f_name = files[f]
        print "{}. {} ({})".format(f+1, f_name,
        sizeof_fmt(os.path.getsize(folder+'/'+f_name)))

    # select pcap file
    select_file = raw_input("Which pcap file would you like to replay? ")
    try:
        pcap_file = files[int(select_file)-1]
    except IndexError:
        return "Invalid pcap file."

    # select interface
    interface = select_int()
    if interface == "invalid":
        return "Invalid interface."

    # select speed
    speed_option = select_speed()
    if speed_option == "invalid":
        return "Invalid replay speed."

    # replay pcap
    command = "sudo tcpreplay -i {} {} {} > /dev/null 2>&1 &".format( \
    interface, speed_option, folder+'/'+pcap_file)
    os.system(command)

    # log replay
    with open("log.txt", 'a') as log_file:
        log_file.write("{} Replaying {} via {}...\n".format( \
        str(datetime.datetime.now())[:19], pcap_file, interface))

    return "Replaying {}...".format(pcap_file)


def main():
    status = ''

    while True:
        os.system("clear")
        print banner
        if status:
            print status
            status = ''
        menu = raw_input('> ')

        # noop
        if menu == '':
            continue

        if menu == '1':
            status = replay_pcap("pcap")

        elif menu == '2':
            with open("log.txt") as f:
                print f.read()
                raw_input("Press ENTER to continue.")

        elif menu == '3':
            raw_input("evilreplay is a command-line interface for replaying "\
            "traffic files.\n\nPress ENTER to continue.")

        elif menu == '4':
            print "Goodbye!"
            sys.exit(0)


if __name__ == "__main__":
    # check for root
    if os.geteuid() != 0:
        print "This program must be run as root."
        print "Interacting with network interfaces requires root access.\n"
        sys.exit(1)

    # start log
    with open("log.txt", 'w') as f:
        f.write("{} LOG START\n".format(str(datetime.datetime.now())[:19]))

    main()
