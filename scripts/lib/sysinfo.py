import sys
import json
import subprocess

def get_governor():
    """ Get the current governor for cpu0, assuming all CPUs use the same one. """
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
