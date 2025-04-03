import time
import json
from .block import Block
from .transaction import Transaction
from app.models.blockchain import BlockchainData

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.mining_reward = 0
        self.difficulty = 2
        
        # Load blockchain from database
        self.load_from_database()
        
        # Create genesis block if chain is empty
        if len(self.chain) == 0:
            self.create_genesis_block()
    
    def create_genesis_block(self):
        """
        Create the first block in the chain
        """
        genesis_block = Block(0, time.time(), [], "0")
        self.chain.append(genesis_block)
        self.save_to_database(genesis_block)
        print("Genesis block created.")
        
    def get_latest_block(self):
        """
        Return the most recent block in the chain
        """
        return self.chain[-1]
    
    def add_transaction(self, sender_id, recipient_id, amount, transaction_type):
        """
        Add a new transaction to pending transactions
        """
        transaction = Transaction(sender_id, recipient_id, amount, transaction_type)
        self.pending_transactions.append(transaction)
        return transaction
    
    def mine_pending_transactions(self):
        """
        Create a new block with all pending transactions and add it to the chain
        """
        if not self.pending_transactions:
            return False
            
        block = Block(
            len(self.chain),
            time.time(),
            self.pending_transactions,
            self.get_latest_block().hash
        )
        
        # Mine the block
        block.mine_block(self.difficulty)
        
        # Add the block to the chain and clear pending transactions
        self.chain.append(block)
        self.pending_transactions = []
        
        # Save block to database
        self.save_to_database(block)
        
        return block
    
    def is_chain_valid(self):
        """
        Check if the blockchain is valid
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            # Check if the current block's hash is valid
            if current_block.hash != current_block.calculate_hash():
                return False
                
            # Check if the current block points to the correct previous hash
            if current_block.previous_hash != previous_block.hash:
                return False
                
        return True
    
    def get_balance(self, address):
        """
        Calculate the balance of an address by going through all transactions
        """
        balance = 0
        
        # Go through all blocks
        for block in self.chain:
            for tx in block.transactions:
                # If the address is the sender, subtract the amount
                if tx.sender_id == address and tx.transaction_type == 'donation':
                    balance -= tx.amount
                    
                # If the address is the recipient, add the amount (for donations)
                if tx.recipient_id == address and tx.transaction_type == 'donation':
                    balance += tx.amount
                    
                # If the address is the sender for spending, subtract the amount
                if tx.sender_id == address and tx.transaction_type == 'spending':
                    balance -= tx.amount
                    
        return balance
    
    def get_address_transactions(self, address):
        """
        Get all transactions for a specific address
        """
        transactions = []
        
        # Go through all blocks
        for block in self.chain:
            for tx in block.transactions:
                # If the address is sender or recipient, add the transaction
                if tx.sender_id == address or tx.recipient_id == address:
                    transactions.append(tx)
                    
        return transactions
    
    def get_charity_spending(self, charity_address):
        """
        Get all spending transactions for a specific charity
        """
        spending = []
        
        # Go through all blocks
        for block in self.chain:
            for tx in block.transactions:
                # If the charity is the sender and transaction type is spending
                if tx.sender_id == charity_address and tx.transaction_type == 'spending':
                    spending.append(tx)
                    
        return spending
        
    def save_to_database(self, block):
        """
        Save a block to the database
        """
        from app import db
        block_data = BlockchainData.from_dict(block.to_dict())
        db.session.add(block_data)
        db.session.commit()
            
    def load_from_database(self):
        """
        Load the blockchain from the database
        """
        from app import db
        blocks = BlockchainData.query.order_by(BlockchainData.block_index).all()
        
        for block_data in blocks:
            block_dict = json.loads(block_data.block_data)
            transactions = [
                Transaction(
                    tx['sender_id'],
                    tx['recipient_id'],
                    tx['amount'],
                    tx['transaction_type']
                ) for tx in block_dict['transactions']
            ]
            
            block = Block(
                block_dict['index'],
                block_dict['timestamp'],
                transactions,
                block_dict['previous_hash'],
                block_dict['nonce']
            )
            block.hash = block_dict['hash']
            self.chain.append(block)

# Global blockchain instance
blockchain = None

def init_blockchain():
    """
    Initialize or load the blockchain
    """
    global blockchain
    blockchain = Blockchain()
    return blockchain

def get_blockchain():
    """
    Get the current blockchain instance
    """
    global blockchain
    if blockchain is None:
        blockchain = init_blockchain()
    return blockchain 