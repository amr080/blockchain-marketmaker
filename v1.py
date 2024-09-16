import hashlib
import time

class Block:
    def __init__(self, index, timestamp, transactions, prev_hash):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions  # Trade orders
        self.prev_hash = prev_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        tx_str = ''.join(self.transactions)
        block_string = f"{self.index}{self.timestamp}{tx_str}{self.prev_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.genesis_block()]

    def genesis_block(self):
        return Block(0, time.time(), ["Genesis Block"], "0")

    def latest_block(self):
        return self.chain[-1]

    def add_block(self, transactions):
        index = self.latest_block().index + 1
        timestamp = time.time()
        prev_hash = self.latest_block().hash
        new_block = Block(index, timestamp, transactions, prev_hash)
        self.chain.append(new_block)

# Demo
bc = Blockchain()
bc.add_block(["BUY 100 AAPL @ 150"])
bc.add_block(["SELL 50 GOOGL @ 2800"])

for block in bc.chain:
    print(f"Block {block.index} [{block.hash[:8]}]: {block.transactions}")
