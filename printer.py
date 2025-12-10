import time
from colours import *

print_text_delay = .001

# custom print() function
# writes a string letter by letter with a slight delay between letters
# defined in print_text_delay variable

def print_text_slowly(string):
    for char in string:
        print(char, end='', flush=True)
        time.sleep(print_text_delay)
    print()

# adds desired colour to the input string. Colour codes are stored in the # colours.py file
def print_in_colour(string, colour_code):
    return colour_code + string + END

def print_a_line_of_stars(colour):
    print(print_in_colour(80 * '*', colour))




