from chaintime import chaintime

class Brick(object):
    def __init__(self, ident=None, head_hash=None, prev_hash=None, nonce=0, bits="0000", timestamp=None, transaction=None):
        self.ident = ident
        self.head_hash = head_hash
        self.prev_hash = prev_hash
        self.nonce = nonce
        self.bits = bits
        self.transaction = transaction
        self.timestamp = timestamp or chaintime.timestamp()
        
    def get_guess(self):
        return "%s%s%s" % (self.transaction.get_guess(), self.prev_hash, self.timestamp)

    def __str__(self):
        return "{i}\n{hh}\n{ph}\n{n}\n{b}\n{ts}\n{ta}".format(
            i=self.ident,
            hh=self.head_hash,
            ph=self.prev_hash,
            n=self.nonce,
            b=self.bits,
            ts=self.timestamp,
            ta=self.transaction
        )

    def __repr__(self):
        return self.__str__()