from printer import *
from Player import MainChar
from npcs import npc_data
from npcs import npc_conversation
from utils import *
from Place import *
from items import items
from idler import *
from death_conditions import *

# change from one place/room to another, called by go() when needed
def change_place(direction):
    old_place = MainChar.current_place.at_first_glance
    index_of_place_object = MainChar.current_place.directions[direction]
    MainChar.set_current_place(places[index_of_place_object])
    new_place = MainChar.current_place.at_first_glance
    print_text_slowly(f'You go from {old_place} into {new_place}.')

    if MainChar.follower != 'none':
        print_text_slowly(f'The {MainChar.follower} follows you.')

    check_for_death_by_room(direction)

# handles the go command. requires the direction where to go as parameter
# checks if the door to that direction is locked, and calls changePlace()
# if possible to go to that direction
def go(direction):
    if direction in MainChar.current_place.directions.keys():
        if MainChar.current_place.door['direction'] == direction and MainChar.current_place.door['open'] == False:
            if(MainChar.current_place.door['unlocked_by'] in MainChar.inventory):
                print_text_slowly(f'Your {MainChar.current_place.door['unlocked_by']} unlocks the door!')
                change_place(direction)
            else:
                print_text_slowly(f'The {direction} door is locked. It looks like you need a {MainChar.current_place.door['unlocked_by']} to proceed.')

        elif MainChar.current_place.blocker['direction'] == direction and MainChar.current_place.blocker['blocked'] == True:
            if(MainChar.follower == MainChar.current_place.blocker['unblocked_by']):
                MainChar.current_place.blocker['blocked'] = False
                print_text_slowly(f'{MainChar.current_place.blocker['after_message']}')
                print_text_slowly('The road is clear!')
                change_place(direction)
            else:
                print_text_slowly(f'There is a {MainChar.current_place.blocker['name']}. It stops you from moving onwards.')
        else:
            change_place(direction)
    else:
        print_text_slowly(f'There is no way to reach {direction} from here.')

# launches chat(), takes the current character in the room in as a parameter to be succesful
# otherwise informs the player chat is not possible due to missing chat partner.
# also gives a list of items available for request command and conversation topics for use
# with ask command.
def chat(character):
    if MainChar.get_current_place() == Plaza:
        idler_speaks()

    elif character in MainChar.current_place.character:
        print_text_slowly(f'You greet the {character}. He says "{npc_data[character]['greeting']}".')
        print_text_slowly(f'The {character} chats with you. Some topics pique your interest: ')
        topics = npc_topics(npc_conversation[character].keys())
        print_text_slowly(f'{print_in_colour(topics, BLUE)}')

        if len(npc_data[character]['items']) > 0:
            print_text_slowly(f'I also have these, if you need: ')
            npc_items = extract_list(npc_data[character]['items'])
            print_text_slowly(f'{print_in_colour(npc_items, GREEN)}')
    else:
        print_text_slowly(f'It seems {character} is not here. {MainChar.current_place.character.capitalize()} is amused when you talk by yourself.')

# asks the current npc about the topics that can be seen with the chat command.
def ask(noun):
    if(noun in npc_conversation[MainChar.current_place.character].keys()):
        print_text_slowly(f'The {MainChar.current_place.character} says "{npc_conversation[MainChar.current_place.character][noun]}"')
    else:
        print_text_slowly(f'{noun.capitalize()} is something I know nothing about.')


# gives a more detailed description of an item or character, depending on the parameter
def describe(noun):
    if noun in MainChar.current_place.character:
        print_text_slowly(npc_data[noun]['description'])
    elif noun in MainChar.current_place.items or noun in npc_data[MainChar.current_place.character]['items']:
        print_text_slowly(items[noun]['description'])
    else:
        print_text_slowly(f'You glance about the room but there is no {noun} here.')

# remove item from your inventory only if the npc wants that item.
# if so, also adds the item to npc's inventory
def give(item):
    if item in MainChar.inventory:
        if item == npc_data[MainChar.current_place.character]['wants']:
            npc_data[MainChar.current_place.character]['items'].append(item)
            room = MainChar.current_place.place_name

            if(MainChar.remove_from_inventory(item)):
                print_text_slowly(f'{MainChar.current_place.character.capitalize()} is very happy to get the {item}.')
                items = MainChar.inventory
                if npc_data[MainChar.current_place.character]['follower'] == False:
                    check_for_death_by_item(room, items)
                else:
                    MainChar.set_follower(MainChar.current_place.character)
                    MainChar.current_place.character = None
        else:
            print_text_slowly(f'{MainChar.current_place.character.capitalize()} does not care for the {item}.')
    else:
        print_text_slowly(f'You rummage and rummage through your bag, but there is no {item} there. You cannot give away what you do not have.' )



def take(item):
    if item in MainChar.current_place.items:
        MainChar.add_to_inventory(item)
        MainChar.current_place.items.remove(item)
        print_text_slowly(f'You pick up {items[item]['synonym'].upper()}.')
    else:
        print_text_slowly(f'Hmmm. You take a long look around and it seems there is no {item} in the room.')

def request(item):
    if item == npc_data[MainChar.current_place.character]['wants']:
        print_text_slowly(f'{MainChar.current_place.character} explains: "No! Never in my life shall I part again from this precious {item}!"')
    elif item in npc_data[MainChar.current_place.character]['items']:
        MainChar.add_to_inventory(item)
        npc_data[MainChar.current_place.character]['items'].remove(item)
        print_text_slowly(f'You politely inform that the {MainChar.current_place.character}\'s {item} is required in your investigation. They grudgingly hand it over.')
    else:
        print_text_slowly(f'The {MainChar.current_place.character} hastily explains that the {item} is not in their possession.')

def act_on_double_command(verb, noun):
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
