from places import places
from player import player
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

    print(wordCountInCommand)
    listOfCommands = commandInput.split(" ")

    if wordCountInCommand == 1 and commandInput == 'apua':
        printer.printText('GET SOME HELP HERE')
            # aputiedosto = open("demohelp.txt")
            #todo: write the file below properly
            # print(aputiedosto.read())
            # print()
            # aputiedosto.close()

    elif wordCountInCommand == 1 and commandInput == 'inventory':
        print(commandInput)

    elif wordCountInCommand == 1:
        print(commandInput)

    elif wordCountInCommand == 2:
        verb = listOfCommands[0]
        noun = listOfCommands[1]
        print(f'{verb} + {noun}')
        #todo early exit if verb not allowed

    try:
        if(verb == 'go' and noun in places[player['placeIndex']]['directions']):
            index = utils.getPlayerPlaceIndex(noun)
            utils.setPlayerPlace(noun, index)
            print(f'lssgo {noun}')
            utils.showStory()
        else:
            print('Caanot go there from here')

    except:
        print('stutters down')

    commandInput = input('What will you do?> ').strip().lower()