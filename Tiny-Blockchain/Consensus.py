import Blockchain
from Blockchain import blockchain

from flask import Flask
from flask import request
from flask import Blueprint

import json

#Exporting blueprint
consensus_api = Blueprint('consensus_api', __name__)

@consensus_api.route('/chain', methods=['GET'])
def get_chain():
    chain_to_send = blockchain

    #Blocks become dictionaries
    for block in chain_to_send:
        chain_to_send.append(json.loads(block))
    print chain_to_send

    #Send our requested chain
    chain_to_send = json.dumps(chain_to_send)
    return chain_to_send

def find_new_chains():
    #Get others nodes blockchains
    other_chains = []
    for node_url in peer_nodes:
        block = requests.get(node_url + "/blocks").content

        #Converting Json to dictionary for easy manipulation
        block = json.loads(block)

        #add to chains list
        other_chains.append(block)
    return other_chains

def consensus():
    #Get blocks from other nodes
    other_chains = find_new_chains()

    #If this node's chain is not the longest, store the longest
    longest_chain = blockchain
    for chain in other_chains:
        if len(longest_chain) < len(chain):
            longest_chain = chain

    blockchain = longest_chain
