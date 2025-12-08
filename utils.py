# A collection of small utility functions that are
# used throughout the program
import sys
from Item import Items

def extract_list(list_of_items):
    return str(' '.join([str(item) for item in list_of_items]))

def extract_object_list(object_list):
    object_list_extracted = []
    for item in object_list:
        object_list_extracted.append(item.name)
    return object_list_extracted

def fetch_item_object_by_value(noun):
    for item in Items:
        if item.name == noun:
            return item


# prints the available topcis for conversation
# with the character in the current room

def npc_topics(list):
    chat_list = [*list]
    show_this_amount_of_topics = len(chat_list)
    conversation_topics = ''
    for item in range(0, show_this_amount_of_topics):
        conversation_topics+= chat_list[item] + ' '
    return conversation_topics

readables =['note']