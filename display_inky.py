import colorsys
import signal
import time
from sys import exit
import six
from math import floor
from PIL import ImageFont

import inkyphat

def display_data(data):
    font_file = inkyphat.fonts.FredokaOne

    top = 0
    left = 0
    offset_left = 5

    text_lines= ["Ada's Adventures in Science","Backers {}".format(data['backers']),"{} - {:.1f}%".format(data['pledged'], data['percent'])]
    font = inkyphat.ImageFont.truetype(font_file, 20)
    for text in text_lines:
        width, height = font.getsize(text)
        inkyphat.text((0, top), text, 1, font=font)
        top += height + 1
    inkyphat.show()
    return

def display_happy(filename):
    inkyphat.set_border(inkyphat.BLACK)
    inkyphat.set_image(Image.open(filename))

    inkyphat.show()
    return
