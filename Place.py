
class Place:
        """Paikkaobjekti"""
        def __init__(self, placeName, placeIndex, atFirstGlance, items, character, description, door, directions):
                self.placeName = placeName
                self.placeIndex = placeIndex
                self.atFirstGlance = atFirstGlance
                self.items = items
                self.character = character
                self.description = description
                self.door = door
                self.directions = directions

        def get_placeName(self):
                return self.placeName

Inn = Place (
        'inn',
        0,
        'the main room of a country inn',
        ['key', 'lamp'],
        ['innkeeper', 'grue'],
        'a once-beautiful room!',
        {'open': False, 'direction' : 'basement', 'open' : 'key' },
        {'basement' : 1, 'plaza' : 2, 'attic' : 3}
)

Basement = Place (
        'basement',
        1,
        'a dark basement',
        ['book'],
        ['grue'],
        'Underground area littered with debris.',
        {'open': False, 'direction' : 'basement', 'open' : 'key' },
        {'inn': 0}
)

Plaza = Place (
        'plaza',
        2,
        'a town plaza',
        ['book'],
        ['grue'],
        'I will eat you',
        {'open': False, 'direction' : 'basement', 'open' : 'key' },
        {'inn': 0, 'smithy' : 4, 'shop': 5, 'trail' : 6}
)

Attic = Place (
        'attic',
        3,
        'an attic of an inn',
        ['book'],
        ['grue'],
        'I will eat you',
        {'open': False, 'direction' : 'basement', 'open' : 'key' },
        {'inn': 0}
)

Smithy = Place (
        'smithy',
        4,
        'a village smithy',
        ['book'],
        ['grue'],
        'I will eat you',
        {'open': False, 'direction' : 'basement', 'open' : 'key' },
        {'plaza': 2}
)

Shop = Place (
        'shop',
        5,
        'a small shop',
        ['book'],
        ['grue'],
        'I will eat you',
        {'open': False, 'direction' : 'basement', 'open' : 'key' },
        {'plaza': 2}
)

Trail = Place (
        'trail',
        6,
        'a forest trail',
        ['book'],
        ['grue'],
        'I will eat you',
        {'open': False, 'direction' : 'basement', 'open' : 'key' },
        {'plaza': 2, 'manor' : 7, 'hut' : 13, 'churchyard' : 15}
)

Manor = Place (
        'manor',
        7,
        'a grand manor house',
        ['book'],
        ['grue'],
        'I will eat you',
        {'open': False, 'direction' : 'basement', 'open' : 'key' },
        {'trail': 6, 'stables' : 8, 'hall' : 9}
)

Stables = Place (
        'stables',
        8,
        'the manor stables',
        ['book'],
        ['grue'],
        'I will eat you',
        {'open': False, 'direction' : 'basement', 'open' : 'key' },
        {'manor': 7}
)

Hall = Place (
        'hall',
        9,
        'the manor hallway',
        ['book'],
        ['grue'],
        'I will eat you',
        {'open': False, 'direction' : 'basement', 'open' : 'key' },
        {'manor': 7, 'study': 10, 'upstairs' : 11, 'kitchen' : 12}
)

Study = Place (
        'study',
        10,
        'the study of the count',
        ['book'],
        ['grue'],
        'I will eat you',
        {'open': False, 'direction' : 'basement', 'open' : 'key' },
        {'hall': 9}
)

Upstairs = Place (
        'upstairs',
        11,
        'manor upstairs floor',
        ['book'],
        ['grue'],
        'I will eat you',
        {'open': False, 'direction' : 'basement', 'open' : 'key' },
        {'hall': 9}
)

Kitchen = Place (
        'a kitchen',
        12,
        'well-equipped manor kitchen',
        ['book'],
        ['grue'],
        'I will eat you',
        {'open': False, 'direction' : 'basement', 'open' : 'key' },
        {'hall': 9}
)

Hut = Place (
        'hut',
        13,
        'a hut by the sea',
        ['book'],
        ['grue'],
        'I will eat you',
        {'open': False, 'direction' : 'basement', 'open' : 'key' },
        {'trail': 6, 'beach' : 14}
)

Beach = Place (
        'beach',
        14,
        'a beach',
        ['book'],
        ['grue'],
        'I will eat you',
        {'open': False, 'direction' : 'basement', 'open' : 'key' },
        {'hut': 13, 'forest' : 16}
)

Churchyard = Place (
        'churchyard',
        15,
        'a churchyard',
        ['book'],
        ['grue'],
        'I will eat you',
        {'open': False, 'direction' : 'basement', 'open' : 'key' },
        {'trail': 6, 'forest' : 16, 'church' : 17}
)

Forest = Place (
        'forest',
        16,
        'a green forest',
        ['book'],
        ['grue'],
        'I will eat you',
        {'open': False, 'direction' : 'basement', 'open' : 'key' },
        {'beach': 14, 'churchyard' : 15}
)

Church = Place (
        'church',
        17,
        'the village church',
        ['book'],
        ['grue'],
        'I will eat you',
        {'open': False, 'direction' : 'basement', 'open' : 'key' },
        {'churchyard': 15, 'crypt' : 18}
)

Crypt = Place (
        'crypt',
        18,
        'the crypt beneath the church',
        ['book'],
        ['grue'],
        'I will eat you',
        {'open': False, 'direction' : 'basement', 'open' : 'key' },
        {'church': 17, 'dungeon' : 19}
)

Dungeon = Place (
        'dungeon',
        19,
        'a horrible dungeon',
        ['book'],
        ['grue'],
        'I will eat you',
        {'open': False, 'direction' : 'basement', 'open' : 'key' },
        {'crypt': 18}
)
places = [Inn, Basement, Plaza,
          Attic, Smithy, Shop,
          Trail, Manor, Stables,
          Hall, Study, Upstairs,
          Kitchen, Hut, Beach,
          Churchyard, Forest, Church,
          Crypt, Dungeon]
