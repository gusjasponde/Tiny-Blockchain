import Blockchain
from flask import Flask
from flask import request
from flask import Blueprint

#Exporting blueprint
consensus_api = Blueprint('consensus_api', __name__)

@consensus_api.route('/chain', methods=['GET'])
def get_blocks():
    chain_to_send = blockchain

    #Blocks become dictionaries
    for block in chain_to_send:
        block_index = str(block.index)
        block_timestamp = str(block.timestamp)
        block_data = str(block.data)
        block_hash = block.hash
        block = {
            "index": block_index,
            "timestamp": block_timestamp,
            "data": block_data,
            "hash": block_hash
        }

    #Send our requested chain
    chain_to_send = json.dumps(chain_to_send)
    return chain_to_send
