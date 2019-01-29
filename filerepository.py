import os
from repository import Repository
from brick import Brick
from transaction import Transaction


class FileRepository(Repository):

    def __init__(self, path):
        self.path = path
        self.brick_ext = ".brick"
        self.ident = "file_repository"

    def load_brick(self, ident):
        assert isinstance(ident, int)
        filename = self._build_path(ident)
        lines = None
        with open(filename) as brick_file:
            lines = brick_file.readlines()
        if lines:
            ident = int(lines[0].strip())
            head_hash = lines[1].strip()
            prev_hash = lines[2].strip()
            nonce = int(lines[3].strip())
            bits = lines[4].strip()
            brick_ts = int(lines[5].strip())
            sender = lines[6].strip()
            receiver = lines[7].strip()
            content = lines[8].strip()
            transaction_ts = int(lines[9].strip())
            transaction = Transaction(sender, receiver, content, transaction_ts)
            return Brick(ident, head_hash, prev_hash, nonce, bits, brick_ts, transaction)

    def save_brick(self, brick):
        next_ident = 0
        curr_idents = self.get_identificators()
        if len(curr_idents) > 0:
            curr_idents.sort()
            next_ident = curr_idents[-1] + 1
        next_path = self._build_path(next_ident)
        with open(next_path, 'w') as brickfile:
            lines = [
                str(brick.ident),
                str(brick.head_hash),
                str(brick.prev_hash),
                str(brick.nonce),
                str(brick.bits),
                str(brick.timestamp),
                str(brick.transaction.sender),
                str(brick.transaction.receiver),
                str(brick.transaction.content),
                str(brick.transaction.timestamp)
            ]
            for line in lines:
                brickfile.write(line + '\n')

    def get_identificators(self):
        idents = []
        for brick_file in self._get_brick_filenames():
            if brick_file.endswith(".brick"):
                brick_ident = brick_file.split('.')[0]
                idents.append(int(brick_ident))
        return sorted(idents)

    def on_link(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def _build_path(self, ident):
        assert isinstance(ident, int)
        return os.path.join(self.path, str(ident) + self.brick_ext)

    def _get_brick_filenames(self):
        return os.listdir(self.path)
