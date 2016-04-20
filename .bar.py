#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# bar.py - minimal lemonbar script by vesche

from os import popen, system
from time import sleep

def read_cmd(cmd):
    return popen(cmd).read()

# bar funcs
def bat():
    bat_c = read_cmd('cat /sys/class/power_supply/BAT0/capacity').rstrip('\n')
    bat_s = read_cmd('cat /sys/class/power_supply/BAT0/status').rstrip('\n')
    if bat_s == 'Charging': bat_o = '+'
    else:                   bat_o = '-'
    return 'BAT: {0}{1}%'.format(bat_o, bat_c)

def brt():
    bscale  = int(read_cmd('cat /sys/class/backlight/intel_backlight/brightness'))
    brt_up  = (bscale / 100 + 1) * '#'
    brt_dwn = (10 - (bscale / 100 + 1)) * '.'
    return 'BRT: {0}{1}'.format(brt_up, brt_dwn)

def clk():
    mil_time = read_cmd('date').split()[3]
    return 'CLK: {0}'.format(mil_time)

def day():
    date_data = read_cmd('date').split()
    day, month, day_n = date_data[0:3]
    return 'DAY: {0}, {1} {2}'.format(day, month, day_n)

def net():
    net_name = read_cmd('iwconfig wlp1s0').split()[3].split(':')[1].strip('"')
    return 'NET: {0}'.format(net_name)

def usr():
    username = read_cmd('whoami').rstrip()
    hostname = read_cmd('hostname').rstrip()
    return 'USR: {0}@{1}'.format(username, hostname)

# pipe bar
def main():
    line = [usr(), bat(), brt(), net(), day(), clk()]
    return ' | '.join(line)

if __name__ == "__main__":
    while True:
        system('buf=\"%%{c}%s\"; echo -e $buf' % main())
        sleep(1)
