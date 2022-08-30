#!/usr/bin/env python3
from time import sleep
from ev3dev.ev3 import *
from PIL import Image, ImageDraw, ImageFont  
from smile import *
from text import *
from draw_text import *
lcd = Screen()

#display_smile(lcd)
#display_text()
#display_text_2(lcd, 'hello world')
#display_text_center(lcd, 'hello world')
#wrap_text(lcd, 'this is a very long string :))')
large_font(lcd,'this is a very long string')

# # Write your program here.
# ev3.speaker.beep()
# arc(xy, start, end, fill=None)
# bitmap(xy, bitmap, fill=None)
# chord(xy, start, end, fill=None, outline=None)
# ellipse(xy, fill=None, outline=None)
# line(xy, fill=None, width=0)
# pieslice(xy, start, end, fill=None, outline=None)
# point(xy, fill=None)
# polygon(xy, fill=None, outline=None)
# rectangle(xy, fill=None, outline=None)
# text(xy, text, fill=None, font=None, anchor=None, spacing=0, align="left")
# multiline_text(xy, text, fill=None, font=None, anchor=None, spacing=0, align="left")
# textsize(text, font=None, spacing=0)
# multiline_textsize(text, font=None, spacing=0)

