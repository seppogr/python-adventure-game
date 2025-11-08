from places import places
from Player import player
#from player import Player
from commands import *
import utils
import printer


utils.setPlayerPlace('inn', 0)
utils.showStart()
utils.showStory()



commandInput = input('What will you do?> ').strip().lower()

while commandInput != ('quit'):
    wordCountInCommand = 0
    for item in commandInput.split(" "):
        wordCountInCommand = wordCountInCommand + 1

    listOfCommands = commandInput.split(" ")

    if wordCountInCommand == 1 and commandInput in singleWordCommands:
        if commandInput == 'help':
            printer.printText('GET SOME HELP HERE')
            # aputiedosto = open("demohelp.txt")
            #todo: write the file below properly
            # print(aputiedosto.read())
            # print()
            # aputiedosto.close()

        elif commandInput == 'inventory':
            print(commandInput)



    elif wordCountInCommand == 2:
        verb = listOfCommands[0]
        noun = listOfCommands[1]

        if verb not in commandVerbs:
            print('illegal command VERB')
            #todo early exit if verb not allowed

        try:
            if(verb == 'go' and noun in places[player['placeIndex']]['directions']):
                index = utils.getPlayerPlaceIndex(noun)
                utils.setPlayerPlace(noun, index)
                for direction in places[player['placeIndex']]['directions']:
                    printer.printText(f'Available direction: {direction}')
                utils.showStory()

            # else:
            #     print('Caanot go there from here')

        except:
            print('stutters down')

    else:
       print('illegal command')

    commandInput = input('What will you do?> ').strip().lower()