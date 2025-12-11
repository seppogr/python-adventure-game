import os

points_gained = {
            'fish_caught' : False,
            'cat_fed'   : False,
            'dog_chased_away' : False,
            'knife': False,
            'note' : False,
            'letter' : False,
            'rag' : False,
            'evidence_gathered' : False,
            'evidence_delivered' : False,
            'passkey_gained' : False,
            'circle_found' : False,
            'spearhead_found' : False,
            'symbol_combined' : False,
            'church' : False,
            'crypt' : False,
            'dungeon': False,
            'game_won' : False,

}

def return_points_gained():
    counter = 0
    for item in points_gained:
        if points_gained[item]:
            counter += 1
    return counter


def check_for_points_gained(input):
    if input in points_gained.keys():
        points_gained[input] = True
        print('Point gained!')
