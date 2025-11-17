# Place:
#         placeName -> name of the place : string
#         placeIndex -> index number of the place: number
#         atFirstGlance -> description of the place when the player enters : string
#         items -> inventory of items in the place : list
#         character -> the character in the room you can talk to : string
#         description- > more information of the place : string
#         door -> door properties : dictionary
#               open : boolean (False if locked, True if open)
#               direction : string (placeName of an area)
#               unlockedBy : string (in the items.py dictionary 'items', what is needed to unlock the door)
#         blocker -> blocks movement anywhere but back : dictionary
#               blocked : boolean (False if no blocker)
#               name : string (name of the blocker, eg 'wolf', 'wild dog' etc)
#               unBlockedBy : string (what item the blocker requires to stop blocking)
#               afterMessage : string (shown after unBlocked)
#         directions - >where you can go to from here : dictionary

class Place:
        """Paikkaobjekti"""
        def __init__(self, place_name, place_index, at_first_glance, items, character, description, door, blocker, directions):
                self.place_name = place_name
                self.place_index = place_index
                self.at_first_glance = at_first_glance
                self.items = items
                self.character = character
                self.description = description
                self.door = door
                self.blocker = blocker
                self.directions = directions

        def get_place_name(self):
                return self.place_name

Inn = Place (
        'inn',
        0,
        'the main room of a country inn',
        ['lamp'],
        'innkeeper',
        'Area longer description',
        {'open': False, 'direction' : 'basement', 'unlocked_by' : 'key' },
        {'blocked' : False, 'name': '', 'unBlockedBy': '','after_message' : ''},
        {'basement' : 1, 'plaza' : 2, 'attic' : 3}
)

Basement = Place (
        'basement',
        1,
        'a dark basement',
        ['book'],
        'grue',
        'Area longer description',
        {'open': True, 'direction' : 'inn', 'unlocked_by' : 'key' },
        {'blocked' : False, 'name': '', 'unBlockedBy': '','after_message' : ''},
        {'inn': 0}
)

Plaza = Place (
        'plaza',
        2,
        'a town plaza',
        ['book'],
        'grue',
        'Area longer description',
        {'open': False, 'direction' : 'basement', 'unlocked_by' : 'key' },
       {'blocked' : False, 'name': '', 'unBlockedBy': '','after_message' : ''},
        {'inn': 0, 'smithy' : 4, 'shop': 5, 'trail' : 6}
)

Attic = Place (
        'attic',
        3,
        'an attic of an inn',
        ['book'],
        'grue',
        'Area longer description',
        {'open': False, 'direction' : 'basement', 'unlocked_by' : 'key' },
        {'blocked' : False, 'name': '', 'unBlockedBy': '','after_message' : ''},
        {'inn': 0}
)

Smithy = Place (
        'smithy',
        4,
        'a village smithy',
        ['book'],
        'grue',
        'Area longer description',
        {'open': False, 'direction' : 'basement', 'unlocked_by' : 'key' },
        {'blocked' : False, 'name': '', 'unBlockedBy': '','after_message' : ''},
        {'plaza': 2}
)

Shop = Place (
        'shop',
        5,
        'a small shop',
        ['book'],
        'grue',
        'Area longer description',
        {'open': False, 'direction' : 'basement', 'unlocked_by' : 'key' },
        {'blocked' : False, 'name': '', 'unBlockedBy': '','after_message' : ''},
        {'plaza': 2}
)

Trail = Place (
        'trail',
        6,
        'a forest trail',
        ['book'],
        'grue',
        'Area longer description',
        {'open': False, 'direction' : 'basement', 'unlocked_by' : 'key' },
        {'blocked' : False, 'name': '', 'unBlockedBy': '','after_message' : ''},
        {'plaza': 2, 'manor' : 7, 'hut' : 13, 'churchyard' : 15}
)

Manor = Place (
        'manor',
        7,
        'a grand manor house',
        ['book'],
        'grue',
        'Area longer description',
        {'open': False, 'direction' : 'basement', 'unlocked_by' : 'key' },
        {'blocked' : False, 'name': '', 'unBlockedBy': '','after_message' : ''},
        {'trail': 6, 'stables' : 8, 'hall' : 9}
)

Stables = Place (
        'stables',
        8,
        'the manor stables',
        ['book'],
        'grue',
        'Area longer description',
        {'open': False, 'direction' : 'basement', 'unlocked_by' : 'key' },
        {'blocked' : False, 'name': '', 'unBlockedBy': '','after_message' : ''},
        {'manor': 7}
)

