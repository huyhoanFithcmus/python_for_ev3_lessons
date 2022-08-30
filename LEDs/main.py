#!/usr/bin/env python3
from ev3dev2.led import Leds
from time import sleep

leds = Leds()

leds.all_off() # Turn all LEDs off
sleep(1)

# Set both pairs of LEDs to amber
leds.set_color('LEFT', 'AMBER')
leds.set_color('RIGHT', 'AMBER')
sleep(4)

# With custom colors:
leds.set_color('LEFT', (1, 0)) # Bright Red.
leds.set_color('RIGHT', (0, 1)) # Bright green.
sleep(4)

leds.set_color('LEFT', (1, 0.01)) # Does not work correctly
leds.set_color('RIGHT', (0.01, 1)) # Does not work correctly
sleep(4)
