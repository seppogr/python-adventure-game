from Player import MainChar
from Place import *
from commands import *
from printer import *
from npcs import npcs
from items import items
from utils import *

currentInteraction = 'default'


printText(f'You are in {MainChar.currentPlace.atFirstGlance}.')

commandInput = input('What will you do?> ').strip().lower()

while commandInput != ('quit'):
    wordCountInCommand = 0
    for item in commandInput.split(" "):
        wordCountInCommand = wordCountInCommand + 1

    listOfCommands = commandInput.split(" ")

    if wordCountInCommand == 1 and commandInput in singleWordCommands:
        if commandInput == 'help':
            printText('GET SOME HELP HERE')
            # aputiedosto = open("demohelp.txt")
            #todo: write the file below properly
            # print(aputiedosto.read())
            # print()
            # aputiedosto.close()
        elif commandInput == 'test':
            currentInteraction = 'innkeeper'
            print(len(npcs[currentInteraction]['items']))
        elif commandInput == 'inventory':
            MainChar.printInventory()

        elif commandInput == 'directions':
            travelDirections = MainChar.currentPlace.directions.keys()
            printText(f'You can go to: ')
            printText(f'{printInColour(extractList(travelDirections), VIOLET)}')

        elif commandInput == 'describe':
            characters = extractList(MainChar.currentPlace.character)
            printText(f'You can see {len(MainChar.currentPlace.character)} characters to talk to here:')
            printText(f'{printInColour(characters, CGREEN)}')
            itemList = extractList(MainChar.currentPlace.items)
            printText(f'The following items are of note: ')
            printText(f'{printInColour(itemList, RED)}')

        else:
            printText('I do not understand that command.')

    elif wordCountInCommand == 2:
        verb = listOfCommands[0]
        noun = listOfCommands[1]

        if verb not in commandVerbs:
            print('illegal command VERB')

        try:
            if(verb == 'go' and noun in MainChar.currentPlace.directions.keys()):
                oldPlace = MainChar.currentPlace.atFirstGlance
                indexOfPlaceObject = MainChar.currentPlace.directions[noun]
                MainChar.set_current_place(places[indexOfPlaceObject])
                newPlace = MainChar.currentPlace.atFirstGlance
                printText(f'You go from {oldPlace} into {newPlace}.')
                currentInteraction = 'default'

            elif(verb == 'describe' and noun in MainChar.currentPlace.character):
                printText(npcs[noun]['description'])

            elif verb == 'chat':
                currentInteraction = noun
                printText(f'You greet the {currentInteraction}. He says "{npcs[currentInteraction]['greeting']}".')
                printText(f'The {currentInteraction} chats with you. Some topics pique your interest: ')
                topics = npcTopics(npcs[currentInteraction].keys())
                printText(f'{printInColour(topics, BLUE)}')

                if len(npcs[currentInteraction]['items']) > 0:
                    printText(f'I also have these, if you need: ')
                    npcItems = extractList(npcs[currentInteraction]['items'])
                    printText(f'{printInColour(npcItems, GREEN)}')

            elif(verb == 'ask'):
                if currentInteraction == 'default':
                    printText(f'Chat with somebody first. It is rude just to ask for things straight out without any small talk.')
                elif(noun in npcs[currentInteraction].keys()):
                    printText(f'The {currentInteraction} say\'s "{npcs[currentInteraction][noun]}"')
                elif(noun in npcs[currentInteraction]['items']):
                    printText(f'{items[noun]['description']}')


            elif(verb == 'describe'):
                if(noun in MainChar.currentPlace.items):
                    printText(items[noun]['description'])
                else:
                    printText(f'You glance around the room, and it seems there is no {noun} visible anywhere. Maybe it is in somebody\'s pocket and you need to ask for it?')
            else:
                printText('I do not understand that command.')

        except:
            print('stutters down')

    else:
       print('illegal command')

    commandInput = input('What will you do?> ').strip().lower()
