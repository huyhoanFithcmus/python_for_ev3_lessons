#!/usr/bin/env python3
from time import sleep
from ev3dev.ev3 import *


def display_smile(lcd):
    smile = True

    while True:
        lcd.clear()

        # lcd.draw returns a PIL.ImageDraw handle
        lcd.draw.ellipse(( 20, 20,  60, 60))
        lcd.draw.ellipse((118, 20, 158, 60))

        if smile:
            lcd.draw.arc((20, 80, 158, 100), 0, 180)
        else:
            lcd.draw.arc((20, 80, 158, 100), 180, 360)

        smile = not smile  # toggle between True and False

        # Update lcd display
        lcd.update() # Applies pending changes to the screen.
        # Nothing will be drawn on the lcd screen
        # until this function is called.

        sleep(1)
