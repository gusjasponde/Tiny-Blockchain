#Naive proof of work
#Keep incrementing until the number
#is divisible by 23

#Note this algorithm can be improved later

def proof_of_work(last_proof):
    incrementor = last_proof + 1
    while not(incrementor % 23 == 0 and incrementor % last_proof == 0):
        incrementor += 1

    return incrementor #as proof of work
