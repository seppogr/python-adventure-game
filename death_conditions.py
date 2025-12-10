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
        death_message = 'As you drop down on the church floor, you notice there is no way to reach window from this side.\nThere is a door to the crypt but you cannot figure out how to open it.\nAfter a while, you are surprised as the church door rattles and Alfred the Innkeeper opens the door.\nHe stares at you for a while but then firmly escorts you back to town square where he puts you in the next bus out of village.'
        hint = 'You cannot but wonder if there would have beens some sort of way to open the crypt door.'
        main_char_death('', death_message, hint)
    if room == 'crypt':
        death_message = 'You cannot force the portal open alone.\nYou wait in the dim crypt.\nAfter a while, the portal opens and some robed figures spawn forth and surround you.\nThey take you to the room beyond.\nIt is a some sort of an unholy worship place,\nand you retch as you suddenly realise there is a severed head on the altar.\nA head you well recognise!\nThen you feel a hit in your head, and nothing more.'
        hint = 'Could be that a strong companion might be able to force the portal. Too late now...'
        main_char_death('', death_message, hint)

def check_for_death_by_item(room, items):
    if room == 'basement' and Lamp not in items:
        death_message = 'The cannibal smashes the lamp.\nIt is very, very dark and you have just time to feel something sharp hitting you.\nThen the final darkness...'
        hint = 'In retrospective, possibly not the smartest choice giving your lamp away in a dark cellar just like that.'
        main_char_death(MainChar.current_place.character, death_message, hint)

    if room == 'inn' and Book in npc_data['innkeeper']['items']:
        death_message = 'The innkeeper smiles and informs you that regrettably the inn will close for the day.\nYou are left outside waiting for some means of transportation out of here.\nAfter a couple of hours a bus arrives, and on the journey back\nto more civilised parts of the country you have a nagging feeling that you missed something.\nAfter all, you DID spy the innkeper hurrying to the direction of the forest with the book.'
        hint = 'Maybe always doing what people tell you to is not a key to victory.'
        main_char_death('a', death_message, hint)



def check_for_death_by_book():
    death_message = 'First, your eyes feel like melting and a moment later it feels your brain is frying. Then, nothing.'
    hint = 'Huh, reading strange books without some means of protection was not too bright. After all, it DID say "Necronomicon" on the cover. '
    main_char_death('book', death_message, hint)

def declare_victory():
    victory_text = open("victory.txt")
    print(victory_text.read())
    victory_text.close()
    print('THE END')
    print_text_slowly(f'Final points: {MainChar.get_points()}/200. ')