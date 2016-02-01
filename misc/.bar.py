#!/usr/bin/env python2

# minimal lemonbar script by vesche

import os
import time

def read_cmd(cmd):
    return os.popen(cmd).read()

# funcs
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
    return 'vesche@c720'

def wrk():
    w_query = read_cmd('bspc query -T').split()
    w1, w2, w3, w4 = '1', '2', '3', '4'
    try:
        if w_query[w_query.index('I')+6]    == '*': w1 = 'x'
        if w_query[w_query.index('II')+6]   == '*': w2 = 'x'
        if w_query[w_query.index('III')+6]  == '*': w3 = 'x'
        if w_query[w_query.index('IV')+6]   == '*': w4 = 'x'
    except: pass
    return 'WRK: {0} {1} {2} {3}'.format(w1, w2, w3, w4)

# pipe bar
def main():
    line = [wrk(), usr(), bat(), brt(), net(), day(), clk()]
    return ' | '.join(line)

if __name__ == "__main__":
    while True:
        os.system('buf=\"{0}\"; echo -e $buf'.format(main()))
        time.sleep(1)
