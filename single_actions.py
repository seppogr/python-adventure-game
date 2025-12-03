from printer import *
from Player import MainChar
from utils import *
from colours import *
from commands import *
from death_conditions import *

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
    print_text_slowly(f'You can go to: ')
    print_text_slowly(f'{print_in_colour(extract_list(travel_directions), VIOLET)}')

def describe():
    print_text_slowly(f'{MainChar.get_current_place().description}')

    if MainChar.current_place.character == '':
        print_text_slowly('There is nobody here.')
    else:
        characters = MainChar.current_place.character
        print_text_slowly(f'Maybe you can chat with the {print_in_colour(characters, GREEN)}.')

    if len(MainChar.current_place.items) > 0:
            item_list = extract_list(MainChar.current_place.items)
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
    if MainChar.current_place.place_name == 'beach' and 'rod' in MainChar.inventory:
        MainChar.add_to_inventory('fish')
        print_text_slowly('You spend a while fishing, and catch a nice fish. Now, who likes uncooked fish?')
    else:
        print_text_slowly('Generally, a significant body of water, such as an ocean, and some sort of fishing rod are both needed to catch fish.')

def read():
    items = MainChar.get_inventory()
    if 'book' in items:
        print_text_slowly('As you turn the pages it becomes evident that this book was not meant for mortal eyes.')
        print_text_slowly('However, you notice that someone has added notes to the sidelines.')
        if 'mask' in items:
            print_text_slowly('Good thing you managed to slip your welding mask on before reading.')
            print_text_slowly('The notes are a diary of cult meetings and what has been offered to the deity.')
            print_text_slowly('As you read down the list, you see that the last offering is scheduled for today and it is a human head.')
        else:
            check_for_death_by_book()

def trade():
    if npc_data[MainChar.current_place.character]['trader'] == True:
        items = MainChar.get_inventory()
        wanted_item = npc_data[MainChar.current_place.character]['wants']
        trade_item = npc_data[MainChar.current_place.character]['trades']
        if wanted_item in items:
            print_text_slowly(f'The {MainChar.current_place.character} is happy to trade ')
            MainChar.add_to_inventory(trade_item)
            npc_data[MainChar.current_place.character]['items'].remove(trade_item)
            MainChar.remove_from_inventory(wanted_item)
            print_text_slowly(f'You give the {wanted_item} and they hand over the {trade_item}.')
            npc_data[MainChar.current_place.character]['trader'] = False
    else:
        print_text_slowly(f'The {MainChar.current_place.character} has nothing that you want to trade.')

def act_on_single_command(command_input):
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
    elif command_input == 'read':
        read()
    elif command_input == 'trade':
        trade()
    else:
        print_text_slowly('I do not understand that command. Write "commands" for a quick help, or "help" for available commands with examples of use.')