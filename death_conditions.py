from Player import MainChar
from printer import *
from npcs import *


def main_char_death(killer, death_message, hint):
    print_text_slowly(death_message)
    if len(killer) > 1:
        print_text_slowly(f'Your journey ends in the hands of a {killer}.')
    print_text_slowly(hint)
    print_text_slowly('GAME OVER')
    print_text_slowly(f'Final points: {MainChar.get_points()}/200. ')
    MainChar.set_life_status(False)

def check_for_death_by_room(room):
    if room == 'basement' and Lamp not in MainChar.inventory:
        death_message = 'The darkness of the cellar engulfs you.\nSomething moves and then it all ends...'
        hint = 'Maybe a light source would have been useful. Just a thought.'
        main_char_death(MainChar.current_place.character, death_message, hint)

    if room == 'church' and (Circle not in MainChar.inventory or Spearhead not in MainChar.inventory) and Symbol not in MainChar.inventory:
        death_message = 'As you drop down on the church floor, you notice there is no way to reach\nwindow from this side. There is a door to the crypt but you cannot figure out\nhow to open it. After a while, you are surprised as the church door rattles and Alfred the Innkeeper opens the door. He stares at you for a while but then firmly\nescorts you back to town square where he puts you in the next bus out of village.'
        hint = 'You cannot but wonder if there would have beens some sort of way to open the\ncrypt door.'
        main_char_death('', death_message, hint)
    if room == 'crypt':
        death_message = 'You cannot force the portal open alone. You wait in the dim crypt. After a\nwhile, the portal opens and some robed figures spawn forth and surround you.\nThey take you to the room beyond. It is a some sort of an unholy worship place,\nand you retch as you suddenly realise there is a severed head on the altar. With\na face you well recognise! Then you feel a hit in your head, and nothing more.'
        hint = 'Could be that a strong companion might be able to force the portal. Too late\nnow...'
        main_char_death('', death_message, hint)

def check_for_death_by_item(room, items):
    if room == 'basement' and Lamp not in items:
        death_message = 'The cannibal smashes the lamp.\nIt is very, very dark and you have just time to\nfeel something sharp hitting you. Then the final darkness...'
        hint = 'In retrospective, possibly not the smartest choice giving your lamp away in a\ndark cellar just like that.'
        main_char_death(MainChar.current_place.character, death_message, hint)

    if room == 'inn' and Book in npc_data['innkeeper']['items']:
        death_message = 'The innkeeper smiles and informs you that regrettably the inn will close for the\nday.You are left outside waiting for some means of transportation out of here.\nAfter a couple of hours a bus arrives, and on the journey back to more civilised\nparts of the country you have a nagging feeling that you missed something. After\nall, you DID spy the innkeper hurrying to the direction of the forest with the\nbook.'
        hint = 'Maybe always doing what people tell you to is not a key to victory.'
        main_char_death('a', death_message, hint)



def check_for_death_by_book():
    death_message = 'First, your eyes feel like melting and a moment later it feels your brain is\nfrying. Then, nothing.'
    hint = 'Huh, reading strange books without some means of protection was not too bright.\nAfter all, it DID say "Necronomicon" on the cover.'
    main_char_death('book', death_message, hint)

def declare_victory():
    victory_text = open("victory.txt")
    print(victory_text.read())
    victory_text.close()
    print('THE END')
    print_text_slowly(f'Final points: {MainChar.get_points()}/200. ')
    MainChar.set_life_status(False)
