import colorsys
import signal
import time
from sys import exit
import six
from math import floor

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    exit("This script requires the pillow module\nInstall with: sudo pip install pillow")

import unicornhathd

def display_data(data):
    width, height = unicornhathd.get_shape()
    num_pix = width*height

    unicornhathd.rotation(90)
    unicornhathd.brightness(0.5)

    width, height = unicornhathd.get_shape()

    percent = floor(data['percent']*num_pix)
    for x in range(width):
        for y in range(height):
            pix = x * width + y
            if pix < percent:
                unicornhathd.set_pixel(x, y, 255,255,255)
            else:
                unicornhathd.set_pixel(x, y, 0,0,0)
    unicornhathd.show()
    time.sleep(5)
    unicornhathd.off()
    return


def display_text(data):
    text = "{} from {} backers = {}%!".format(data['pledged'], data['backers'], data['percent'])

    colours = [tuple([int(n * 255) for n in colorsys.hsv_to_rgb(x/1.0, 1.0, 1.0)]) for x in range(1)]

    FONT = ("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 12)

    unicornhathd.rotation(0)
    unicornhathd.brightness(1.0)

    width, height = unicornhathd.get_shape()

    text_x = width
    text_y = 2


    font_file, font_size = FONT

    font = ImageFont.truetype(font_file, font_size)

    text_width, text_height = width, 0

    w, h = font.getsize(text)
    text_width += w + width
    text_height = max(text_height,h)

    text_width += width + text_x + 1

    image = Image.new("RGB", (text_width,max(16, text_height)), (0,0,0))
    draw = ImageDraw.Draw(image)

    offset_left = 0

    draw.text((text_x, text_y), text, colours[index], font=font)

    for scroll in range(text_width - width):
        for x in range(width):
            for y in range(height):
                pixel = image.getpixel((x+scroll, y))
                r, g, b = [int(n) for n in pixel]
                unicornhathd.set_pixel(width-1-x, y, r, g, b)

        unicornhathd.show()
        time.sleep(0.01)

    unicornhathd.off()
    return

def display_happy(filename):

    unicornhathd.rotation(90)
    unicornhathd.brightness(0.5)

    width, height = unicornhathd.get_shape()

    img = Image.open(filename)

    valid = False
    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((y, x))
            r, g, b = int(pixel[0]),int(pixel[1]),int(pixel[2])
            if r or g or b:
                valid = True
            unicornhathd.set_pixel(x, y, r, g, b)
    if valid:
        unicornhathd.show()
        time.sleep(5)
        unicornhathd.off()
    return
