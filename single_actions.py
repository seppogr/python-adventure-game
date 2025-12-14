import pprint
from printer import *
from Player import MainChar
from utils import *
from colours import *
from commands import *
from death_conditions import *
from Item import *
from proof_manager import proof
from points_manager import *
from in_game_messages import in_game_messages as message

# in game test command used in testing.
# atm prints out the dictionary from where player points are tracked.
def test():
    print('Congrats, you found the secret! Can you find the other one?')
    print('The table below keepd track of the points gained during the game')
    pprint.pp(points_gained)


# Try this if the cat is your follower
def secret():
    if MainChar.follower == 'cat':
        print_text_slowly(message['cat_photo'])
        print_cat()
    else:
        print_text_slowly(message['idler_and_cat'])

# open the help file
def help():
    help_file = open("help.txt")
    print(help_file.read())
    print()
    help_file.close()

# show available traveling directions to player
def directions():
    travel_directions = MainChar.current_place.directions.keys()
    number_of_directions =len(travel_directions)
    if number_of_directions == 1:
        print_text_slowly(message['the_only_way'])
    else:
        print_text_slowly(message['travel_directions'])

    print_text_slowly(f'{print_in_colour(extract_list(travel_directions), VIOLET)}')

# Describe the room the player is in
def describe():
    print_text_slowly(f'{MainChar.get_current_place().description}')
    if MainChar.current_place.character == '' and MainChar.follower != 'none':
        print_text_slowly(f'{message['no_npc_in_room_with_companion']}{MainChar.follower}.')
    elif MainChar.current_place.character == '':
        print_text_slowly(message['no_npc_in_room'])
    else:
        characters = MainChar.current_place.character
        print_text_slowly(f'{message['chat_with']}{print_in_colour(characters, GREEN)}.')

    if len(MainChar.current_place.items) > 0:
            item_list = ''
            for item in MainChar.current_place.items:
                item_list += item.name + ' '
            print_text_slowly(message['items_found_in_room'])
            print_text_slowly(f'{print_in_colour(item_list, RED)}')
    else:
            print_text_slowly(message['no_items_in_room'])

# print list of available commands. a sort of quick help.
def commands():
    com_verbs = extract_list(command_verbs)
    print_text_slowly(f'{message['double_actions']}\n{print_in_colour(com_verbs, BLACK)}')
    single_coms = extract_list(single_word_commands)
    print_text_slowly(f'{message['single_actions']}\n{print_in_colour(single_coms, BLACK)}')

# print who is your current companion
def companion():
    current_follower = MainChar.get_follower()
    if MainChar.follower == 'none':
        print_text_slowly(message['no_companion'])
    else:
        print_text_slowly(f'{message['companion_is']}{current_follower}.{message['nice_feeling']}')

# if you have a rod and are at beach, a fish is added to place inventory
def fish():
    if MainChar.current_place.place_name == 'beach' and Rod in MainChar.inventory:
        MainChar.current_place.items.append(Fish)
        print_text_slowly(message['catch_fish'])
    else:
        print_text_slowly(message['cannot_fish'])

# Change items with an npc
def trade():
    if npc_data[MainChar.current_place.character]['trader'] == True:
        items = MainChar.get_inventory()
        wanted_item = npc_data[MainChar.current_place.character]['wants']
        trade_item = npc_data[MainChar.current_place.character]['trades']
        if wanted_item in items:
            print_text_slowly(f'The {MainChar.current_place.character}{message['will_trade']}')
            MainChar.add_to_inventory(trade_item)
            npc_data[MainChar.current_place.character]['items'].remove(trade_item)
            MainChar.remove_from_inventory(wanted_item )
            print_text_slowly(f'{message['give_item']}{wanted_item.name}{message['get_item']}{trade_item.name}.')
            npc_data[MainChar.current_place.character]['trader'] = False
            check_for_points_gained(wanted_item.name)
            check_for_points_gained(trade_item.name)
        else:
            print_text_slowly(f'The {MainChar.current_place.character}{message['no_trade_now']}')
    else:
        print_text_slowly(f'The {MainChar.current_place.character}{message['no_trade_at_all']}')

# If in forest and a shovel in inventory, circle is added to place inventory
def dig():
    inventory = MainChar.get_inventory()
    place = MainChar.current_place.place_name

    if place == 'forest' and Shovel in inventory:
        if Circle not in MainChar.current_place.items and Circle not in inventory:
            print_text_slowly(message['dig_success'])
            MainChar.current_place.items.append(Circle)
        else:
            print_text_slowly(message['dig_not_anymore'])

    elif place == 'forest' and Shovel not in inventory:
        print_text_slowly(message['no_digging_tool'])

    elif place != 'forest' and Shovel in inventory:
        print_text_slowly(message['wrong_place_digging'])

    elif place != 'forest' and Shovel not in inventory:
        print_text_slowly(message['dig_failure'])

# if spearhead and circle in inventory, they are removed from player
# inventory and a symbol item is added
def combine():
    inventory = MainChar.get_inventory()
    if Circle in inventory and Spearhead in inventory:
        print_text_slowly(message['combine_success'])
        MainChar.add_to_inventory(Symbol)
        MainChar.remove_from_inventory(Circle)
        MainChar.remove_from_inventory(Spearhead)
        proof['symbol'] = True
        print_text_slowly(message['combine_extra_info'])

    elif Circle in inventory and Spearhead not in inventory:
         print_text_slowly(message['combine_spearhead_missing'])
    elif Circle not in inventory and Spearhead in inventory:
         print_text_slowly(message['combine_circle_missing'])
    elif Circle not in inventory and Spearhead not in inventory:
         print_text_slowly(message['no_items_to_combine'])

# if win conditions are met, show victory text and exit game
def climb():
    if MainChar.current_place.place_name == 'dungeon' and Symbol not in MainChar.inventory:
        declare_victory()
    else:
        print_text_slowly(message['will_not_climb'])


def act_on_single_command(command_input):
    try:
        if command_input == 'help':
            help()
        elif command_input == 'test':
            test()
        elif command_input == 'inventory':
            MainChar.print_inventory()
        elif command_input == 'directions':
            directions()
        elif command_input == 'describe':
            describe()
        elif command_input == 'commands':
            commands()
        elif command_input == 'companion':
            companion()
        elif command_input == 'fish':
            fish()
        elif command_input == 'trade':
            trade()
        elif command_input == 'dig':
            dig()
        elif command_input == 'combine':
            combine()
        elif command_input == 'climb':
            climb()
        elif command_input == 'secret':
            secret()
        else:
            print_text_slowly(message['command_not_found'])
    except Exception as e:
        print(e)