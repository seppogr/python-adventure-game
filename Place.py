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

from Item import *

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
        [Lamp],
        'innkeeper',
        '''
        COMMON ROOM

        This is a typical inn. You can see several tables and chairs,
        and there is a fire warming up weary travelers in the fireplace.
        You smell a delicious aroma in the air. In the back of the room
        there is a bar, and behind it an innkeeper stands ready to serve
        customers. Curiously, there is no one else around. There are two
        doors, one leading to th square, and another one. Stairs are
        leading upstairs into the attic.

        ''',
        {'open': False, 'direction' : 'basement', 'unlocked_by' : Key },
        {'blocked' : False, 'direction' : '', 'name': '', 'unblocked_by': '','after_message' : ''},
        {'basement' : 1, 'plaza' : 2, 'attic' : 3}
)

Basement = Place (
        'basement',
        1,
        'a dark basement',
        [Book],
        'cannibal',
        '''
        THE INN BASEMENT

        As you take a look around in the lamplight, you can see almost nothing
        out of the ordinary in this underground celler. Several goods requiring
        cold storage are stacked here in barrels and crates. However, there is
        a character shifting nervously just at the edge of the circle of light
        radiating from your lamp. It looks like a you have stumbled into the
        lair of a sharp-toothed wererat. Additionally, you notice a black-bound
        book in the middle of what appears to be a faded red circle. The only way
        out of here is way you came.

        ''',
        {'open': True, 'direction' : 'inn', 'unlocked_by' : No_item },
        {'blocked' : False, 'direction' : '', 'name': '', 'unblocked_by': '','after_message' : ''},
        {'inn': 0}
)

Plaza = Place (
        'plaza',
        2,
        'a town plaza',
        [Note],
        'idler',
        '''
        THE TOWN SQUARE

        You can see several buildings lining up this small town square or plaza,
        but people are absent. The only one around seems to be some sort of
        village idler. They sure talk a lot but don't make much sense. Still, could
        be useful at least try to chat wit them. A clinking noise is coming from the
        village smithy. There is also an inn and a shop lining this small square.
        A small carriage trail leads further into the woods.

        ''',
        {'open': True, 'direction' : '', 'unlocked_by' : No_item },
        {'blocked' : False,  'direction' : '', 'name': '', 'unblocked_by': '','after_message' : ''},
        {'inn': 0, 'smithy' : 4, 'shop': 5, 'trail' : 6}
)

Attic = Place (
        'attic',
        3,
        'a dusty attic',
        [Newspaper],
        'cat',
        '''
        THE INN ATTIC

        This is the inn attic. Whereas other areas have been quite neat and tidy,
        this room is the total opposite. There are all sorts of piles of junk
        everywhere and you guess that it would take a better part of a week
        to organise everything. There is an orange tabby cat lazing around.
        Stairs lead back down to the common room of the inn.

        ''',
        {'open': True, 'direction' : '', 'unlocked_by' : No_item },
        {'blocked' : False,  'direction' : '', 'name': '', 'unblocked_by': '','after_message' : ''},
        {'inn': 0}
)

Smithy = Place (
        'smithy',
        4,
        'a village smithy',
        [Mask],
        'smith',
        '''
        SMITHY

        Heat and smell of metal welcomes you to the village smithy. There are
        tools everywhere, and a giant anvil dominates the room. The deafening noise
        stops when you open the door and enter. All is suddenly very, very quiet.
        The only door leads back to the square.

        ''',
        {'open': True, 'direction' : '', 'unlocked_by' : No_item },
        {'blocked' : False,  'direction' : '', 'name': '', 'unblocked_by': '','after_message' : ''},
        {'plaza': 2}
)

Shop = Place (
        'shop',
        5,
        'a local shop',
        [],
        'shopkeeper',

        '''
        A SMALL SHOP

        As you enter from the open door, you find yourseld in a shop. It is evident
        that the customers are local farmers as the products on sale are typical
        farming equipment. Maybe there could be something useful to buy amidst all
        the items you deem unnecessary in your profession. No other doors here except
        the one you came from.

        ''',
        {'open': True, 'direction' : '', 'unlocked_by' : No_item },
        {'blocked' : False,  'direction' : '', 'name': '', 'unblocked_by': '','after_message' : ''},
        {'plaza': 2}
)

