#!/usr/bin/env python3

import sys, getopt
import inkyphat
from PIL import ImageFont, Image
from time import sleep

def image(file):
    inkyphat.clear()
    inkyphat.set_colour('red')
    inkyphat.set_image(Image.open(file))
    inkyphat.show()

def main (argv):
    global font
    file = ""
    try:
        opts, arg = getopt.getopt(argv,"hf:",["file="])
    except getopt.GetoptError:
        print( 'image.py -f <filename> ')
        sys.exit(2)
    for opt, arg in opts:
        print("opt: ", opt)
        print("arg: ", arg)
        if opt == '-h':
            print( 'image.py -f <filename> ')
            sys.exit()
        elif opt in ("-f", "--file"):
            file = arg
    print( 'file is ', file )
    inkyphat.clear()
    inkyphat.set_colour('red')
    image(file)

if __name__ == "__main__":
    main(sys.argv[1:])

