from chaintime import chaintime


class Brick(object):
    def __init__(self, ident=None, head_hash=None, prev_hash=None, nonce=0, bits="0000", timestamp=None,
                 transaction=None):
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
        return (
            """
            IDENT:       {ident}
            HEAD_HASH:   {head_hash}
            PREV_HASH:   {prev_hash}
            NONCE:       {nonce}
            BITS:        {bits}
            TIMESTAMP:   {timestamp}
            {transaction}
            """
        ).format(
            ident=self.ident,
            head_hash=self.head_hash,
            prev_hash=self.prev_hash,
            nonce=self.nonce,
            bits=self.bits,
            transaction=str(self.transaction),
            timestamp=self.timestamp
        )

    def __repr__(self):
        return self.__str__()
