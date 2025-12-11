proof = { 'knife': False,
         'note' : False,
         'letter' : False,
         'rag' : False
}

proof_conversation = {'knife' : 'A sharp, blade, definintely has traces of blood.',
                      'note' : 'The handwriting looks refined and cultured.',
                      'letter' : 'Familiar handwriting. Must be someone from the village.',
                      'rag' : 'It is coloured by blood.',
                      'symbol' : 'That is an old symbol. I have seen it in the crypt door in church.',
                      'evidence' : 'A strong case, but we need to see them. Let us go to the church and\nsee if we can enter the crypt somehow!\nI heard somewhere there is a crypt under the church.'}

# count how many True vlaues in proof list, returns the amount
def amount_of_found_proof():
    counter = 0
    for item in proof:
        if proof[item]:
            counter += 1
    return counter

# returns the list of proof items currently found, ie keys that have True value in proof list
def return_found_proof():
    proof_list=[]
    for item in proof:
        if proof[item]:
            proof_list.append(item)
    return proof_list

# Check if a key is in proof list, if found sets it to True
def check_if_proof(item):
    if item in proof.keys():
        proof[item] = True
