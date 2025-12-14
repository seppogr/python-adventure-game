from printer import *
from Player import MainChar
from npcs import *
from utils import *
from Place import *
from Item import *
from idler import *
from death_conditions import *
from proof_manager import *
from points_manager import *
from in_game_messages import in_game_messages as message


# change from one place/room to another, called by go() when needed
def change_place(direction):
    old_place_at_first_glance = MainChar.current_place.at_first_glance
    index_of_place_object = MainChar.current_place.directions[direction]
    MainChar.set_current_place(places[index_of_place_object])
    new_place_at_first_glance = MainChar.current_place.at_first_glance

    print_text_slowly(f'You go from {old_place_at_first_glance} into {new_place_at_first_glance}.')
    if direction == 'smithy':
        proof_list = return_found_proof()
        for proof in proof_list:
            npc_conversation['smith'][proof] = proof_conversation[proof]
    if direction == 'dungeon':
        dungeon_text = open("dungeon.txt")
        print(dungeon_text.read())
        print()
        dungeon_text.close()
    if MainChar.follower != 'none':
        follower = MainChar.get_follower()
        print_text_slowly(f'The {follower.upper()} follows you.')
    check_for_points_gained(direction)
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
    MainChar.current_place.blocker['unblocked_by']
    unblocking_item = fetch_item_object_by_value(MainChar.current_place.blocker['unblocked_by'])


    if direction in available_directions:
        if direction == door_opens_to and door_unlocked == False:
            if(unlocking_item in inventory):
                print_text_slowly(f'Your {unlocking_item.name}{message['unlock_door']}')
                change_place(direction)

            else:
                print_text_slowly(f'The {direction}{message['door_locked_need_a']}{unlocking_item.name}.')

        elif direction == blocker_in_this_direction and road_blocker_status == True:
            unblocking_item = MainChar.current_place.blocker['unblocked_by']
            print(f'You start to go to {direction} but there is a {blocker} that way and...')
            if(follower == follower_who_helps_with_this_block and check_if_follower(unblocking_item)):
                MainChar.current_place.blocker['blocked'] = False
                print_text_slowly(f'{message_of_unblocking}')
                MainChar.set_follower('none')
                print_text_slowly(f'The {follower}{message['follower_leaves']}')
                print_text_slowly(message['can_proceed'])

            elif unblocking_item in MainChar.inventory:
                MainChar.current_place.blocker['blocked'] = False
                print_text_slowly(f'You take your {unblocking_item.name} and use it to {message_of_unblocking}')
                change_place(direction)

            else:
                if MainChar.current_place == Crypt:
                    check_for_death_by_room('crypt')
                else:
                    print_text_slowly(message['cannot_proceed'])
        else:
            change_place(direction)
    else:
        print_text_slowly(f'{direction.upper()}{message['direction_not_available']}')

# launches chat(), takes the current character in the room in as a parameter to be succesful
# otherwise informs the player chat is not possible due to missing chat partner.
# also gives a list of items available for request command and conversation topics for use
# with ask command.
def chat(character):

    if MainChar.get_current_place() == Plaza:
        if character == MainChar.follower:
            print_text_slowly(message['chat_in_plaza'])
        elif character != MainChar.current_place.character:
            print_text_slowly(message['idler_accepts_imaginary_friend'])
        idler_speaks()

    elif character == MainChar.current_place.character:
        print_text_slowly(f'{message['greet_npc']}{character}. He says "{npc_data[character]['greeting']}".')
        print_text_slowly(message['npc_conversation_list'])
        topics = npc_topics(npc_conversation[character].keys())
        print_text_slowly(f'{print_in_colour(topics, BLUE)}')


        if len(npc_data[character]['items']) > 0:
            print_text_slowly(f'{message['notice_npc_items']}{character} is carrying: ')
            npc_items = extract_item_names_from_object_list(npc_data[MainChar.current_place.character]['items'])
            npc_items_string = ''
            for item in npc_items:
                npc_items_string += item + ' '
            print_text_slowly(f'{print_in_colour(npc_items_string, GREEN)}')

    elif character == MainChar.follower:
        topics = npc_topics(npc_conversation[character].keys())
        print_text_slowly(f'{message['chat_with_companion']}{MainChar.follower}')

    else:
        print_text_slowly(f'{message['try_conversation']}{character}{message['npc_unavailable']}')

