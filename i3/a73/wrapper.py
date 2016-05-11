#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This script is a simple wrapper which prefixes each i3status line with custom
# information. It is a python reimplementation of:
# http://code.stapelberg.de/git/i3status/tree/contrib/wrapper.pl
#
# To use it, ensure your ~/.i3status.conf contains this line:
#     output_format = "i3bar"
# in the 'general' section.
# Then, in your ~/.i3/config, use:
#     status_command i3status | ~/i3status/contrib/wrapper.py
# In the 'bar' section.
#
# In its current version it will display the cpu frequency governor, but you
# are free to change it to display whatever you like, see the comment in the
# source code below.
#
# © 2012 Valentin Haenel <valentin.haenel@gmx.de>
#
# This program is free software. It comes without any warranty, to the extent
# permitted by applicable law. You can redistribute it and/or modify it under
# the terms of the Do What The Fuck You Want To Public License (WTFPL), Version
# 2, as published by Sam Hocevar. See http://sam.zoy.org/wtfpl/COPYING for more
# details.

import sys
import json
import subprocess

def get_governor():
    """ Get the current governor for cpu0, assuming all CPUs use the same. """
    with open('/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor') as fp:
        return fp.readlines()[0].strip()

def get_memory():
    """ Get memory """
    return subprocess.getoutput("LANG=C /usr/bin/free -m | awk 'NR==2{print $7}'")

def get_battery():
    """ Get battery """
    bat = int(subprocess.getoutput("cat /proc/apm | awk '{print $7}' | rev | cut -c 2- | rev"))
    cha = int(subprocess.getoutput("cat /proc/apm | awk '{print $4}' | cut -c 3-"))
    col = '#00FF00'
    sts = '\N{WHITE CIRCLE}'
    if bat < 60: col = '#FFFF00'
    if bat < 40: col = '#FF0000'
    if cha == 1: sts = '\N{BLACK CIRCLE}'
    return bat, sts, col

def get_volume():
    """ Get volume """
    return subprocess.getoutput("amixer get Master | egrep -o '[0-9]+%' | egrep -o '[0-9]*'")

def get_frequency():
    try:
        freq = int(subprocess.getoutput("cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq"))
        return round(freq / float(1000000), 1)
    except:
        return "meme"

def get_net():
    data = subprocess.getoutput("ifstat wlan0 -t 15 | grep wlan0")
    rx = subprocess.getoutput("echo '" + data + "' | awk '{print $6}'")
    tx = subprocess.getoutput("echo '" + data + "' | awk '{print $8}'")
    rx_int = 0
    tx_int = 0
    if rx.endswith('K'):
        rx_int = int(rx[:-1]) * 1024
    else:
        rx_int = int(rx)
    if tx.endswith('K'):
        tx_int = int(tx[:-1]) * 1024
    else:
        tx_int = int(tx)
    return round(rx_int / float(1024), 1), round(tx_int / float(1024), 1)

def print_line(message):
    """ Non-buffered printing to stdout. """
    sys.stdout.write(message + '\n')
    sys.stdout.flush()

def read_line():
    """ Interrupted respecting reader for stdin. """
    # try reading a line, removing any extra whitespace
    try:
        line = sys.stdin.readline().strip()
        # i3status sends EOF, or an empty line
        if not line:
            sys.exit(3)
        return line
    # exit on ctrl-c
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    # Skip the first line which contains the version header.
    print_line(read_line())

    # The second line contains the start of the infinite array.
    print_line(read_line())

    while True:
        line, prefix = read_line(), ''
        # ignore comma at start of lines
        if line.startswith(','):
            line, prefix = line[1:], ','

        j = json.loads(line)
        # insert information into the start of the json, but could be anywhere
        # CHANGE THIS LINE TO INSERT SOMETHING ELSE
        # j.insert(0, {'full_text' : '%s' % get_governor(), 'name' : 'gov'})
        rx, tx = get_net()
        j.insert(0, {'full_text' : '\N{DOWNWARDS ARROW} %s KB' % rx, 'name' : 'net', 'color' : '#60FF60'})
        j.insert(1, {'full_text' : '\N{UPWARDS ARROW} %s KB' % tx, 'name' : 'net', 'color' : '#FF6060'})
        j.insert(0, {'full_text' : '%s GHz' % get_frequency(), 'name' : 'freq'})
        j.insert(0, {'full_text' : '%sM free' % get_memory(), 'name' : 'mem'})
        bat, sta, col = get_battery()
        j.insert(5, {'full_text' : '%s %s' % (sta, bat), 'name' : 'bat', 'color' : '%s' % col})
        j.insert(5, {'full_text' : '\N{EIGHTH NOTE} %s' % get_volume(), 'name' : 'vol'})
        # and echo back new encoded json
        print_line(prefix+json.dumps(j))
