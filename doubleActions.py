from printer import *
from Player import MainChar
from npcs import npcs
from utils import *
from Place import *
from items import items



def go(direction):
    oldPlace = MainChar.currentPlace.atFirstGlance
    indexOfPlaceObject = MainChar.currentPlace.directions[direction]
    MainChar.set_current_place(places[indexOfPlaceObject])
    newPlace = MainChar.currentPlace.atFirstGlance
    printText(f'You go from {oldPlace} into {newPlace}.')

def chat(character):
    if character in MainChar.currentPlace.character:
        printText(f'You greet the {character}. He says "{npcs[character]['greeting']}".')
        printText(f'The {character} chats with you. Some topics pique your interest: ')
        topics = npcTopics(npcs[character].keys())
        printText(f'{printInColour(topics, BLUE)}')

        if len(npcs[character]['items']) > 0:
            printText(f'I also have these, if you need: ')
            npcItems = extractList(npcs[character]['items'])
            printText(f'{printInColour(npcItems, GREEN)}')
    else:
        printText(f'It seems {character} is not here. {MainChar.currentPlace.character.capitalize()} is amused when you talk by yourself.')

def ask(noun):
    if(noun in npcs[MainChar.currentPlace.character].keys()):
        printText(f'The {MainChar.currentPlace.character} says "{npcs[MainChar.currentPlace.character][noun]}"')
    else:
        printText(f'{noun.capitalize()} is something I know nothing about.')

def describe(noun):
    if noun in MainChar.currentPlace.character:
        printText(npcs[noun]['description'])
    elif noun in MainChar.currentPlace.items or noun in npcs[MainChar.currentPlace.character]['items']:
        printText(items[noun]['description'])
    else:
        printText(f'You glance about the room but there is no {noun} here.')

def actOnDoubleCommand(verb, noun):
    try:
        if(verb == 'go' and noun in MainChar.currentPlace.directions.keys()):
            go(noun)
        elif verb == 'describe':
            describe(noun)
        elif verb == 'chat':
            chat(noun)
        elif(verb == 'ask'):
            ask(noun)

    except:
        print('stutters down')
