
import os
from transaction import Transaction
from brick import Brick
from filerepository import FileRepository
from chain import Chain


if __name__ == '__main__':
    chain_path = os.path.join(os.path.split(os.path.abspath(__file__))[0], "chain")
    repo = FileRepository(chain_path)
    transaction = Transaction("sender", "receiver", "Is a generic constructor that takes the string name of the desired algorithm as its first parameter.")
    chain = Chain()
    chain.link_repository(repo)
    chain.add_transaction(transaction)
