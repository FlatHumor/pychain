
import os
from transaction import Transaction
from brick import Brick
from filerepository import FileRepository
from chain import Chain


if __name__ == '__main__':
    chain_path = os.path.join(os.path.split(os.path.abspath(__file__))[0], "chain")
    repo = FileRepository(chain_path)
    transaction = Transaction("sender", "receiver", "transaction content")
    chain = Chain()
    chain.link_repository(repo)
    if chain.is_valid():
        chain.add_transaction(transaction)
