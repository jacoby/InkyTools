#!/usr/bin/env python3

import sys, getopt

import inkyphat
from PIL import ImageFont, Image
from time import sleep

font = ImageFont.truetype(inkyphat.fonts.FredokaOne,60)

def text(text, colour):
    w, h = font.getsize(text)
    x = (inkyphat.WIDTH / 2) - (w / 2)
    y = (inkyphat.HEIGHT / 2) - (h / 2)
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
    fontsize = ""
    entry = ""
    try:
        opts, arg = getopt.getopt(argv,"he:f:",["entry=","fontsize="])
    except getopt.GetoptError:
        print( 'argv.py -f <fontsize> -e <entry>')
        sys.exit(2)
    for opt, arg in opts:
        print("opt: ", opt)
        print("arg: ", arg)
        if opt == '-h':
            print( 'argv.py -f <fontsize> -e <entry>')
            sys.exit()
        elif opt in ("-e", "--entry"):
            entry = arg
        elif opt in ("-f", "--fontsize"):
            fontsize = int(arg)
    print( 'font size is ', fontsize )
    print( 'entry is ', entry )
    font = ImageFont.truetype(inkyphat.fonts.FredokaOne,fontsize)
    inkyphat.clear()
    inkyphat.set_colour('red')
    text(entry,inkyphat.BLACK)

if __name__ == "__main__":
    main(sys.argv[1:])
