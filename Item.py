class Item:
    def __init__(self, name, description, synonym):
        self.name = name
        self.description = description
        self.synonym = synonym

Lamp = Item ('lamp', 'An oil lamp. Gives bright light. ', 'a brightly illuminating lamp')

Key = Item('key', 'An old key. Opens the basement door.', 'a key to the basement door')

Book = Item('book', 'An ominous black-bound tome. Written by Abdul Alhazred.', ' the necronomicon')

Rod = Item('rod', 'A rod for fishing. You feel confident that you will catch a really big fish with this one.', 'a fishing rod')

Mask = Item('mask', 'A mask designed for protecting your eyes when welding. Probably useful when staring at other harmful things too.', 'a welding mask')

Fish = Item('fish', 'Not the biggest fish you have ever caught, but nothing prevents you from telling it is.', 'a fresh fish')

Money = Item('money', 'Some coins in a pouch, enough for a tin of coffee.', 'a pouch of coins')

Coffee = Item('coffee', 'A tin of coffee. Will last for at least a couple of days.', 'an unopened tin of coffee')

Shovel = Item('shovel', 'A sturdy and reliable shovel. Good for digging.', 'a good metal shovel')

Circle = Item('circle', 'A small metal circle. Looks like it has some indentations and could be combined with some other similar objects.', 'a metal circle')

Note = Item('note', 'The note reads: "A, bury yours somewhere. It is not safe for us to keep them combined until tonight. I will hide mine. --C PS. Get the book from the guardian somehow!"', 'a piece of paper with some writing')

Knife = Item('knife', 'A long knife with a sharp edge. It is clear that somebody has tried to wash the stains away quite recently.', 'a wicked, blood-stained knife')

Rag = Item('rag', 'A red-stained rag. Blood, maybe?', 'a stained rag')

Letter = Item('letter', 'C! Did what you asked. Are you sure your part is safe with her. She IS a bit unreliable, if you know what I mean. --A', 'a short letter addressed to someone with initial "C"')

Mirror = Item('mirror', 'A very normal mirror. The reflection is clear and the surfaced unstained.', 'an ordinary looking-glass')

Passkey = Item('passkey', 'A key to unlock the upstairs door in the manor.', 'the manor upstairs key')

Spearhead = Item('spearhead', 'An ancient spearhead. Upon closer inspection, some small parts in the edges have seen use recently and shine in an uncomfortable way.', 'an evil-looking spearhead')

Symbol = Item('symbol', 'A strange symbol combining circle and spearhead. You guess it has some religious signifigance, but you would not classify it as "holy".', 'an evil symbol')

No_item = Item('', '', '')

Items = [Lamp, Key, Book, Rod, Mask, Fish, Money,
         Coffee, Shovel, Circle, Note, Knife, Rag,
         Letter, Mirror, Passkey, Spearhead, Symbol]

readables_as_string = ['note']
# items = {
#     'lamp' : {
#         'description': 'An oil lamp.',
#         'synonym': 'a brightly illuminating lamp'
#     },
#     'key' : {
#         'description': 'A bog old key. Opens the basement door.',
#         'synonym' : 'a key to the basement door'
#     },
#     'book' : {
#         'description': 'An ominous black-bound tome. Written by Abdul Alhazred.',
#         'synonym' : ' the necronomicon'
#     },
#     'rod' : {
#         'description' : 'A rod for fishing. You feel confident that you will catch a really big fish with this one.',
#         'synonym' : 'a fishing rod'
#     },
#     'mask' : {
#         'description' : 'A mask designed for protecting your eyes when welding. Probably useful when staring at other harmful things too.',
#         'synonym' : 'a welding mask'
#     },
#     'fish' : {
#         'description' : 'Not the biggest fish you have ever caught, but nothing prevents you from telling it is.',
#         'synonym' : 'a fresh fish'
#     },
#     'money' : {
#         'description' : 'Some coins in a pouch, enough for a tin of coffee.',
#         'synonym' : 'a pouch of coins'
#     },
#     'coffee' : {
#         'description' : 'A tin of coffee. Will last for at least a couple of days.',
#         'synonym' : 'an unopened tin of coffee'
#     },
#     'shovel' : {
#         'description' : 'A sturdy and reliable shovel. Good for digging.',
#         'synonym' : 'a shovel'
#     },
#     'circle' : {
#         'description' : 'A small metal circle. Looks like it has some indentations and could be combined with some other similar objects.',
#         'synonym' : 'a metal circle'
#     },
#     'note': {
#         'description' : 'The note reads: "A, bury yours somewhere. It is not safe for us to keep them combined until tonight. I will hide mine. --C PS. Get the book from the guardian somehow!"',
#         'synonym' : 'a piece of paper with some writing'
#     },
#     'knife' : {
#         'description' : 'A long knife with a sharp edge. It is clear that somebody has tried to wash the stains away quite recently.',
#         'synonym' : 'a wicked, blood-stained knife'
#     },
#     'rag' : {
#         'description' : 'A red-stained rag. Blood, maybe?',
#         'synonym' : 'a stained rag'
#     },
#     'letter' : {
#         'description' : 'C! Did what you asked. Are you sure your part is safe with her. She IS a bit unreliable, if you know what I mean. --A',
#         'synonym' : 'a short letter addressed to someone with initial "C"'
#     },
#     'mirror' : {
#         'description' : 'A very normal mirror. The reflection is clear and the surfaced unstained.',
#         'synonym' : 'an ordinary looking-glass'
#     },
#     'passkey' : {
#         'description' : 'A key to unlock the upstairs door in the manor.',
#         'synonym' : 'the manor upstairs key'
#     },
#     'spearhead' : {
#         'description' : 'An ancient spearhead. Upon closer inspection, some small parts in the edges have seen use recently and shine in an uncomfortable way.',
#         'synonym' : 'an evil-looking spearhead'
#     },
#     'symbol' : {
#         'description' : 'A strange symbol combining circle and spearhead. You guess it has some religious signifigance, but you would not classify it as "holy".',
#         'synonym' : 'an evil symbol'
#     }
# }