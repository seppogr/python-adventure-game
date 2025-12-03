# npc_data:
# all data used in the game regarding the npc.

npc_data = {
    'innkeeper': {
        'description' : 'A middle-aged man with a beard and a worried look on his face. Probably wants to talk to you about something.',
        'wants' : 'book',
        'items' : ['key'],
        'greeting' : 'Hello traveler',
        'follower' : False,
        'trader'   : False,
        'trades'   : ''
    },
    'wererat' : {
        'description' : 'A sharp-toothed monster. Likely you will get eaten by it.',
        'wants' : 'lamp',
        'items' : [],
        'greeting' : 'Graugh!!!',
        'follower' : False,
        'trader'   : False,
        'trades'   : ''
    },
    'cat' : {
        'description' : 'A fine-looking healthy cat.',
        'wants': 'fish',
        'items' : [],
        'greeting' : 'Meeee-oooow! MEEEE-OOOOWWW!',
        'follower' : True,
        'trader'   : False,
        'trades'   : ''
    },
    'smith' : {
        'description' : 'A strong man.',
        'wants': '',
        'items' : [],
        'greeting' : 'Hrmph!',
        'follower' : False,
        'trader'   : False,
        'trades'   : ''
    },
    'shopkeeper' : {
        'description' : 'An amiable follow. Apaprently used to dealing with people.',
        'wants': 'money',
        'items' : ['coffee'],
        'greeting' : 'Hrmph!',
        'follower' : False,
        'trader'   : True,
        'trades'   : 'coffee'
    },
    'cook' : {
        'description' : 'An elderly cook. Clearly intelligent and runs the manor kitchen with utmost care.',
        'wants': 'coffee',
        'items' : ['keypass'],
        'greeting' : 'Hello dear!',
        'follower' : False,
        'trader'   : True,
        'trades'   : 'keypass'
    }
}

# npc_conversation:
# A dictionary of various non-player characters encountered n the game.
# Keys represent different conversation topics and values what the npc has to say about it.

npc_conversation = {
    'innkeeper'     : {
        'name'      : 'I am Alfred.',
        'job'       : 'Yes, I AM the innkeeper.',
        'mission'   : 'There is a book in the basement. Can you bring it to me?',
        'key'       : 'You will need this key to open the basement door.',
        'lamp'      : 'That is a good lamp.',
        'wererat'   : 'A wererat has mede its lair in the basement and I cannot go there myself.',
        'basement'  : 'It is our wine cellar. Kept dark in purpose.',
        'book'      : 'The count left it in the basement.',
        'friend'    : 'I think someone of that description was here but left in a hurry. I do not think he is in the area anymore.'
    },
    'wererat' : {
        'wererat'   : 'I must stay here in the basement until the sun goes down. Just my luck I guess.',
        'mission'   : 'What a nice lamp you have, please give it to me! I hate it here in the dark.',
        'book'      : 'It is not important, no need for you to check it. Just leave it here in the circle.',
        'circle'    : 'Just some drawing on the floor. Nothing important.',
        'friend'    : 'Mmmm---friend yes-yes friend.'
    },
    'cat' : {
        'meow'      : 'MEOW!',
        'purr'      : 'Purrr-rrrrr.'
    },
    'smith' : {
        'name'      : 'I am Alan.',
        'job'       : 'The local smith, I also fix this and that.',
        'mask'      : 'That, an old welding mask. I do not use it anymore. Just take it if you need it.',
        'innkeeper' : 'He has some business going on with the coun in the manor. I do not trust them.',
        'count'     : 'The old lord hereabouts. Only the cook of their household is of a good sort.'
    },
    'shopkeeper' : {
        'name'      : 'William, at your service.',
        'job'       : 'I run this country shop. We mainly sell farming equipment and other equipment.',
        'coffee'    : 'Ah, yes I sell quality coffee.',
        'food'      : 'The locals grow or fish their own food, I just sell coffee and seasonings.'
    },
    'cook' : {
        'name'      : 'My name is Lina.',
        'job'       : 'I cook for the lord and the lady, been doing that for fifty years now.',
        'help'      : 'If you could be so dear and fetch my coffee package from the shop.',
        'money'     : 'Take that money from the table, it should be enough.',
        'coffee'    : 'With some money you could go and buy it from the shop if you do not mind.',
        'trade'     : 'Get me some coffee and I will give the upstairs passkey.',
        'passkey'   : 'It will unlock the upstairs door.'
    }
}