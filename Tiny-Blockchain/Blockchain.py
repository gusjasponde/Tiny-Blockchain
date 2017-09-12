import hashlib
import json
import datetime
import Util

#Defining the block into our blockchain
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp.isoformat()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block().encode('utf8')

    def hash_block(self):
        sha = hashlib.sha256()
        blkstr = (str(self.index) +
                  str(self.timestamp) +
                  str(self.data) +
                  str(self.previous_hash))
        sha.update(blkstr.encode('utf-8'))
        return sha.hexdigest()

    def reprJSON(self):
        return dict(index=self.index, timestamp=self.timestamp, data=self.data, previous_hash=self.previous_hash, hash=self.hash)

#Genesis block creator
def create_genesis_block():
    return Block(0, datetime.datetime.now(), "Genesis block", "0")

def next_block(last_block):
    this_data = json.dumps({
        "proof-of-work": last_block.index + 1,
        "transactions": "Initial block"
    })
    return Block(last_block.index + 1, datetime.datetime.now(), this_data, last_block.hash)


#Code for running the blockchain
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

genesis_blocks_qty = 10

#adding blocks in the whole chain
for i in range(0, genesis_blocks_qty):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    print "Block #",block_to_add.index," added"
    print "Hash: ",block_to_add.hash
