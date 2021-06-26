import hashlib
from ppretty import ppretty
import time
from datetime import datetime

#for transaction puproses
now = datetime.now().strftime("%H:%M:%S")
print(now)

class Block:
    def __init__(self, transactions, t_stamp, prev_hash = ''):
        self.t_stamp = t_stamp
        self.transactions = transactions
        self.prev_hash = prev_hash
        self.hash = self.hashify
        self.nonce = 0
    def hashify(self):
        input_str = str(self.prev_hash) + str(self.nonce)
        return hashlib.sha256(input_str.encode('utf-8')).hexdigest()

    def mine_block(self,difficulty):
        hash_string = str(self.hashify())
        string = ""
        for i in range(difficulty):
            string += "0"

        while(hash_string[0:difficulty] != string):
            self.nonce+=1
            hash_string = self.hashify()


        print('Mined Block: ' + str(hash_string))
class Transactions:
    def __init__(self, from_address, to_address, amount):
        self.from_address = from_address
        self.to_address = to_address
        self.amount = amount
class BlockChain:
    def __init__(self):
        self.chain = [self.genesis_initiation()]
        self.difficulty = 2
        self.nonce = 0
        self.pending_transactions = []
        self.mining_reward = 5
    def genesis_initiation(self):
        return Block("08/04/2003", "First Block", "0")

    def get_latest_block(self):
        return self.chain[len(self.chain)-1]

    def mine_pending_transactions(self, mining_reward_address):
        block = Block(now, self.pending_transactions)
        block.mine_block(self.difficulty)

        print('Block succesfully mined!')

        self.chain.append(block)

        self.pending_transactions = [Transactions(None, mining_reward_address, self.mining_reward)]
    def create_transaction(self,transaction):
        self.pending_transactions.append(transaction)

    def get_address_balance(self,address):
        balance = 0
        for block in self.chain:
            for transactions in block.transactions:
                if(transactions.from_address == address):
                    balance -= transactions.amount
                if (transactions.from_address == address):
                    balance += transactions.amount

        return balance

    def verify_chain_integrity(self):
        #dont start with block 0, block 0 is the genesis block
        bool = True
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            prev_block = self.chain[i-1]

            if(current_block.hash != current_block.hashify):
                bool = False

            prev_block_hash = prev_block.hashify()
            current_block_hash = current_block.hashify()

            for i in range(len(prev_block_hash)):
                if current_block_hash[i] == prev_block_hash[i]:
                    continue
                else:
                    break
                    bool = False

        print(type(prev_block.hashify))
        print(type(current_block.prev_hash))
        return bool








noamcoin = BlockChain()
noamcoin.create_transaction(Transactions('address_one', 'address_two', 10))
noamcoin.create_transaction(Transactions('address_two', 'address_one', 5))


print('\n Miner starting')
noamcoin.mine_pending_transactions('bens-address')
print('\n Balance of bens address is', noamcoin.get_address_balance('bens-address'))

print(ppretty(noamcoin))
