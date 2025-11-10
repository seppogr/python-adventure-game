# A collection of small utility functions that are
# used throughout the program

def extractList(listOfItems):
    return str(' '.join([str(item) for item in listOfItems]))

def npcTopics(list):
    chatList = [*list]
    s = ''
    for item in range(0, len(chatList) - 3):
        s += chatList[item] + ' '
    return s
