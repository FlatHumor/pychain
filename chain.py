import hashlib
from brick import Brick
from transaction import Transaction

class Chain(object):

    DEFAULT_HASH = "E175E69A8312A66A7011C1DCCFC2CF69823BC2C52F58CA516F60698F02DAA1D6"

    def __init__(self):
        self.repository = None

    def link_repository(self, repository):
        self.repository = repository
        self.repository.on_link()

    def unlink_repository(self):
        self.repository = None

    def add_transaction(self, transaction):
        if self.repository is None:
            return
        prev_brick_number = 0
        curr_brick_number = 0
        prev_hash = Chain.DEFAULT_HASH
        prev_brick = self.get_previous_brick()
        if prev_brick is not None:
            # prev_brick_number = prev_brick.ident
            prev_hash = prev_brick.head_hash
            curr_brick_number = prev_brick.ident + 1
        curr_brick = Brick(ident=curr_brick_number, prev_hash=prev_hash, transaction=transaction)
        curr_brick_guess = curr_brick.get_guess()
        curr_brick.head_hash = self.build_hash(curr_brick_guess)
        self.calculate_nonce(curr_brick)
        self.repository.save_brick(curr_brick)
        
    def calculate_nonce(self, brick):
        while not self.check_nonce(brick.head_hash, brick.nonce, brick.bits):
            brick.nonce += 1

    def check_nonce(self, head_hash, nonce, bits):
        proof = "%s%s" % (head_hash, nonce)
        hash = self.build_hash(proof)
        first_bits = hash[0:len(bits)]
        return first_bits == bits

    def build_hash(self, guess):
        return hashlib.sha256(guess.encode()).hexdigest()

    def get_previous_brick(self):
        brick_numbers = self.repository.get_identificators()
        if len(brick_numbers) > 0:
            prev_brick_number = brick_numbers[-1]
            return self.repository.load_brick(prev_brick_number)

    def is_valid(self):
        brick_numbers = self.repository.get_identificators()
        if len(brick_numbers) is 0:
            return True
        prev_hash = Chain.DEFAULT_HASH
        brick = None
        transaction_guess = None
        brick_guess = None
        brick_hash = None
        for brick_number in brick_numbers:
            brick = self.repository.load_brick(brick_number)

            if brick_number == brick_numbers[0]:
                prev_hash = brick.head_hash
                continue
            
            # transaction_guess = brick.transaction.get_guess()
            brick_guess = brick.get_guess()
            brick_hash = self.build_hash(brick_guess)

            if brick.head_hash != brick_hash:
                print('VALIDATION FAILED ON HASH RECALCULATION')
                return False

            if brick.prev_hash != prev_hash:
                print('VALIDATION FAILED ON LINK CHECKING')
                print("BRICK # %s" % brick.ident)
                return False

            if not self.check_nonce(brick.head_hash, brick.nonce, brick.bits):
                print('VALIDATION FAILED ON NONCE CHECKING')
                return False

            prev_hash = brick.head_hash
        return True
