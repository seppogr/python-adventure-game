# A collection of small utility functions that are
# used throughout the program

def extractList(listOfItems):
    return str(' '.join([str(item) for item in listOfItems]))


# 4 is magic number here because the last FOUR keys in the
# npcs[character] dictionary in npcs.py are not meant to be revealed
# to the player as converstaion topics.

def npcTopics(list):
    chatList = [*list]
    showThisAmountOfTopics = len(chatList) - 4
    conversationTopics = ''
    for item in range(0, showThisAmountOfTopics):
        conversationTopics+= chatList[item] + ' '
    return conversationTopics
