import Blockchain
from flask import Flask
from flask import request
from flask import Blueprint

#Exporting blueprint
consensus_api = Blueprint('consensus_api', __name__)

@consensus_api.route('/chain', methods=['GET'])
def get_chain():
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

def find_new_chains():
    #Get others nodes blockchains
    other_chains = []
    for node_url in peer_nodes:
        block = requests.get(node_url + "/blocks").content

        #Converting Json to dictionary for easy
        #manipulation
        block = json.loads(block)

        #add to chains list
        other_chains.append(block)
    return other_chains
