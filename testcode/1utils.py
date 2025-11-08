from places import places
from Player import player

# prints the start story on screen
# todo a lot!!!
def showStart():
    print("Majatalon isäntä on huhuillut sinut sisään. Hän vaikuttaa hermostuneelta.")
    print()

# prints the player place
def showStory():
    print(f"{places[player['placeIndex']]['story']}")
    print()

# set player place in the room they have entered
def setPlayerPlace(place, index):
    player['place'] = place
    player['placeIndex'] = index

# palauttaa paikkaindeksin eri paikoille
def getPlayerPlaceIndex(place):
    if place == 'inn':
        return 0
    elif place == 'basement':
        return 1
    elif place == 'plaza':
        return 2
    elif place == 'attic':
        return 3
    elif place == 'smithy':
        return 4
    elif place == 'shop':
        return 5
    elif place == 'trail':
        return 6
    elif place == 'manor':
        return 7
    elif place == 'stables':
        return 8
    elif place == 'hall':
        return 9
    elif place == 'study':
        return 10
    elif place == 'upstairs':
        return 11
    elif place == 'kitchen':
        return 12
    elif place == 'hut':
        return 13
    elif place == 'beach':
        return 14
    elif place == 'churchyard':
        return 15
    elif place == 'forest':
        return 16
    elif place == 'church':
        return 17
    elif place == 'crypt':
        return 18
    elif place == 'dungeon':
        return 19