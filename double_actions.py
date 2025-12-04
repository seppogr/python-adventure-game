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
    old_place_at_first_glance = MainChar.current_place.at_first_glance
    index_of_place_object = MainChar.current_place.directions[direction]
    MainChar.set_current_place(places[index_of_place_object])
    new_place_at_first_glance = MainChar.current_place.at_first_glance

    print_text_slowly(f'You go from {old_place_at_first_glance} into {new_place_at_first_glance}.')

    if MainChar.follower != 'none':
        follower = MainChar.get_follower()
        print_text_slowly(f'The {follower} follows you.')

    check_for_death_by_room(direction)

# handles the go command. requires the direction where to go as parameter
# checks if the door to that direction is locked, and calls changePlace()
# if possible to go to that direction
def go(direction):
    available_directions = MainChar.current_place.directions.keys()
    door_opens_to = MainChar.current_place.door['direction']
    inventory = MainChar.get_inventory()
    door_unlocked = MainChar.current_place.door['open']
    unlocking_item = MainChar.current_place.door['unlocked_by']
    blocker = MainChar.current_place.blocker['name']
    blocker_in_this_direction = MainChar.current_place.blocker['direction']
    road_blocker_status = MainChar.current_place.blocker['blocked']
    follower = MainChar.get_follower()
    follower_who_helps_with_this_block = MainChar.current_place.blocker['unblocked_by']
    message_of_unblocking = MainChar.current_place.blocker['after_message']

    if direction in available_directions:
        if direction == door_opens_to and door_unlocked == False:
            if(unlocking_item in inventory):
                print_text_slowly(f'Your {unlocking_item} unlocks the door!')
                change_place(direction)

            else:
                print_text_slowly(f'The {direction} door is locked. It looks like you need a {unlocking_item} to proceed.')

        elif direction == blocker_in_this_direction and road_blocker_status == True:
            if(follower == follower_who_helps_with_this_block):
                road_blocker_status = False
                print_text_slowly(f'{message_of_unblocking}')
                print_text_slowly('The road is clear!')
                change_place(direction)
            else:
                print_text_slowly(f'There is a {blocker}. It stops you from moving onwards.')
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

    elif character == MainChar.current_place.character:
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
    npc = MainChar.current_place.character
    place_items =  MainChar.current_place.items
    npc_items = npc_data[MainChar.current_place.character]['items']
    char_items = MainChar.get_inventory()

    if noun in place_items or noun in npc_items or noun in char_items:
        print_text_slowly(items[noun]['description'])

    elif noun in npc:
        print_text_slowly(npc_data[noun]['description'])

    else:
        print_text_slowly(f'You glance about the room but there is no {noun} here. You do not find it in your pockets either. You check your hands but they are definitely NOT holding anything even remotely resembling the {noun}')

# remove item from your inventory only if the npc wants that item.
# if so, also adds the item to npc's inventory
def give(item):
    player_inventory = MainChar.get_inventory()
    npc_wants_this_item = npc_data[MainChar.current_place.character]['wants']
    npc_trader_status = npc_data[MainChar.current_place.character]['trader']
    npc_inventory = npc_data[MainChar.current_place.character]['items']
    npc_in_this_place = MainChar.current_place.character
    npc_follower_status = npc_data[MainChar.current_place.character]['follower']

    if item in player_inventory:
        if npc_trader_status == False:
            if item == npc_wants_this_item:
                npc_inventory.append(item)
                room = MainChar.current_place.place_name

                if(MainChar.remove_from_inventory(item)):
                    print_text_slowly(f'{npc_in_this_place.capitalize()} is very happy to get the {item}.')

                    items = MainChar.get_inventory()
                    if npc_follower_status == False:
                        check_for_death_by_item(room, items)

                    else:
                        MainChar.set_follower(npc_in_this_place)
                        npc_in_this_place = None
        else:
            print_text_slowly(f'{npc_in_this_place.capitalize()} does not care for the {item}. Or Maybe they will want to trade instead.')
    else:
        print_text_slowly(f'You rummage and rummage through your bag, but there is no {item} there. You cannot give away what you do not have.' )



def take(item):
    items_in_the_room = MainChar.current_place.items
    item_short_description = items[item]['synonym']

    if item in items_in_the_room:
        MainChar.add_to_inventory(item)
        items_in_the_room.remove(item)
        print_text_slowly(f'You pick up {item_short_description.upper()}.')

    else:
        print_text_slowly(f'Hmmm. You take a long look around and it seems there is no {item} in the room.')

def request(item):
    item_npc_wants_to_keep = npc_data[MainChar.current_place.character]['wants']
    npc = MainChar.current_place.character
    npc_inventory = npc_data[MainChar.current_place.character]['items']
    npc_trader_status = npc_data[MainChar.current_place.character]['trader']

    if item == item_npc_wants_to_keep:
        print_text_slowly(f'{npc.capitalize()} explains: "No! Never in my life shall I part again from this precious {item}!"')

    elif item in npc_inventory and npc_trader_status == False:
        MainChar.add_to_inventory(item)
        npc_inventory.remove(item)
        print_text_slowly(f'You politely inform that the {npc}\'s {item} is required in your investigation. They grudgingly hand it over.')

    elif item in npc_inventory and npc_trader_status == True:
        print_text_slowly(f'The {npc} says: "I could give you the {item}, if you bring me {item_npc_wants_to_keep}."')

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
