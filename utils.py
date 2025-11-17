# A collection of small utility functions that are
# used throughout the program

def extract_list(list_of_items):
    return str(' '.join([str(item) for item in list_of_items]))


# prints the available topcis for conversation
# with the character in the current room

def npc_topics(list):
    chat_list = [*list]
    show_this_amount_of_topics = len(chat_list)
    conversation_topics = ''
    for item in range(0, show_this_amount_of_topics):
        conversation_topics+= chat_list[item] + ' '
    return conversation_topics
