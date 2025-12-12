from Place import *
from printer import *

class Player:
    def __init__(self, points, current_place, follower, inventory, life_status):
        self.points = points
        self.current_place = current_place
        self.follower = follower
        self.inventory = []
        for e in inventory:
            self.add_to_inventory(e)
        self.life_status = life_status

    def get_points(self):
        return self.points

    def get_current_place(self):
        return self.current_place

    def get_follower(self):
        return self.follower

    def set_follower(self, follower):
        self.follower = follower

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
            print_text_slowly('you have...')
            for item in self.inventory:
                print_text_slowly(f'- {item.name}')
        else:
            print_text_slowly(f'You are carrying nothing.')

    def set_life_status(self, life_status):
        self.life_status = life_status

    def get_life_status(self):
        return self.life_status

    def __str__(self):
        return f'{self.points}'

# initialise main character with default values
# (points gained, starting place, follower, inventory, is alive)
MainChar = Player(0, Plaza, '', [], True)