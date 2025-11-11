from printer import *
from Player import MainChar
from utils import *
from colours import *

def test():
    print('test code here')
    print(MainChar.currentPlace.placeName)

def help():
    printText('GET SOME HELP HERE')
        # aputiedosto = open("demohelp.txt")
            #todo: write the file below properly
            # print(aputiedosto.read())
            # print()
            # aputiedosto.close()

def directions():
    travelDirections = MainChar.currentPlace.directions.keys()
    printText(f'You can go to: ')
    printText(f'{printInColour(extractList(travelDirections), VIOLET)}')

def describe():
    printText(f'{MainChar.get_current_place().placeName.upper()}')
    printText(f'{MainChar.get_current_place().description}')
    characters = MainChar.currentPlace.character
    printText(f'You can see {printInColour(characters, GREEN)} here:')
    itemList = extractList(MainChar.currentPlace.items)
    printText(f'The following items are of note: ')
    printText(f'{printInColour(itemList, RED)}')

def actOnSingleCommand(commandInput):
    if commandInput == 'help':
        help()
    elif commandInput == 'test':
        test()
    elif commandInput == 'inventory':
        MainChar.printInventory()
    elif commandInput == 'directions':
        directions()
    elif commandInput == 'describe':
        describe()
    else:
        printText('I do not understand that command.')