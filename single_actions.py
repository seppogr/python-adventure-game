from printer import *
from Player import MainChar
from utils import *
from colours import *
from commands import *
from death_conditions import *
from Item import *
from proof_manager import proof

def test():
    print('test code here')
    print(MainChar.current_place.place_name)

def help():
    help_file = open("help.txt")
    print(help_file.read())
    print()
    help_file.close()
    print('For a quick list of available commands, write "commands"')

def directions():
    travel_directions = MainChar.current_place.directions.keys()
    number_of_directions =len(travel_directions)
    if number_of_directions == 1:
        print_text_slowly('From here, the only way is: ')
    else:
        print_text_slowly(f'You notice the following possible directions: ')
    print_text_slowly(f'{print_in_colour(extract_list(travel_directions), VIOLET)}')

def describe():
    print_text_slowly(f'{MainChar.get_current_place().description}')

    if MainChar.current_place.character == '' and MainChar.follower != 'none':
        print_text_slowly(f'There is nobody except you and {MainChar.follower} here.')
    elif MainChar.current_place.character == '':
        print_text_slowly('You are alone.')
    else:
        characters = MainChar.current_place.character
        print_text_slowly(f'Maybe you can chat with the {print_in_colour(characters, GREEN)}.')

    if len(MainChar.current_place.items) > 0:
            item_list = ''
            for item in MainChar.current_place.items:
                item_list += item.name + ' '
            print_text_slowly(f'Some possibly useful items are lying around: ')
            print_text_slowly(f'{print_in_colour(item_list, RED)}')
    else:
            print_text_slowly('There are no interesting items around.')

def commands():
    com_verbs = extract_list(command_verbs)
    print_text_slowly(f'Combine these with a noun (for example place or item etc.): {print_in_colour(com_verbs, BLACK)}')
    single_coms = extract_list(single_word_commands)
    print_text_slowly(f'These will work as a single command: {print_in_colour(single_coms, BLACK)}')

def companion():
    current_follower = MainChar.get_follower()
    if MainChar.follower == 'none':
        print_text_slowly('You do not have a companion at the moment, maybe you will find one.')
    else:
        print_text_slowly(f'Your current companion is a {current_follower}. It feels nice not to be alone.')

def fish():
    if MainChar.current_place.place_name == 'beach' and Rod in MainChar.inventory:
        MainChar.current_place.items.append(Fish)
        print_text_slowly('You spend a while fishing, and catch a nice fish. Now, who likes uncooked fish?')
    else:
        print_text_slowly('Generally, a significant body of water, such as an ocean, and some sort of fishing rod are both needed to catch fish.')


def trade():
    if npc_data[MainChar.current_place.character]['trader'] == True:
        items = MainChar.get_inventory()
        wanted_item = npc_data[MainChar.current_place.character]['wants']
        trade_item = npc_data[MainChar.current_place.character]['trades']
        if wanted_item in items:
            print_text_slowly(f'The {MainChar.current_place.character} is happy to trade ')
            MainChar.add_to_inventory(trade_item)
            npc_data[MainChar.current_place.character]['items'].remove(trade_item)
            MainChar.remove_from_inventory(wanted_item )
            print_text_slowly(f'You give the {wanted_item.name } and they hand over the {trade_item.name}.')
            npc_data[MainChar.current_place.character]['trader'] = False
    else:
        print_text_slowly(f'The {MainChar.current_place.character} has nothing that you want to trade.')

def dig():
    inventory = MainChar.get_inventory()
    place = MainChar.current_place.place_name

    if place == 'forest' and Shovel in inventory:
        print_text_slowly('You dig around the place marked with an "X" and find something.')
        print_text_slowly('It is a metal circle.')
        MainChar.current_place.items.append(Circle)

    elif place == 'forest' and Shovel not in inventory:
        print_text_slowly('The ground is soft and good for digging and ther certainly is an "X" to mark something. But you have no tool for digging.')

    elif place != 'forest' and Shovel in inventory:
        print_text_slowly('This is not a good place to dig. Or are you inside a building perhaps? In any case the shovel is ineffective.')

    elif place != 'forest' and Shovel not in inventory:
        print_text_slowly('What you are missing is a good place to dig, and a tool for doing it.')

def combine():
    inventory = MainChar.get_inventory()
    if Circle in inventory and Spearhead in inventory:
        print_text_slowly('You take the spear and the circle, and try to fit them together. After a while of tinkering they both fit in place!')
        MainChar.current_place.items.append(Symbol)
        MainChar.remove_from_inventory(Circle)
        MainChar.remove_from_inventory(Spearhead)
        proof['symbol'] = True

        print_text_slowly('It is clearly a religious symbol, but could also be a key to a locked place?')

    elif Circle in inventory and Spearhead not in inventory:
         print_text_slowly('The markings of the metal circle look as if it could be combined with something.')
    elif Circle not in inventory and Spearhead in inventory:
         print_text_slowly('You take a closer look at the spearhead and it does seem it could be combined with something.')
    elif Circle not in inventory and Spearhead not in inventory:
         print_text_slowly('You do not think you have anything that fits together with anything else.')

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
        else:
            print_text_slowly('I do not understand that command. Write "commands" for a quick help, or "help" for available commands with examples of use.')
    except Exception as e:
        print(e)