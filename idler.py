import random
from printer import *
from colours import idler_colour_list


idler_verbs = ['mention', 'remark', 'state', 'whisper',
              'murmur', 'mutter', 'grumble', 'mumble',
              'croak', 'shout', 'yell', 'scream',
              'bellow', 'holler']

idler_adverbs = ['softly', 'loudly', 'calmly', 'sternly', 'politely', 'cheerfully',
                 'sarcastically', 'seriously', 'boldly', 'confidentially', 'clearly',
                 'abruptly', 'vaguely', 'frankly', 'directly', 'persuasively']

idler_sayings = ['The town horse radiates warmth!', 'I think the swamp is round.', 'Everyone stares at the plaza.',
             'There is no room for thought in my bag.', 'Fishing is good for health.', 'I can dream in blue.',
             'I think there is a dungeon beneath the church.']

def idler_speaks():
    random.seed()
    idler_verb = idler_verbs[random.randint(0, len(idler_verbs) - 1)]
    verb_colour = idler_colour_list[random.randint(0, len(idler_colour_list) -1)]
    idler_adverb = idler_adverbs[random.randint(0, len(idler_adverbs) -1)]
    adverb_colour = idler_colour_list[random.randint(0, len(idler_colour_list) -1)]
    idler_saying = idler_sayings[random.randint(0, len(idler_sayings) - 1)]
    saying_colour = idler_colour_list[random.randint(0, len(idler_colour_list) -1)]
    print_text_slowly(f'The idler {print_in_colour(idler_verb + 's', verb_colour)} {print_in_colour(idler_adverb, adverb_colour)}: "{print_in_colour(idler_saying, saying_colour)}"')
