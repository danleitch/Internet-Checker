#!/usr/bin/env python3

import os
import time

# The IP address to ping (Google's DNS server)
ip = "8.8.8.8"

# The command to turn the LED on (May differ on different models)
on_cmd = "echo 1 | sudo tee /sys/class/leds/PWR/brightness >/dev/null"

# The command to turn the LED off (May differ on different models)
off_cmd = "echo 0 | sudo tee /sys/class/leds/PWR/brightness >/dev/null"

# The current LED state (0 for off, 1 for on)
led_state = 0

while True:
    # Ping the IP address and check the result
    result = os.system("ping -c 1 " + ip)
    if result == 0 and led_state == 1:
        # Internet is available and LED is on, turn off the LED
        os.system(off_cmd)
        led_state = 0
    elif result != 0 and led_state == 0:
        # Internet is unavailable and LED is off, turn on the LED
        os.system(on_cmd)
        led_state = 1

    # Wait for 30 seconds before checking again
    time.sleep(30)
