"""This is a data storage for different colours and types that
    are available for use in python. Used when calling the
    printInColour(string, colourCode) function. The colourCode
    arguments are the codes below. For example
    printInColour('hello world', RED) returns the string
    'hello world' in red.

    Colour codes from https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
"""

# the colour code variables without 'C' are in use elsewhere in the program
RED    = '\33[31m'
VIOLET = '\33[35m'
BLUE   = '\33[34m'
GREEN  = '\33[32m'
END      = '\33[0m'

# below are not in use yet

CBOLD     = '\33[1m'
CITALIC   = '\33[3m'
CURL      = '\33[4m'
CBLINK    = '\33[5m'
CBLINK2   = '\33[6m'
CSELECTED = '\33[7m'

CBLACK  = '\33[30m'

CYELLOW = '\33[33m'
CBEIGE  = '\33[36m'
CWHITE  = '\33[37m'

CBLACKBG  = '\33[40m'
CREDBG    = '\33[41m'
CGREENBG  = '\33[42m'
CYELLOWBG = '\33[43m'
CBLUEBG   = '\33[44m'
CVIOLETBG = '\33[45m'
CBEIGEBG  = '\33[46m'
CWHITEBG  = '\33[47m'

CGREY    = '\33[90m'
CRED2    = '\33[91m'
CGREEN2  = '\33[92m'
CYELLOW2 = '\33[93m'
CBLUE2   = '\33[94m'
CVIOLET2 = '\33[95m'
CBEIGE2  = '\33[96m'
CWHITE2  = '\33[97m'

CGREYBG    = '\33[100m'
CREDBG2    = '\33[101m'
CGREENBG2  = '\33[102m'
CYELLOWBG2 = '\33[103m'
CBLUEBG2   = '\33[104m'
CVIOLETBG2 = '\33[105m'
CBEIGEBG2  = '\33[106m'
CWHITEBG2  = '\33[107m'

# def colourString(string, colourCode):
#     return colourCode + string + END

# # Use the code below for testing what output looks like
# print(colourString('hello world', CWHITEBG2))