Hall = Place (
        'hall',
        9,
        'the manor hallway',
        ['book'],
        'grue',
        'Area longer description',
        {'open': False, 'direction' : 'basement', 'unlocked_by' : 'key' },
        {'blocked' : False, 'name': '', 'unBlockedBy': '','after_message' : ''},
        {'manor': 7, 'study': 10, 'upstairs' : 11, 'kitchen' : 12}
)

Study = Place (
        'study',
        10,
        'the study of the count',
        ['book'],
        'grue',
        'Area longer description',
        {'open': False, 'direction' : 'basement', 'unlocked_by' : 'key' },
        {'blocked' : False, 'name': '', 'unBlockedBy': '','after_message' : ''},
        {'hall': 9}
)

Upstairs = Place (
        'upstairs',
        11,
        'manor upstairs floor',
        ['book'],
        'grue',
        'Area longer description',
        {'open': False, 'direction' : 'basement', 'unlocked_by' : 'key' },
        {'blocked' : False, 'name': '', 'unBlockedBy': '','after_message' : ''},
        {'hall': 9}
)

Kitchen = Place (
        'a kitchen',
        12,
        'well-equipped manor kitchen',
        ['book'],
        'grue',
        'Area longer description',
        {'open': False, 'direction' : 'basement', 'unlocked_by' : 'key' },
        {'blocked' : False, 'name': '', 'unBlockedBy': '','after_message' : ''},
        {'hall': 9}
)

Hut = Place (
        'hut',
        13,
        'a hut by the sea',
        ['book'],
        'grue',
        'Area longer description',
        {'open': False, 'direction' : 'basement', 'unlocked_by' : 'key' },
        {'blocked' : False, 'name': '', 'unBlockedBy': '','after_message' : ''},
        {'trail': 6, 'beach' : 14}
)

Beach = Place (
        'beach',
        14,
        'a beach',
        ['book'],
        'grue',
        'Area longer description',
        {'open': False, 'direction' : 'basement', 'unlocked_by' : 'key' },
        {'blocked' : False, 'name': '', 'unBlockedBy': '','after_message' : ''},
        {'hut': 13, 'forest' : 16}
)

Churchyard = Place (
        'churchyard',
        15,
        'a churchyard',
        ['book'],
        'grue',
        'Area longer description',
        {'open': False, 'direction' : 'basement', 'unlocked_by' : 'key' },
        {'blocked' : False, 'name': '', 'unBlockedBy': '','after_message' : ''},
        {'trail': 6, 'forest' : 16, 'church' : 17}
)

Forest = Place (
        'forest',
        16,
        'a green forest',
        ['book'],
        'grue',
        'Area longer description',
        {'open': False, 'direction' : 'basement', 'unlocked_by' : 'key' },
        {'blocked' : False, 'name': '', 'unBlockedBy': '','after_message' : ''},
        {'beach': 14, 'churchyard' : 15}
)

Church = Place (
        'church',
        17,
        'the village church',
        ['book'],
        'grue',
        'Area longer description',
        {'open': False, 'direction' : 'basement', 'unlocked_by' : 'key' },
        {'blocked' : False, 'name': '', 'unBlockedBy': '','after_message' : ''},
        {'churchyard': 15, 'crypt' : 18}
)

Crypt = Place (
        'crypt',
        18,
        'the crypt beneath the church',
        ['book'],
        'grue',
        'Area longer description',
        {'open': False, 'direction' : 'basement', 'unlocked_by' : 'key' },
        {'blocked' : False, 'name': '', 'unBlockedBy': '','after_message' : ''},
        {'church': 17, 'dungeon' : 19}
)

Dungeon = Place (
        'dungeon',
        19,
        'a dungeon',
        ['book'],
        'grue',
        'Area longer description',
        {'open': False, 'direction' : 'basement', 'unlocked_by' : 'key' },
        {'blocked' : False, 'name': '', 'unBlockedBy': '','after_message' : ''},
        {'crypt': 18}
)
places = [Inn, Basement, Plaza,
          Attic, Smithy, Shop,
          Trail, Manor, Stables,
          Hall, Study, Upstairs,
          Kitchen, Hut, Beach,
          Churchyard, Forest, Church,
          Crypt, Dungeon]
