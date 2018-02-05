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

    text_lines= ["Backers {}".format(data['backers']),"{} - {}%".format(data['pledged'], data['percent'])]

    inkyphat.show()
    return

def display_happy(filename):
    inkyphat.set_border(inkyphat.BLACK)
    inkyphat.set_image(Image.open(filename))

    inkyphat.show()
    return
