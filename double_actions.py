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
                print_text_slowly(f'Your {unlocking_item.name} unlocks the door!')
                change_place(direction)

            else:
                print_text_slowly(f'The {direction} door is locked. It looks like you need a {unlocking_item.name}.')

        elif direction == blocker_in_this_direction and road_blocker_status == True:
            unblocking_item = MainChar.current_place.blocker['unblocked_by']
            print(f'You start to go to {direction} but there is a {blocker} that way and...')
            if(follower == follower_who_helps_with_this_block and check_if_follower(unblocking_item)):
                MainChar.current_place.blocker['blocked'] = False
                print_text_slowly(f'{message_of_unblocking}')
                MainChar.set_follower('none')
                print_text_slowly(f'The {follower} decides it is time for a rest and leaves. You must go on alone.')
                print_text_slowly('The road ahead is clear!')

            elif unblocking_item in MainChar.inventory:
                MainChar.current_place.blocker['blocked'] = False
                print_text_slowly(f'You take your {unblocking_item.name} and use it to {message_of_unblocking}')
                change_place(direction)

            else:
                if MainChar.current_place == Crypt:
                    check_for_death_by_room('crypt')
                else:
                    print_text_slowly(f'...you cannot get past it. Probably there is something you can do.')
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
        if character == MainChar.follower:
            print_text_slowly('It is impossible to talk to anyone except the village idler. He is simply just everywhere\nin this place at once.')
        elif character != MainChar.current_place.character:
            print_text_slowly('The idler does not mind that you try to talk to somebody who is not here.')
        idler_speaks()

    elif character == MainChar.current_place.character:
        print_text_slowly(f'You greet the {character} politely. He says "{npc_data[character]['greeting']}".')
        print_text_slowly(f'As you carry on with some small talk, it occurs to you that maybe\nyou could ask about: ')
        topics = npc_topics(npc_conversation[character].keys())
        print_text_slowly(f'{print_in_colour(topics, BLUE)}')


        if len(npc_data[character]['items']) > 0:
            print_text_slowly(f'During your conversation, you notice that the {character} is carrying: ')
            npc_items = extract_item_names_from_object_list(npc_data[MainChar.current_place.character]['items'])
            npc_items_string = ''
            for item in npc_items:
                npc_items_string += item + ' '
            print_text_slowly(f'{print_in_colour(npc_items_string, GREEN)}')

    elif character == MainChar.follower:
        topics = npc_topics(npc_conversation[character].keys())
        print_text_slowly(f'You chat with the {MainChar.follower} pleasantly.')

    else:
        print_text_slowly(f'It seems {character} is not here. {MainChar.current_place.character.capitalize()} is\namused when you talk by yourself.')

# asks the current npc about the topics that can be seen with the chat command.
def ask(noun):
    if noun in npc_conversation[MainChar.current_place.character].keys():
        print_text_slowly(f'The {MainChar.current_place.character} says "{npc_conversation[MainChar.current_place.character][noun]}"')

    else:
        print_text_slowly(f'{noun.capitalize()} is something I know nothing about.')


# gives a more detailed description of an item or character, depending on the parameter
def describe(noun):
    room_items = extract_item_names_from_object_list(MainChar.current_place.items)
    npc_items = extract_item_names_from_object_list(npc_data[MainChar.current_place.character]['items'])
    character_items = extract_item_names_from_object_list(MainChar.get_inventory())
    item_obj = fetch_item_object_by_value(noun)

    if noun in room_items or noun in npc_items or noun in character_items:
        print_text_slowly(item_obj.description)

    elif noun in MainChar.current_place.character:
        print_text_slowly(npc_data[noun]['description'])

    else:
        print_text_slowly(f'You glance about the room but there is no {noun} here. You do not find it in your pockets either.\nYou check your hands but they are definitely NOT holding anything even remotely resembling the {noun}')

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
                    print_text_slowly(f'{npc_in_this_place.capitalize()} is very happy to get the {item}.')
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
            print_text_slowly(f'{not_interested}, but could be interested in trading something.')
    else:
        print_text_slowly(f'You rummage and rummage through your bag, but there is no {item} there.\nsYou cannot give away what you do not have.' )



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
        print_text_slowly(f'Hmmm. You take a long look around and it seems there is no {item}\nlying around.')