Trail = Place (
        'trail',
        6,
        'a forest trail',
        [],
        '',
         '''
        TRAIL IN THE FOREST

        The trail leading to local manor is not wide, but a well-enough
        maintained that a carriage can pass through. It is still evident
        that traffic is scarce. The air smells fresh and forest around is
        green with plants and trees.

        ''',
        {'open': True, 'direction' : '', 'unlocked_by' : No_item },
        {'blocked' : True, 'direction': 'manor','name': 'vicious dog', 'unblocked_by': 'cat','after_message' : '... the cat drives the vicious dog away!'},
        {'plaza': 2, 'manor' : 7, 'hut' : 13, 'churchyard' : 15}
)

Manor = Place (
        'manor',
        7,
        'a manor courtyard',
        [Ladder],
        '',
        '''
        MANOR COURTYARD

        You are looking at the manor of the local lord. It has two stories
        and has clearly seen better days: the paint is peeling here and there
        and the roof looks like it would need a makeover before it starts
        leaking. You hazard a guess it will as soon as it starts raining.
        You can visit the smithy or go straight to manor, or to the forest trail.

        ''',
        {'open': True, 'direction' : '', 'unlocked_by' : No_item },
        {'blocked' : False,  'direction' : '', 'name': '', 'unblocked_by': '','after_message' : ''},
        {'trail': 6, 'stables' : 8, 'hall' : 9}
)

Stables = Place (
        'stables',
        8,
        'the manor stables',
        [Knife],
        'stablehand',
        '''
        STABLES

        This is the place where normally horses are kept out of the rain. However,
        at the moment there are none due to a grisly scene in one of the corners.
        You can see bloodstains in one corner. There is also a stablehand present. They
        seem a bit shaken. He shuffles nervously.

        ''',
        {'open': True, 'direction' : '', 'unlocked_by' : No_item },
        {'blocked' : False,  'direction' : '', 'name': '', 'unblocked_by': '','after_message' : ''},
        {'manor': 7}
)

Hall = Place (
        'hall',
        9,
        'the manor hallway',
        [Mirror],
        '',
        '''
        MANOR HALLWAY

        As you enter the hallway a strange quietness envelopes you. It is as
        if there are layers upon layers of old and buried secrets in this manor house.
        There are dusty paintings on the walls, and the people in the a staring at you
        sternly from times gone.

        ''',
        {'open': False, 'direction' : 'upstairs', 'unlocked_by' : Passkey },
        {'blocked' : False,  'direction' : '', 'name': '', 'unblocked_by': '','after_message' : ''},
        {'manor': 7, 'study': 10, 'upstairs' : 11, 'kitchen' : 12}
)

Study = Place (
        'study',
        10,
        'the study of the count',
        [Letter],
        'count',
        '''
        STUDY OF THE MANOR LORD

        This is the stydy of the manor lord, Count Willis. Books line the walls and
        an old globe sits in the corner. On display is also an old armour,
        perhaps it has once been instrumental in gaining these lands. Curiously, a
        used-looking bed is in the corner, which looks very out-of-place.

        ''',
        {'open': True, 'direction' : '', 'unlocked_by' : No_item },
        {'blocked' : False,  'direction' : '', 'name': '', 'unblocked_by': '','after_message' : ''},
        {'hall': 9}
)

Upstairs = Place (
        'upstairs',
        11,
        'manor upstairs floor',
        [],
        'countess',
        '''
        UPSTAIRS

        Soft chanting fills your ears as you enter the upsairs room.
        The upstairs is a single large space, and it is aparent that some years
        ago large renovations were started and later abandoned. Walls have been
        torn down but no new ones have been installed. Everywhere you look,
        there is only dust, except in one corner where you notice a bedding
        for a single person.
        ''',
        {'open': True, 'direction' : '', 'unlocked_by' : No_item },
        {'blocked' : False,  'direction' : '',  'name': '', 'unblocked_by': '','after_message' : ''},
        {'hall': 9}
)

Kitchen = Place (
        'kitchen',
        12,
        'a well-equipped manor kitchen',
        [Money],
        'cook',
        '''
        KITCHEN

        The kitchen is clean, tidy and evidently run by care and precision.
        It looks everything that the rest of the manor is not. You get a sense
        of welcome in this room.

        ''',
        {'open': True, 'direction' : '', 'unlocked_by' : No_item },
        {'blocked' : False,  'direction' : '', 'name': '', 'unblocked_by': '','after_message' : ''},
        {'hall': 9}
)

