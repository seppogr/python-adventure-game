from Player import MainChar
from printer import *


def main_char_death(killer, death_message, hint):
    print_text_slowly(death_message)
    print_text_slowly(f'Your journey ends in the hands of a {killer}.')
    print_text_slowly(hint)
    print_text_slowly('GAME OVER')
    print_text_slowly(f'Final points: {MainChar.get_points()}/200. ')
    MainChar.set_life_status(False)


def check_for_death_by_room(room):
    if room == 'basement' and 'lamp' not in MainChar.inventory:
        death_message = 'The darkness of the cellar engulfs you. Something moves and then it all ends...'
        hint = 'Maybe a light source would have been useful. Just a thought.'
        main_char_death(MainChar.current_place.character, death_message, hint)

def check_for_death_by_item(room, items):
    if room == 'basement' and 'lamp' not in items:
        death_message = 'The wererat smashes the lamp. It is very, very dark and you have just time to feel something sharp hitting you. Then the final darkness...'
        hint = 'In retrospective, possibly not the smartest choice giving your lamp away in a dark cellar just like that.'
        main_char_death(MainChar.current_place.character, death_message, hint)