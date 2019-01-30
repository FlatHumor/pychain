
import os
import sys
from transaction import Transaction
from brick import Brick
from filerepository import FileRepository
from chain import Chain


if __name__ == '__main__':
    chain_path = os.path.join(os.path.split(os.path.abspath(__file__))[0], "chain") 
    sender = "example sender"
    receiver = "example receiver"
    content = "example content"
    if len(sys.argv) == 5:
        chain_path = sys.argv[1]
        sender = sys.argv[2]
        receiver = sys.argv[3]
        content = sys.argv[4]
    repo = FileRepository(chain_path)
    transaction = Transaction(sender, receiver, content)
    chain = Chain()
    chain.link_repository(repo)
    if chain.is_valid():
        chain.add_transaction(transaction)
