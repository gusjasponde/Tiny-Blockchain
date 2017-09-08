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

