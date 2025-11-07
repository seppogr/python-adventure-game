# This is the main data container for all rooms in the adventure game.
# All list entries are dictionaries and can contain any number of entries.
#
# The format is as follows:

# placename : What the place is called.
# story: what is written when player enters the room. A short decription.
# items: a dictionary of pickable items in the room.
# characters: who you can talk to in the room
# speech: The characters first greeting when player enters the room
# door: a direction, can be locked and if so deny entry beyond

# to add more directions, just add more directions to the list.

places = [
        {'inn' :'inn',
        'story': 'Olet vanhassa hollituvassa.',
        'items': {'key': 'key', 'lamp': 'lamp'},
        'characters': 'isäntä',
        'speech' : 'Tervehdys matkalainen! Olisi vähän asiaa.',
        'door' : {'open': False, 'direction' : 'basement', 'open' : 'key' },
        'directions': ['basement', 'plaza', 'attic']
        },
        {'basement': 'basement',
         'story': 'Onpa täällä pimeää. Hui! Siut todennäköisesti syö grue.',
         'items': {'book': 'book'},
         'characters' : 'grue',
         'speech' : 'Maiskis!',
         'door' : {'open': True, 'direction' : 'inn' },
         'directions': ['inn']
        },
        {'plaza': 'plaza',
         'story': 'Town plaza',
         'items': {'book': 'book'},
         'characters' : 'loafer',
         'speech' : 'Dude!',
         'door' : {'open': True, 'direction' : 'inn' },
         'directions': ['inn', 'smithy', 'shop', 'trail']
        },
        {'attic': 'attic',
         'story': 'Dusty inn attic',
         'items': {'book': 'book'},
         'characters' : '',
         'speech' : '',
         'door' : {'open': True, 'direction' : 'inn' },
         'directions': ['inn']
        },
        {'smithy': 'smithy',
         'story': 'Village smithy',
         'items': {'book': 'book'},
         'characters' : '',
         'speech' : '',
         'door' : {'open': True, 'direction' : 'inn' },
         'directions': ['plaza']
        },
        {'shop': 'shop',
         'story': 'Village shop',
         'items': {'book': 'book'},
         'characters' : '',
         'speech' : '',
         'door' : {'open': True, 'direction' : 'inn' },
         'directions': ['plaza']
        },
        {'trail': 'trail',
         'story': 'Forest trail',
         'items': {'book': 'book'},
         'characters' : 'wild dog',
         'speech' : '',
         'door' : {'open': True, 'direction' : 'inn' },
         'directions': ['plaza', 'manor', 'churchyard', 'hut']
        },
        {'manor': 'manor',
         'story': 'noble manor house yard',
         'items': {'book': 'book'},
         'characters' : 'wild dog',
         'speech' : '',
         'door' : {'open': True, 'direction' : 'inn' },
         'directions': ['trail', 'stables', 'hall']
        },
        {'stables': 'stables',
         'story': 'grim crime scene',
         'items': {'book': 'book'},
         'characters' : 'wild dog',
         'speech' : '',
         'door' : {'open': True, 'direction' : 'inn' },
         'directions': ['manor']
        },
        {'hall': 'hall',
         'story': 'tidy manor hall',
         'items': {'book': 'book'},
         'characters' : 'wild dog',
         'speech' : '',
         'door' : {'open': True, 'direction' : 'inn' },
         'directions': ['manor', 'kitchen', 'upstairs', 'study']
        },
        {'study': 'study',
         'story': 'study room of a local nobleman',
         'items': {'book': 'book'},
         'characters' : 'count',
         'speech' : '',
         'door' : {'open': True, 'direction' : 'inn' },
         'directions': ['hall']
        },
        {'upstairs': 'upstairs',
         'story': 'a comfortable room for the countess',
         'items': {'book': 'book'},
         'characters' : 'countess',
         'speech' : '',
         'door' : {'open': True, 'direction' : 'inn' },
         'directions': ['hall']
        },
        {'kitchen': 'kitchen',
         'story': 'a hot kitchen',
         'items': {'book': 'book'},
         'characters' : 'cook',
         'speech' : '',
         'door' : {'open': True, 'direction' : 'inn' },
         'directions': ['hall']
        },
        {'hut': 'hut',
         'story': 'hut of  local witch',
         'items': {'book': 'book'},
         'characters' : 'witch',
         'speech' : '',
         'door' : {'open': True, 'direction' : 'inn' },
         'directions': ['trail', 'beach']
        },
        {'beach': 'beach',
         'story': 'beach',
         'items': {'book': 'book'},
         'characters' : 'witch',
         'speech' : '',
         'door' : {'open': True, 'direction' : 'inn' },
         'directions': ['hut', 'forest']
        },
        {'churchyard': 'churchyard',
         'story': 'outside the local church',
         'items': {'book': 'book'},
         'characters' : 'witch',
         'speech' : '',
         'door' : {'open': True, 'direction' : 'inn' },
         'directions': ['trail', 'church', 'forest']
        },
        {'forest': 'forest',
         'story': 'forest forest',
         'items': {'book': 'book'},
         'characters' : 'witch',
         'speech' : '',
         'door' : {'open': True, 'direction' : 'inn' },
         'directions': ['beach', 'churchyard']
        },
        {'church': 'church',
         'story': 'churchhh',
         'items': {'book': 'book'},
         'characters' : 'witch',
         'speech' : '',
         'door' : {'open': True, 'direction' : 'inn' },
         'directions': ['churchyard', 'crypt']
        },
        {'crypt': 'crypt',
         'story': 'a crypt',
         'items': {'book': 'book'},
         'characters' : 'witch',
         'speech' : '',
         'door' : {'open': True, 'direction' : 'inn' },
         'directions': ['church', 'dungeon']
        },
        {'dungeon': 'dungeon',
         'story': 'a dungeon',
         'items': {'book': 'book'},
         'characters' : 'witch',
         'speech' : '',
         'door' : {'open': True, 'direction' : 'inn' },
         'directions': ['crypt']
        }
]
