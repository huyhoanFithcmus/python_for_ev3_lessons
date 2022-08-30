#!/usr/bin/env python3
# from ev3dev.ev3 import *   # NOT NEEDED
from time import sleep
import os

def display_text():
    os.system('setfont Lat15-TerminusBold14')
    # os.system('setfont Lat15-TerminusBold32x16')  # Try this larger font
    # A full list of fonts can be found with `ls /usr/share/consolefonts`

    print('EV3 Python rules!')
    print()  # print a blank line

    print('EV3', 'Python rules!')  # comma means continue on same line

    # By default, the invisible parameter 'end' is the new line character
    print('EV3')    # A new line will be started after this
    print('Python rules!')

    # Here the 'end' parameter is replaced
    # with an empty string so no new line is begun
    print('EV3', end='')
    print('Python rules!')

    # Here the 'end' parameter is replaced
    # with a space character so no new line is begun
    print('EV3', end=' ')
    print('Python rules!')

    sleep(15)  # display the text long enough for it to be seen