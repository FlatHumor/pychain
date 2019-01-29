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
            transaction = Transaction(lines[6], lines[7], lines[8], lines[9])
            return Brick(lines[0], lines[1], lines[2], lines[3], lines[4], lines[5], transaction)

    def save_brick(self, brick):
        next_ident = 0
        curr_idents = self.get_identificators()
        if len(curr_idents) > 0:
            curr_idents.sort()
            next_ident = curr_idents[-1] + 1
        next_path = self._build_path(next_ident)
        with open(next_path, 'w') as brickfile:
            brickfile.write(str(brick))

    def get_identificators(self):
        idents = []
        for brick_file in self._get_brick_filenames():
            if brick_file.endswith(".brick"):
                brick_ident = brick_file.split('.')[0]
                idents.append(int(brick_ident))
        return idents

    def on_link(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def _build_path(self, ident):
        assert isinstance(ident, int)
        return os.path.join(self.path, str(ident) + self.brick_ext)

    def _get_brick_filenames(self):
        return os.listdir(self.path)
