
class Place:
        def __init__(self, placeName, placeIndex, story, items, character, speech, door, directions):
                self.placeName = placeName
                self.placeIndex = placeIndex
                self.story = story
                self.items = items
                self.character = character
                self.speech = speech
                self.door = door
                self.directions = directions

        def get_placeName(self):
                return self.placeName

Inn = Place (
        'inn',
        0,
        'Olet vanhassa hollituvassa.',
        ['key', 'lamp'],
        'innkeeper',
        'Welcome traveller! Stay awhile, and listen!',
        {'open': False, 'direction' : 'basement', 'open' : 'key' },
        {'basement' : 1, 'attic' : 2}
)

Basement = Place (
        'basement',
        1,
        'A dark basement',
        ['book'],
        'grue',
        'I will eat you',
        {'open': False, 'direction' : 'basement', 'open' : 'key' },
        {'inn': 0}
)
Attic = Place (
        'attic',
        2,
        'Attic',
        ['book'],
        'grue',
        'I will eat you',
        {'open': False, 'direction' : 'basement', 'open' : 'key' },
        {'inn': 0}
)

places = [Inn, Basement, Attic]
