from Place import *

class Player:
    """edustaa pelaajaa"""
    def __init__(self, points, current_place, current_place_index, inventory):
        self.points = points
        self.current_place = current_place
        self.current_place_index = current_place_index
        self.inventory = []
        for e in inventory:
            self.add_to_inventory(e)

    def get_points(self):
        return self.points

    def get_current_place(self):
        return self.current_place

    def get_placeIndex(self):
        return self.current_place_index

    def get_inventory(self):
        return self.inventory

    def set_points(self, points):
        self.points = points

    def set_current_place(self, current_place):
        self.current_place = current_place

    def add_to_inventory(self, item):
        if item not in self.inventory:
            self.inventory.append(item)

    def remove_from_inventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        else:
            return False

    def print_inventory(self):
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