# asks the current npc about the topics that can be seen with the chat command.
def ask(noun):
    if noun in npc_conversation[MainChar.current_place.character].keys():
        print_text_slowly(f'The {MainChar.current_place.character} says "{npc_conversation[MainChar.current_place.character][noun]}"')

    else:
        print_text_slowly(f'{noun.capitalize()}{message['npc_cannot_answer']}')


# gives a more detailed description of an item or character, depending on the parameter
def describe(noun):
    room_items = extract_item_names_from_object_list(MainChar.current_place.items)
    npc_items = extract_item_names_from_object_list(npc_data[MainChar.current_place.character]['items'])
    a = MainChar.get_inventory()
    character_items = extract_item_names_from_object_list(a)
    item_obj = fetch_item_object_by_value(noun)

    if noun in room_items or noun in npc_items or noun in character_items:
        print_text_slowly(item_obj.description)

    elif noun == MainChar.current_place.character:
        print_text_slowly(npc_data[noun]['description'])

    else:
        print_text_slowly(f'{message['no_item_to_describe']}{noun}.\n{message['no_item_to_describe_cont']}{noun}')

# remove item from your inventory only if the npc wants that item.
# if so, also adds the item to npc's inventory
def give(item):
    player_inventory = MainChar.get_inventory()
    npc_wants_this_item = npc_data[MainChar.current_place.character]['wants']
    npc_trader_status = npc_data[MainChar.current_place.character]['trader']
    npc_inventory = npc_data[MainChar.current_place.character]['items']
    npc_in_this_place = MainChar.current_place.character
    npc_follower_status = npc_data[MainChar.current_place.character]['follower']
    item_obj = fetch_item_object_by_value(item)
    not_interested = f'{npc_in_this_place.capitalize()} is not interested in {item}.'

    if item_obj in player_inventory:
        if npc_trader_status == False:
            if item_obj == npc_wants_this_item:
                npc_inventory.append(item_obj)
                room = MainChar.current_place.place_name
                check_for_points_gained(item)

                if item == 'fish':
                    check_for_points_gained('cat_fed')

                if(MainChar.remove_from_inventory(item_obj)):
                    print_text_slowly(f'{npc_in_this_place.capitalize()}{message['happy_to_get']}{item}.')
                    items = MainChar.get_inventory()
                    if npc_follower_status == False:
                        check_for_death_by_item(room, items)

                    else:
                        MainChar.set_follower(npc_in_this_place)
                        print_text_slowly(f'The {npc_in_this_place.upper()} will help you now.')

                        if npc_in_this_place == 'smith'and Evidence in npc_data[MainChar.current_place.character]['items']:
                            check_for_points_gained('evidence_delivered')
                            MainChar.set_follower('smith')
                            npc_conversation['smith']['evidence'] = proof_conversation['evidence']

                        npc_in_this_place = None
            else:
                print_text_slowly(f'{not_interested}')
        else:
            print_text_slowly(f'{not_interested}{message['npc_could_trade']}')
    else:
        print_text_slowly(f'{message['item_not_in_inventory']}{item}')

# Check if item is available for taking and adds it to player inventory

def take(item):
    items_in_the_room = MainChar.current_place.items
    item_obj = fetch_item_object_by_value(item)
    item_short_description = item_obj.synonym

    if item_obj in items_in_the_room:
        MainChar.add_to_inventory(item_obj)
        items_in_the_room.remove(item_obj)
        print_text_slowly(f'You pick up {item_short_description.upper()}.')
        check_if_proof(item)
        check_for_points_gained(item)

    else:
        print_text_slowly(f'{message['cannot_pick_up']}{item}.')

# check if npc inventory item is available for taking

