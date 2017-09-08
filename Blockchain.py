import hashlib

#Defining the block into our blockchain
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.hash = self.hash_block()

        def hash_block(self):
            sha = hashlib.sha256()
            sha.update(str(self.index) +
                   str(self.timestamp) +
                   str(self.data) +
                   str(self.previous_hash))
            return sha.hexdigest()


#Genesis block creator
import datetime
def create_genesis_block():
    return Block(0, datetime.datetime.now(), "Genesis block", "0")

def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = datetime.datetime.now()
    this_data = "Block " + str (this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)
