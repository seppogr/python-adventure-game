from printer import *
from Player import MainChar
from utils import *
from colours import *
from commands import *

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
    else:
        print_text_slowly('I do not understand that command.')