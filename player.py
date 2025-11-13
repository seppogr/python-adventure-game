from Place import *

class Player:
    """edustaa pelaajaa"""
    def __init__(self, points, currentPlace, currentPlaceIndex, inventory):
        self.points = points
        self.currentPlace = currentPlace
        self.currentPlaceIndex = currentPlaceIndex
        self.inventory = []
        for e in inventory:
            self.add_to_inventory(e)

    def get_points(self):
        return self.points

    def get_current_place(self):
        return self.currentPlace

    def get_placeIndex(self):
        return self.currentPlaceIndex

    def get_inventory(self):
        return self.inventory

    def set_points(self, points):
        self.points = points

    def set_current_place(self, currentPlace):
        self.currentPlace = currentPlace

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

    def __str__(self):
        return f'{self.points}'

# initialise main character with default values
MainChar = Player(0, Inn, 0, ['ball', 'book'])