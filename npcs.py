# A dictionary of various non-player characters encountered n the game.
# Keys represent different conversation topics and values what the npc has to say about it.
# Last four key-value pairs are invisible to the player and used in marking the quests
# progression and npc inventory and other data not meant as a conversation topic.

npcs = {
    'default' : {

    },
    'innkeeper': {
        'name' : 'I am Alfred the innkeeper.',
        'job' : 'Yes, I AM the innkeeper.',
        'mission' : 'There is a book in the basement. Can you bring it to me.',
        'key' : 'You will need this key to open the basement door.',
        'lamp' : 'The grue in the basement is afraid of light. This lamp will help you.',
        'grue' : 'Well, I am afraid the basement is home to a grue.',
        'basement' : 'Yes, the basement is our wine cellar.',
        'book' : 'The count left it there',
        'description' : 'A middle-aged man with a beard and a worried look on his face. Probably wants to talk to you about something.',
        'wants' : 'book',
        'items' : ['key'],
        'greeting' : 'Hello traveler',
    },
    'grue' : {
        'grue' : 'I am GRUE!!!',
        'mission' : 'What a nice lamp you have, please give it to me!',
        'book' : 'It says NECRONOMICON on the cover. A bit shady if you ask me.',
        'description' : 'A sharp-toothed monster. Likely you will get eaten by it.',
        'wants' : 'lamp',
        'items' : [],
        'greeting' : 'Graugh!!!'
    }
}