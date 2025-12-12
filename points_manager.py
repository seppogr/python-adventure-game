

points_gained = {
            'fish' : False, #
            'cat_fed': False,
            'survived_reading_book' : False,
            'manor' : False, #
            'knife': False, #
            'note' : False,
            'newspaper' : False,#
            'letter' : False, #
            'rag' : False, #
            'evidence' : False, #
            'evidence_delivered' : False,
            'passkey' : False,
            'circle' : False, #
            'spearhead' : False, #
            'symbol' : False, #
            'money' : False,
            'coffee' : False,
            'mirror' : False,
            'church' : False, #
            'crypt' : False, #
            'dungeon': False, #
            'game_won' : False, #
}

def return_points_gained():
    counter = 0
    for item in points_gained:
        if points_gained[item]:
            counter += 1
    return counter


def check_for_points_gained(input):
    if input in points_gained.keys():

        if points_gained[input] == False:
            print('Point gained!')

        points_gained[input] = True



