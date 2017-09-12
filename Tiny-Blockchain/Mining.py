#Mining for this tiny coin

from ProofOfWork import proof_of_work
from Transaction import transaction_list
from Transaction import Transaction
from Blockchain import blockchain
from Blockchain import Block

from flask import Flask
from flask import request
from flask import Blueprint

import json
import datetime
from Util import ComplexEncoder

#miner_address
miner_address = "d2958a8e0a1d2ff69c9c74c4e2e1467a3c157d926457345fa4ee2a39e909ba99"

#defining api for exporting modules
mining_api = Blueprint('mining_api', __name__)

@mining_api.route('/debug', methods = ['GET'])
def deb():
    return json.dumps("it works!")

@mining_api.route('/mine', methods = ['GET'])
def mine():
    #Last proof of work
    last_block = blockchain[len(blockchain) - 1]
    last_proof = json.loads(last_block.data)['proof-of-work']

    #The program will be stuck here
    #until a new valid proof of work
    #is found
    proof = proof_of_work(last_proof)

    #Once the proof is valid, new block
    #can be added and miner can be rewarded
    transaction_list.append(
        json.dumps(Transaction("network-reward", miner_address, 1).reprJSON(), cls=ComplexEncoder)
    )

    #Data needed to create a new block
    new_block_data = json.dumps({
        "proof-of-work": proof,
        "transactions": json.dumps(list(transaction_list), cls=ComplexEncoder)
    }, cls=ComplexEncoder)

    #Clear the transaction list
    transaction_list[:] = []

    #New block
    mined_block = Block(
        last_block.index + 1,
        datetime.datetime.now(),
        new_block_data,
        last_block.hash
    )
    blockchain.append(mined_block)

    #Response for new block mined
    return json.dumps(mined_block.reprJSON(), cls=ComplexEncoder) + "\n"
