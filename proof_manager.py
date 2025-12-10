proof = { 'knife': True,
         'note' : True,
         'letter' : True,
         'rag' : False,
         'symbol' : False
}

proof_conversation = {'knife' : 'A sharp, blade, definintely has traces of blood.',
                      'note' : 'The handwriting looks refined and cultured.',
                      'letter' : 'Familiar handwriting. Must be someone from the village.',
                      'rag' : 'It is coloured by blood.',
                      'symbol' : 'That is an old symbol. I have seen it in the crypt door in church.',
                      'evidence' : 'A strong case, but we need to see them. Let us go to the church and\nsee if we can enter the crypt somehow!\nI heard somewhere there is a crypt under the church.'}

def return_found_proof():
    proof_list = []
    for item in proof:
        if proof[item]:
            proof_list.append(item)

    return proof_list

#print(return_found_proof())