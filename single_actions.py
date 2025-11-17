from printer import *
from Player import MainChar
from utils import *
from colours import *

def test():
    print('test code here')
    print(MainChar.current_place.place_name)

def help():
    print_text('GET SOME HELP HERE')
        # aputiedosto = open("demohelp.txt")
            #todo: write the file below properly
            # print(aputiedosto.read())
            # print()
            # aputiedosto.close()

def directions():
    travel_directions = MainChar.current_place.directions.keys()
    print_text(f'You can go to: ')
    print_text(f'{print_in_colour(extract_list(travel_directions), VIOLET)}')

def describe():
    print_text(f'{MainChar.get_current_place().place_name.upper()}')
    print_text(f'{MainChar.get_current_place().description}')
    characters = MainChar.current_place.character
    print_text(f'You can see {print_in_colour(characters, GREEN)} here:')
    item_list = extract_list(MainChar.current_place.items)
    print_text(f'The following items are of note: ')
    print_text(f'{print_in_colour(item_list, RED)}')

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
    else:
        print_text('I do not understand that command.')