def request(item):
    item_obj = fetch_item_object_by_value(item)
    item_npc_wants_to_keep = npc_data[MainChar.current_place.character]['wants']
    npc = MainChar.current_place.character
    npc_inventory = npc_data[MainChar.current_place.character]['items']
    npc_trader_status = npc_data[MainChar.current_place.character]['trader']

    if item_obj.name == item_npc_wants_to_keep.name:
        print_text_slowly(f'{npc.capitalize()}{message['npc_refuses_request']}{item}!"')

    elif item_obj in npc_inventory and npc_trader_status == False:
        MainChar.add_to_inventory(item_obj)
        npc_inventory.remove(item_obj)
        print_text_slowly(f'You press on the {npc} to give the {item}.\nIt is now in your possession.')
        check_for_points_gained(item)

    elif item_obj in npc_inventory and npc_trader_status == True:
        print_text_slowly(f'The {npc} says: "I could give you the {item},\nif you bring me {item_npc_wants_to_keep.name}."')

# gey description of an item if it's readable

def read(noun):
    inventory = MainChar.get_inventory()
    item_obj = fetch_item_object_by_value(noun)
    if item_obj in inventory:
        if item_obj.name == 'book':
            print_text_slowly(message['read_book_1'])
            print_text_slowly(message['read_book_2'])

            if Mask in inventory:
                print_text_slowly(message['read_book_with_mask_1'])
                print_text_slowly(message['read_book_with_mask_2'])
                print_text_slowly(message['read_book_with_mask_3'])
                check_for_points_gained('survived_reading_book')
            else:
                check_for_death_by_book()

        elif item_obj.name in readables_as_string:
            print_text_slowly(f'{item_obj.description}')
            check_for_points_gained(noun)

        else:
            print_text_slowly(message['nothing_to_read'])

    else:
        print_text_slowly(message['nothing_to_read'])

# removes item from player inventory and adds it to room inventory

def drop(noun):
    inventory = MainChar.get_inventory()
    item_obj = fetch_item_object_by_value(noun)
    if item_obj in inventory:
        MainChar.current_place.items.append(item_obj)
        MainChar.remove_from_inventory(item_obj)

        if noun == 'symbol' and MainChar.current_place.place_name == 'dungeon':
            check_for_points_gained('game_won')
            print_escape_text()


        else:
            print_text_slowly(f'You drop your {item_obj.name.upper()}{message['drop_success']}')
    else:
        print_text_slowly(f'You try to to drop {item_obj.name.upper()}{message['drop_failure']}')

# Check if player has 4 proof in inventory and if so, removes them and adds Evidence item.
# Otherwise informs how many pieces of proof are missing.

def gather(noun):
    amount_of_proof = amount_of_found_proof()
    if noun == 'evidence' and amount_of_proof < 4:
        print_text_slowly(message['proof_missing'])
        amount_needed = 5 - amount_of_proof
        if amount_needed != 1:
            print_text_slowly(f'{amount_needed}{message['amount_of_proof_missing']}')
        else:
            print_text_slowly(message['proof_missing_just_one'])

    elif noun == 'evidence' and amount_of_proof == 4:
        if Letter in MainChar.get_inventory() and Note in MainChar.get_inventory() and Knife in MainChar.get_inventory() and Rag in MainChar.get_inventory():
            print_text_slowly(message['evidence_success'])
            MainChar.remove_from_inventory(Letter)
            MainChar.remove_from_inventory(Note)
            MainChar.remove_from_inventory(Knife)
            MainChar.remove_from_inventory(Rag)
            MainChar.add_to_inventory(Evidence)
            print_text_slowly(message['evidence_gathered'])
            print_text_slowly(message['evidence_next_step'])
            check_for_points_gained(noun)
        else:
            print_text_slowly(message['evidence_found_but_dropped'])
    else:
        print_text_slowly(f'{message['noun_error_start']}{noun}{message['gather_not_evidence']}')


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
        elif verb == 'read':
            read(noun)
        elif verb == 'drop':
            drop(noun)
        elif verb == 'gather':
            gather(noun)

    except AttributeError:
        print_text_slowly(f'You grow pensive, distracted for a while but the feeling passes.\nYou come to realise there is no {noun} to be found.')
    except KeyError as e:
        print_text_slowly(f'It seems there simply is no {noun} here. {e}')
