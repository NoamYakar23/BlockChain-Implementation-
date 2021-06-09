import hashlib
from ppretty import ppretty

class Block:
    def __init__(self, index, t_stamp, data, prev_hash = ''):
        self.index = index
        self.t_stamp = t_stamp
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.hashify
        self.nonce = 0
    def hashify(self):
        input_str = str(self.index) + str(self.prev_hash) + str(self.data) + str(self.nonce)
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
class BlockChain:
    def __init__(self):
        self.chain = [self.genesis_initiation()]
        self.difficulty = 5
        self.nonce = 0
    def genesis_initiation(self):
        return Block(0, "08/04/2003", "First Block", "1")

    def get_latest_block(self):
        return self.chain[len(self.chain)-1]

    def add_block(self, new_block):
        new_block.prev_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

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
noamcoin.add_block(Block(1, "07/12/1998", "5 added coins"))
noamcoin.add_block(Block(2, "01/03/1989", "20 added coins"))

print("Valid Block Chain? " + str(noamcoin.verify_chain_integrity()))

print(ppretty(noamcoin))
