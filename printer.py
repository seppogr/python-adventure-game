import time
from colours import *

print_text_delay = .04
#print_text_delay = .001

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

def print_escape_text():
    print_text_slowly('As you throw the symbol on the floor, something curious happens:')
    print_text_slowly('The symbol shatters into two pieces, and a strong surge of power pulses from the')
    print_text_slowly('exact place where the pieces of the symbol fell from each other. The power')
    print_text_slowly('clearly disrupts the ritual the three robed figures were conducting, and the')
    print_text_slowly('ground starts to shatter. Suddenly, a hole appears in the cavern roof! Sunlight')
    print_text_slowly('starts to stream into the dungeon and, as on cue, you feel it is now or never.')

def print_cat():
    print_text_slowly(print_in_colour(
"""+--------------------+
|  /\___/\ --- MEOW! |
| ( =`.´= )          |
|  (__(,,))___/      |
+--------------------+""",REDBG2))
