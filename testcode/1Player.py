# player data

# points: gained points are stored here
# place: name of the current room
# placeIndex: index number of the room, is set to the index of the room in the 'places' list
# inventory: itmes carried by the player

player = {'points': 0,
           'place' : '',
           'placeIndex': 0,
           'inventory': []}


class Player:
    """edustaa pelaajaa"""
    def __init__(self, points, place, placeIndex, inventory):
        self.points = points
        self.place = place
        self.placeIndex = placeIndex
        self.inventory = []
        for e in inventory:
            self.add_to_inventory(e)

    def get_points(self):
        return self.points

    def get_place(self):
        return self.place

    def get_placeIndex(self):
        return self.placeIndex

    def get_inventory(self):
        return self.inventory

    def set_points(self, points):
        self.points = points

    def set_place(self, place):
        self.place = place

    def set_placeIndex(self, placeIndex):
        self.placeIndex = placeIndex

    def add_to_inventory(self, item):
        if item not in self.inventory:
            self.inventory.append(item)

    def remove_from_inventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        else:
            return False

    def printInventory(self):
        if self.inventory:
            print('you have...')
            for item in self.inventory:
                print(f'- {item}')
        else:
            print(f'Inventory is empty')