from printer import *
from Player import MainChar
from npcs import npcData
from npcs import npcConversation
from utils import *
from Place import *
from items import items

# shorthand variable, make the code more readable because used a lot
# in functions below
currentNpc = MainChar.currentPlace.character

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
    if character ==  currentNpc:
        printText(f'You greet the {character}. He says "{npcData[character]['greeting']}".')
        printText(f'The {character} chats with you. Some topics pique your interest: ')
        topics = npcTopics(npcConversation[character].keys())
        printText(f'{printInColour(topics, BLUE)}')

        if len(npcData[character]['items']) > 0:
            printText(f'I also have these, if you need: ')
            npcItems = extractList(npcData[character]['items'])
            printText(f'{printInColour(npcItems, GREEN)}')
    else:
        printText(f'It seems {character} is not here. {currentNpc.capitalize()} is amused when you talk by yourself.')

def ask(noun):
    if(noun in npcConversation[currentNpc].keys()):
        printText(f'The {MainChar.currentNpc} says "{npcConversation[currentNpc][noun]}"')
    else:
        printText(f'{noun.capitalize()} is something I know nothing about.')

def describe(noun):
    if noun in currentNpc:
        printText(npcData[noun]['description'])
    elif noun in MainChar.currentPlace.items or noun in npcData[currentNpc]['items']:
        printText(items[noun]['description'])
    else:
        printText(f'You glance about the room but there is no {noun} here.')

def give(item):
    if item in MainChar.inventory:
        if item == npcData[currentNpc]['wants']:
            npcData[currentNpc]['items'].append(item)
            if(MainChar.remove_from_inventory(item)):
                printText(f'{currentNpc.capitalize()} thanks you heartily as you give your {item} away.')
        else:
            printText(f'{currentNpc.capitalize()} does not care for the {item}.')
    else:
        printText(f'You rummage and rummage through your bag, but there is no {item} there. You cannot give away what you do not have.' )

def take(item):
    if item in MainChar.currentPlace.items:
        MainChar.add_to_inventory(item)
        MainChar.currentPlace.items.remove(item)
        printText(f'You add the {item} into your bag.')
    else:
        printText(f'Hmmm. You take a long look around and it seems there is no {item} in the room.')

def request(item):
    if item in npcData[currentNpc]['items']:
        MainChar.add_to_inventory(item)
        npcData[MainChar.currentPlace.character]['items'].remove(item)
        printText(f'You politely inform that the {currentNpc}\'s {item} is required in your investigation. They grudgingly hand it over.')
    else:
        printText(f'The {currentNpc} hastily explains that the {item} is not in their possession.')

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
        elif verb == 'request':
            request(noun)

    except:
        print('stutters down')
