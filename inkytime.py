#!/usr/bin/env python3

import sys, getopt
import inkyphat
from PIL import ImageFont, Image
import time

font = ImageFont.truetype(inkyphat.fonts.FredokaOne,60)

def text(text, colour):
    w, h = font.getsize(text)
    x = (inkyphat.WIDTH / 2) - (w / 2)
    y = (inkyphat.HEIGHT / 2) - (h / 2)
    y -= 10
    inkyphat.text((x, y), text, colour, font)
    inkyphat.show()

def image(file):
    inkyphat.clear()
    inkyphat.set_colour('red')
    inkyphat.set_image(Image.open(file))
    inkyphat.show()

def cleaner():
    colours = (inkyphat.RED, inkyphat.BLACK, inkyphat.WHITE)
    for c in enumerate(colours):
        inkyphat.set_border(c)
        for x in range(inkyphat.WIDTH):
            for y in range(inkyphat.HEIGHT):
                inkyphat.putpixel((x, y), c)
    inkyphat.show()

def main (argv):
    global font
    t = time.strftime("%I:%M")
    inkyphat.clear()
    inkyphat.set_colour("black")
    text(t,inkyphat.BLACK)

if __name__ == "__main__":
    main(sys.argv[1:])

