class Item:
    def __init__(self, name, description, synonym):
        self.name = name
        self.description = description
        self.synonym = synonym

Lamp = Item('lamp', 'An oil lamp. Gives bright light. ', 'a brightly illuminating lamp')

Key = Item('key', 'An old key. Opens the basement door.', 'a key to the basement door')

Book = Item('book', 'An ominous black-bound tome. Written by Abdul Alhazred.', ' the necronomicon')

Rod = Item('rod', 'A rod for fishing. You feel confident that you will catch a really big fish with this one.', 'a fishing rod')

Mask = Item('mask', 'A mask designed for protecting your eyes when welding. Probably useful when staring at other harmful things too.', 'a welding mask')

Fish = Item('fish', 'Not the biggest fish you have ever caught, but nothing prevents you from telling it is.', 'a fresh fish')

Money = Item('money', 'Some coins in a pouch, enough for a tin of coffee.', 'a pouch of coins')

Coffee = Item('coffee', 'A tin of coffee. Will last for at least a couple of days.', 'an unopened tin of coffee')

Shovel = Item('shovel', 'A sturdy and reliable shovel. Good for digging.', 'a good metal shovel')

Circle = Item('circle', 'A small metal circle. Looks like it has some indentations and could be combined with some other similar objects.', 'a metal circle')

Note = Item('note', 'The note reads: "A, bury yours somewhere. It is not safe for us to keep them combined until tonight. I will hide mine.\n --C\n PS. Get the book from the guardian somehow!"', 'a piece of paper with some writing')

Knife = Item('knife', 'A long knife with a sharp edge. It is clear that somebody has tried to wash the stains away quite recently.', 'a wicked, blood-stained knife')

Rag = Item('rag', 'A red-stained rag. Blood, maybe?', 'a stained rag')

Letter = Item('letter', 'C! Did what you asked. Are you sure your part is safe with her. She IS a bit unreliable, if you know what I mean.\n --A', 'a short letter addressed to someone with initial "C"')

Mirror = Item('mirror', 'A very normal mirror. The reflection is clear and the surfaced unstained.', 'an ordinary looking-glass')

Passkey = Item('passkey', 'A key to unlock the upstairs door in the manor.', 'the manor upstairs key')

Spearhead = Item('spearhead', 'An ancient spearhead. Upon closer inspection, some small parts in the edges have seen use recently and shine in an uncomfortable way.', 'an evil-looking spearhead')

Symbol = Item('symbol', 'A strange symbol combining circle and spearhead. You guess it has some religious signifigance, but you would not classify it as "holy".', 'an evil symbol')

Newspaper = Item('newspaper', 'A local newspaper full of old articles, you almost throw it away until your eyes spot something interesting. And ominous.\n "STRANGE DISAPPEARANCE\n A headless body found!!!"\n The rest is torn away.', 'an old local newspaper')

Ladder = Item('ladder', 'A sturdy, portable ladder. Useful for reaching high spots.', 'a wooden ladder')

Evidence = Item('evidence', 'A strong case against the Count, the Innkeeper, and the Stablehand. But is it strong enough? You guess not enough to confront them directly, but someone honest could be convinced...', 'evidence')

No_item = Item('', '', '')

Items = [Lamp, Key, Book, Rod, Mask, Fish, Money,
         Coffee, Shovel, Circle, Note, Knife, Rag,
         Letter, Mirror, Passkey, Spearhead, Symbol,
         Newspaper, Ladder, Evidence]

readables_as_string = ['note', 'newspaper']
