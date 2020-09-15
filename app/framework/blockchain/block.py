from time import time
import json
import hashlib

class Block:
    def __init__(self, index, chain: list, transaction: list, proof, previous_hash=None):
        self.chain = chain
        self.index = len(self.chain) + 1
        self.timestamp = time()
        self.transaction = transaction
        self.proof = proof
        self.previous_hash = previous_hash or self.hash(chain[-1])
    
    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block
        :param block: <dict> Block
        :return: <str>
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()