def request(item):
    item_obj = fetch_item_object_by_value(item)
    item_npc_wants_to_keep = npc_data[MainChar.current_place.character]['wants']
    npc = MainChar.current_place.character
    npc_inventory = npc_data[MainChar.current_place.character]['items']
    npc_trader_status = npc_data[MainChar.current_place.character]['trader']

    if item_obj.name == item_npc_wants_to_keep.name:
        print_text_slowly(f'{npc.capitalize()} explains: "No! Never in my life shall I part again from this precious {item}!"')

    elif item_obj in npc_inventory and npc_trader_status == False:
        MainChar.add_to_inventory(item_obj)
        npc_inventory.remove(item_obj)
        print_text_slowly(f'You press on the {npc} to give the {item}.\nIt is now in your possession.')
        check_for_points_gained(item)

    elif item_obj in npc_inventory and npc_trader_status == True:
        print_text_slowly(f'The {npc} says: "I could give you the {item},\nif you bring me {item_npc_wants_to_keep.name}."')

def read(noun):
    nothing_to_read = 'It appears you have nothing to read.'
    inventory = MainChar.get_inventory()
    item_obj = fetch_item_object_by_value(noun)
    if item_obj in inventory:
        if item_obj.name == 'book':
            print_text_slowly('As you turn the pages it becomes evident that this book was not meant for mortal eyes.')
            print_text_slowly('However, you notice that someone has added notes to the sidelines.')

            if Mask in inventory:
                print_text_slowly('Good thing you managed to slip your welding mask on before reading.')
                print_text_slowly('The notes are a diary of cult meetings and what has been offered to the deity.')
                print_text_slowly('As you read down the list, you see that the last offering is scheduled for\ntoday and it is a human head.')
                check_for_points_gained('survived_reading_book')
            else:
                check_for_death_by_book()

        elif item_obj.name in readables_as_string:
            print_text_slowly(f'{item_obj.description}')
            check_for_points_gained(noun)

        else:
            print_text_slowly(nothing_to_read)

    else:
        print_text_slowly(nothing_to_read)

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
            print_text_slowly(f'You drop your {item_obj.name.upper()} to the ground.\nHopefully nobody comes and takes it in case you need it later!')
    else:
        print_text_slowly(f'You try to to drop {item_obj.name.upper()} but soon\nrealise you do not have it!')

def gather(noun):
    amount_of_proof = amount_of_found_proof()
    if noun == 'evidence' and amount_of_proof < 4:
        print_text_slowly(f'You strongly feel you are on the right track but\nsomething is still needed.')
        amount_needed = 5 - amount_of_proof
        if amount_needed != 1:
            print_text_slowly(f'You think about {amount_needed} more pieces proof should do it.')
        else:
            print_text_slowly(f'Just one more piece of evidence and you could present\nyour case to someone honest.')

    elif noun == 'evidence' and amount_of_proof == 4:
        if Letter in MainChar.get_inventory() and Note in MainChar.get_inventory() and Knife in MainChar.get_inventory() and Rag in MainChar.get_inventory():
            print_text_slowly(f'That is it!')
            MainChar.remove_from_inventory(Letter)
            MainChar.remove_from_inventory(Note)
            MainChar.remove_from_inventory(Knife)
            MainChar.remove_from_inventory(Rag)
            MainChar.add_to_inventory(Evidence)
            print_text_slowly(f'You pack the knife, rag, note and letter tightly into a pack of evidence.')
            print_text_slowly('Now, what to do with this?')
            check_for_points_gained(noun)
        else:
            print_text_slowly('It seems you have dropped something vital somewhere!')
    else:
        print_text_slowly(f'You muse over things, but {noun} has not even circumstantial signifigance\nin finding out what happened to your friend.')


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