Hut = Place (
        'hut',
        13,
        'a hut by the sea',
        [Rod],
        '',
        '''
        THE BEACH HUT

        THe hut by the beach is weather-worn, but at least the roof seems tight
        enough to keep the rain outside. By the hut door there are fishing
        equipment and next to the hut is a patch where some plants such as potatoes
        and carrots are grown. This does not seem to be a typical witch's hut but
        instead a fisherman's.

        ''',
        {'open': True, 'direction' : '', 'unlocked_by' : No_item },
        {'blocked' : False,  'direction' : '', 'name': '', 'unblocked_by': '','after_message' : ''},
        {'trail': 6, 'beach' : 14}
)

Beach = Place (
        'beach',
        14,
        'a beach',
        [],
        '',
        '''
        THE BEACH

        THe beach goes on and on to both directions. The sea is calm today,
        and there is nothing of interest out in the sea. However, something
        nags at you: nothing means exactly NOTHING, and you suddenly realise
        that there are no sea birds anywhere.

        ''',
        {'open': True, 'direction' : '', 'unlocked_by' : No_item },
        {'blocked' : False,  'direction' : '', 'name': '', 'unblocked_by': '','after_message' : ''},
        {'hut': 13, 'forest' : 16}
)

Churchyard = Place (
        'churchyard',
        15,
        'a churchyard',
        [Shovel],
        '',
        '''
        THE CHURCHYARD

        Around the churchyard there are several burial markers, and in this
        respect the environs of the local church does not differ in any way
        from that of a typical village church. On a closer look, you notice
        that all the markers grow with moss and there are no fresh graves even
        though the path to the church itself is well-used. The church door is
        firmly locked, but you could probably reach an open window above if
        you could reach it.

        ''',
        {'open': True, 'direction' : '', 'unlocked_by' : No_item },
        {'blocked' : True,  'direction' : 'church', 'name': 'a firmly locked door', 'unblocked_by': Ladder,'after_message' : 'climb through the window'},
        {'trail': 6, 'forest' : 16, 'church' : 17}
)

Forest = Place (
        'forest',
        16,
        'a green forest',
        [],
        '',
        '''
        A FOREST

        The trees are form a natural wall to both sides and amidst the dense
        growth is a game trail leading onwards. Curiously, all the man-made buldings
        in the area have shown severe dilapitation wheras the forest feels energetic
        and healthy. Somebody has gathered branches and arranged them to resemble an "X".

        ''',
        {'open': True, 'direction' : '', 'unlocked_by' : No_item },
        {'blocked' : False,  'direction' : '', 'name': '', 'unblocked_by': '','after_message' : ''},
        {'beach': 14, 'churchyard' : 15}
)

Church = Place (
        'church',
        17,
        'the village church',
        [],
        '',
        '''
        THE CHURCH INTERIOR

        Even though the path to the church was well-traveled it is difficult
        to believe that the church has seen much religious use recently. In the
        dusty floor is a clear traveled path to the catacombs. The catacomb door slams
        shut just as you enter, and there is an indentation of curious shape in the door.

        ''',
        {'open': False, 'direction' : 'crypt', 'unlocked_by' : Symbol},
        {'blocked' : False,  'direction' : '', 'name': '', 'unblocked_by': '','after_message' : ''},
        {'crypt' : 18}
)

Crypt = Place (
        'crypt',
        18,
        'a dark crypt',
        [],
        '',
          '''
        THE DARK CRYPT

        It seems a the church above was a much more recent construction than these catacombs.
        You get feeling of being crushed by the walls and the floor, but not of the ceiling.
        You suddenly notice a trail of blood droplets leading to a portal that has been barred
        with a sturdy door. You check the door, but someone much stronger is required to force
        it open.

        ''',
        {'open': True, 'direction' : '', 'unlocked_by' : No_item },
        {'blocked' : True,  'direction' : 'dungeon', 'name': 'portal', 'unblocked_by': 'smith','after_message' : '... the smith forces the portal open.'},
        {'dungeon' : 19}
)

Dungeon = Place (
        'dungeon',
        19,
        'a dungeon',
        [],
        '',
        '''
        THE RITUAL CHAMBER

        ''',
        {'open': True, 'direction' : '', 'unlocked_by' : No_item },
        {'blocked' : False,  'direction' : '', 'name': '', 'unblocked_by': '','after_message' : ''},
        {'crypt': 18}
)
places = [Inn, Basement, Plaza,
          Attic, Smithy, Shop,
          Trail, Manor, Stables,
          Hall, Study, Upstairs,
          Kitchen, Hut, Beach,
          Churchyard, Forest, Church,
          Crypt, Dungeon]
