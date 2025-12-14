# Main file. LAunches and updates the game and the game ui.

from Player import MainChar
from Place import *
from commands import *
from printer import *
from single_actions import act_on_single_command
from double_actions import act_on_double_command
from points_manager import *
import sys
import os
from in_game_messages import in_game_messages as message

def print_ui():
        cls = lambda: os.system('clear')
        cls()
        title = f'     {print_in_colour('"The Strange Disappearance of Ernest Mulhoney"', BLACK)}'
        MainChar.points = return_points_gained()
        max_score = str(len(points_gained.keys()))
        current_score = str(MainChar.points)
        points = f'Points: {print_in_colour(current_score + '/' + max_score, WHITEBG)}'
        space = 9 * ' '
        print_a_line_of_stars(RED)
        print(f'{title}{space}{points}')
        print_a_line_of_stars(RED)

def main():
    start_text = open("start.txt")
    print(start_text.read())
    print()
    start_text.close()
    input('Press "Enter" to start your investigation.')
    print_ui()
    print_text_slowly(f'You are in {MainChar.current_place.at_first_glance}.')
    command_input = input('What will you do?> ').strip().lower()

    while command_input != ('quit'):

        print_ui()
        word_count_in_command = 0
        for item in command_input.split(" "):
            word_count_in_command = word_count_in_command + 1
        list_of_commands = command_input.split(" ")
        if word_count_in_command == 1 and command_input in single_word_commands:
            act_on_single_command(command_input)

        elif word_count_in_command == 2:
            verb = list_of_commands[0]
            noun = list_of_commands[1]
            if verb not in command_verbs:
                print_text_slowly(message['command_not_supported'])
            act_on_double_command(verb, noun)

        else:
            print_text_slowly(message['command_not_supported'])

        if MainChar.get_life_status() == False:
            print_text_slowly(f'Final score {MainChar.points}/{len(points_gained.keys())}')
            sys.exit(1)

        command_input = input('What will you do?> ').strip().lower()

    print_text_slowly('Bye!')

if __name__ == '__main__':
    main()