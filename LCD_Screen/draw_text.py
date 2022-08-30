#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

def display_text_2(lcd, myString):
    lcd = Screen()
    lcd.draw.rectangle((0,0,177,40), fill='black')
    lcd.draw.text((48,13),myString, fill='white')
    lcd.draw.text((36,80),myString)
    lcd.update()
    sleep(6)

def display_text_center(lcd, mystring):
    lcd.clear()
    size = lcd.draw.textsize(mystring) # returns a tuple
    lcd.draw.text((20, 20), 'textsize = '+str(size))
    # screen height = 128 pixels, so vertical center is
    # at 64 pixels, so place text (height 11 pixels) at
    # 5 pixels above the center, at 59
    lcd.draw.text((89-size[0]/2, 59), mystring)
    lcd.update()
    sleep(10)

def wrap_text(lcd, mystring):
    newstring=''
    for i in range(len(mystring)):
        # len(mystring) gives the number of characters
        newstring = newstring+mystring[i]
        if i%30 == 29:  # modulo, or remainder after division
            newstring = newstring+'\n'
            # \n is the new line character

    lcd.clear()
    lcd.draw.text((0,0), newstring)
    lcd.update()
    sleep(10)

def large_font(lcd, myString):
    f = ImageFont.truetype('arial.ttf', 75)
    lcd.draw.text((3,0), myString, font=f)
    lcd.update()

    sleep(7)  # if run from Brickman, need time to see displayed image