# npc_data:
# all data used in the game regarding the npc.
from Item import *

npc_data = {
    'innkeeper': {
        'description' : 'A middle-aged man with a beard and a worried look on his face. Probably wants to talk to you about something.',
        'wants' : Book,
        'items' : [Key],
        'greeting' : 'Hello traveler',
        'follower' : False,
        'trader'   : False,
        'trades'   : No_item
    },
    'cannibal' : {
        'description' : 'A sharp-toothed monster. Likely you will get eaten by it.',
        'wants' : Lamp,
        'items' : [],
        'greeting' : 'Graugh!!!',
        'follower' : False,
        'trader'   : False,
        'trades'   : No_item
    },
    'cat' : {
        'description' : 'A fine-looking healthy cat.',
        'wants': Fish,
        'items' : [],
        'greeting' : 'Meeee-oooow! MEEEE-OOOOWWW!',
        'follower' : True,
        'trader'   : False,
        'trades'   : No_item
    },
    'smith' : {
        'description' : 'A strong man.',
        'wants': Evidence,
        'items' : [],
        'greeting' : 'Hrmph!',
        'follower' : True,
        'trader'   : False,
        'trades'   : No_item
    },
    'shopkeeper' : {
        'description' : 'An amiable follow. Apaprently used to dealing with people.',
        'wants': Money,
        'items' : [Coffee],
        'greeting' : 'Hrmph!',
        'follower' : False,
        'trader'   : True,
        'trades'   : Coffee
    },
    'cook' : {
        'description' : 'An elderly cook. Clearly intelligent and runs the manor kitchen with utmost care.',
        'wants': Coffee,
        'items' : [Passkey],
        'greeting' : 'Hello dear!',
        'follower' : False,
        'trader'   : True,
        'trades'   : Passkey
    },
    'stablehand' : {
        'description' : 'A shifty character. Clearly hides something. But what?',
        'wants': No_item,
        'items' : [Rag],
        'greeting' : 'Uh.. Hi.',
        'follower' : False,
        'trader'   : False,
        'trades'   : No_item
    },
    'count' : {
        'description' : 'An old aristocrat. Seems well-aware that he is superior to you.',
        'wants': No_item,
        'items' : [],
        'greeting' : 'Yes, what ist it? Speak up, man!',
        'follower' : False,
        'trader'   : False,
        'trades'   : No_item
    },
        'countess' : {
        'description' : 'A sad-lookin lady.',
        'wants': Mirror,
        'items' : [Spearhead],
        'greeting' : 'Ohh. Ohh! OHHH!',
        'follower' : False,
        'trader'   : True,
        'trades'   : Spearhead
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
        'cannibal'   : 'A cannibal is kept in the basement and I cannot go there myself.',
        'basement'  : 'It is our wine cellar. Kept dark in purpose.',
        'book'      : 'The count left it in the basement.',
        'friend'    : 'I think someone of that description was here but left in a hurry. I do not think he is in the area anymore.'
    },
    'cannibal' : {
        'cannibal'   : 'I must stay here in the basement until the polica arrives. Just my luck I guess.',
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
        'count'     : 'The old lord hereabouts. Only the cook of their household is of a good sort.',
        'friend'    : 'He was here, fishing for a couple of days. And the disappeared',
        'disappearance' : 'A strange case, there is something odd about that.'
    },
    'shopkeeper' : {
        'name'      : 'Adam, at your service.',
        'job'       : 'I run this country shop. We mainly sell farming equipment and other equipment.',
        'coffee'    : 'Ah, yes I sell quality coffee.',
        'food'      : 'The locals grow or fish their own food, I just sell coffee and seasonings.',
        'count'     : 'Ahh, our lord hereabouts. Oldish fellow.',
        'friend'    : 'I think I saw somebody of that description not a few days past.'
    },
    'cook' : {
        'name'      : 'My name is Carla.',
        'job'       : 'I cook for the lord and the lady, been doing that for fifty years now.',
        'help'      : 'If you could be so dear and fetch my coffee package from the shop.',
        'money'     : 'Take that money from the table, it should be enough.',
        'coffee'    : 'With some money you could go and buy it from the shop if you do not mind.',
        'trade'     : 'Get me some coffee and I will give the upstairs passkey.',
        'passkey'   : 'It will unlock the upstairs door.',
        'count'     : 'Ah well, set in his ways. Not the same after they locked the countess upstairs.',
        'locked'    : 'Yes, maybe I should not say anything. I got the passkey, though.',
        'countess'  : 'Lost her mind, poor thing. Not surprising after seeing what they did to that poor man.',
        'stablehand'       : 'I should not say anything. The count forbade it.'
    },
    'stablehand' : {
        'name'          : 'Chris.',
        'job'           : 'I-a I work at the stables.',
        'horses'        : 'They were ummm..., sold a while ago',
        'knife'         : 'Knife, what knife?',
        'bloodstains'   : 'it is uhhh, a pig we slaughtered. Yesterday.',
        'rag'           : 'Oh this, umm, nothing. Just have a flu, me.'
    },
    'count' : {
        'name' : 'You may call me The Count',
        'job' : 'I govern these parts.',
        'countess' : 'I am afraid that is a topic not to be discussed among starngers. Suffice to say she is unwell at present and rests upstairs.',
        'stablehand' : 'I cannot fathom how I could manage how I could manged without Chris! Indispensable, that man.',
        'cook' : 'She is not very trustworthy, I am afraid. I would have let her go were it not for the delicate condition of the countess.'
    },
    'countess' : {
        'name' : 'I am- I am. Lady Alise.',
        'job' : 'Sighhhh.',
        'count' : 'He is half evil, locked me here.',
        'spearhead' : 'Half of a whole it is, and other half is not here.',
        'need' : 'What need I? To see, to see myself truthfully again.'
    },

}