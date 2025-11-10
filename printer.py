import time
from colours import *

# custom  print() function
# writes a string letter by letter with a slight delay between letters

def printText(string):
    for char in string:
        print(char, end='', flush=True)
        time.sleep(.05)
    print()

def printInColour(string, colourCode):
    return colourCode + string + CEND
