#Mining for this tiny coin

import ProofOfWork
from Transaction import transaction_list
from Blockchain import blockchain

from flask import Flask
from flask import request
from flask import Blueprint

#defining api for exporting modules
mining_api = Blueprint('mining_api', __name__)


@mining_api.route('/mine', methods = ['GET'])
def mine():
    #Last proof of work
    last_block = blockchain[len(blockchain) - 1]
    last_proof = last_block.data['proof-of-work']

    #The program will be stuck here
    #until a new valid proof of work
    #is found
    proof = proof_of_work(last_proof)

    #Once the proof is valid, new block
    #can be added and miner can be rewarded
    transaction_list.append(
        {"from": "network-reward", "to": miner_address, "amount" : 1}
    )

    #Data needed to create a new block
    new_block_data = {
        "proof-of-work": proof,
        "transactions": list(transaction_list)
    }
    new_block_index = last_block_index + 1
    new_block_timestamp = this_timestamp = datetime.datetime.now()
    last_block_hash = last_block.hash

    #Clear the transaction list
    transaction_list[:] = []

    #New block
    mined_block = Block(
        new_block_index,
        new_block_timestamp,
        new_block_data,
        last_block_hash
    )
    blockchain.append(mined_block)

    #Response for new block mined
    return json.dumps({
        "index" : new_block_index,
        "timestamp" : str(new_block_timestamp),
        "data" : new_block_data,
        "hash" : last_block_hash
    }) + "\n"
