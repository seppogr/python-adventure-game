from printer import *
from Player import MainChar
from npcs import npcs
from utils import *
from Place import *
from items import items

def changePlace(direction):
    oldPlace = MainChar.currentPlace.atFirstGlance
    indexOfPlaceObject = MainChar.currentPlace.directions[direction]
    MainChar.set_current_place(places[indexOfPlaceObject])
    newPlace = MainChar.currentPlace.atFirstGlance
    printText(f'You go from {oldPlace} into {newPlace}.')

def go(direction):
    if direction in MainChar.currentPlace.directions.keys():
        if MainChar.currentPlace.door['direction'] == direction and MainChar.currentPlace.door['open'] == False:
            if(MainChar.currentPlace.door['unlockedBy'] in MainChar.inventory):
                printText(f'Your {MainChar.currentPlace.door['unlockedBy']} unlocks the door!')
                changePlace(direction)
            else:
                printText(f'The {direction} door is locked. It looks like you need a {MainChar.currentPlace.door['unlockedBy']} to proceed.')
        else:
            changePlace(direction)
    else:
        printText(f'There is no way to reach {direction} from here.')

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

def give(item):
    if item in MainChar.inventory:
        if item == npcs[MainChar.currentPlace.character]['wants']:
            npcs[MainChar.currentPlace.character]['items'].append(item)
            if(MainChar.remove_from_inventory(item)):
                print(f'{MainChar.currentPlace.character.capitalize()} thanks you heartily as you give your {item} away.')
        else:
            printText(f'{MainChar.currentPlace.character.capitalize()} does not care for the {item}.')
    else:
        printText(f'You rummage and rummage through your bag, but there is no {item} in there. You cannot give away what you do not have.' )

def take(item):
    if item in MainChar.currentPlace.items:
        MainChar.add_to_inventory(item)
        MainChar.currentPlace.items.remove(item)
        printText(f'You add the {item} into your bag.')
    else:
        printText(f'Hmmm. You take a long look around and it seems there is no {item} in the room.')


def actOnDoubleCommand(verb, noun):
    try:
        if verb == 'go':
            go(noun)
        elif verb == 'describe':
            describe(noun)
        elif verb == 'chat':
            chat(noun)
        elif verb == 'ask':
            ask(noun)
        elif verb == 'give':
            give(noun)
        elif verb == 'take':
            take(noun)

    except:
        print('stutters down')
