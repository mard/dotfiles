#!/bin/sh
# set CPU frequency configuration
echo ondemand > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
echo 80 > /sys/devices/system/cpu/cpufreq/ondemand/up_threshold
echo 10 > /sys/devices/system/cpu/cpufreq/ondemand/sampling_down_factor

# enable CPU freq reading
chmod 444 /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq

# enable suspend
chmod 666 /sys/power/state

