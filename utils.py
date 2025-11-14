# A collection of small utility functions that are
# used throughout the program

def extractList(listOfItems):
    return str(' '.join([str(item) for item in listOfItems]))


# prints the available topcis for conversation
# with the character in the current room

def npcTopics(list):
    chatList = [*list]
    showThisAmountOfTopics = len(chatList)
    conversationTopics = ''
    for item in range(0, showThisAmountOfTopics):
        conversationTopics+= chatList[item] + ' '
    return conversationTopics
