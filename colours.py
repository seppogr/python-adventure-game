"""This is a data storage for different colours and types that
    are available for use in python. Used when calling the
    printInColour(string, colourCode) function. The colourCode
    arguments are the codes below. For example
    printInColour('hello world', RED) returns the string
    'hello world' in red.

    Colour codes from https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
"""

# Colours currently in use
RED    = '\33[31m'
VIOLET = '\33[35m'
BLUE   = '\33[34m'
GREEN  = '\33[32m'
BLACK  = '\33[30m'
YELLOW = '\33[33m'
BEIGE  = '\33[36m'
WHITE  = '\33[37m'

# Background colours currently in use
BLACKBG  = '\33[40m'
REDBG    = '\33[41m'
GREENBG  = '\33[42m'
YELLOWBG = '\33[43m'
BLUEBG   = '\33[44m'
VIOLETBG = '\33[45m'
BEIGEBG  = '\33[46m'
WHITEBG  = '\33[47m'
GREYBG    = '\33[100m'
REDBG2    = '\33[101m'
GREENBG2  = '\33[102m'
YELLOWBG2 = '\33[103m'
BLUEBG2   = '\33[104m'
VIOLETBG2 = '\33[105m'
BEIGEBG2  = '\33[106m'
WHITEBG2  = '\33[107m'
END      = '\33[0m'

idler_colour_list = [BLACKBG, REDBG, GREENBG, YELLOWBG, VIOLETBG, BEIGEBG, WHITEBG, GREYBG, REDBG2, GREENBG2, YELLOWBG2, BEIGEBG2, WHITEBG2]
# below are not in use yet

CBOLD     = '\33[1m'
CITALIC   = '\33[3m'
CURL      = '\33[4m'
CBLINK    = '\33[5m'
CBLINK2   = '\33[6m'
CSELECTED = '\33[7m'




CGREY    = '\33[90m'
CRED2    = '\33[91m'
CGREEN2  = '\33[92m'
CYELLOW2 = '\33[93m'
CBLUE2   = '\33[94m'
CVIOLET2 = '\33[95m'
CBEIGE2  = '\33[96m'
CWHITE2  = '\33[97m'



# def colourString(string, colourCode):
#     return colourCode + string + END

# # Use the code below for testing what output looks like
# print(colourString('hello world', CWHITEBG2))