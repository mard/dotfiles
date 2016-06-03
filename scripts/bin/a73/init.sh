#!/bin/sh
# set CPU frequency governor configuration
echo conservative > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor

# enable CPU freq reading
chmod 444 /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq

# enable suspend
chmod 666 /sys/power/state

