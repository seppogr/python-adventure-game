from Player import MainChar
from Place import *
from commands import *
from printer import *
from utils import *
from single_actions import act_on_single_command
from double_actions import act_on_double_command

#currentInteraction = 'default'


print_text(f'You are in {MainChar.current_place.at_first_glance}.')

command_input = input('What will you do?> ').strip().lower()

while command_input != ('quit'):
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
            print_text('That command is not supported.')
        act_on_double_command(verb, noun)

    else:
        print_text('I do not understand that command.')

    command_input = input('What will you do?> ').strip().lower()
