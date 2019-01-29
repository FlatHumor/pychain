import json
from chaintime import chaintime


class Transaction(object):
    def __init__(self, sender=None, receiver=None, content=None, timestamp=None):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.timestamp = timestamp or chaintime.timestamp()

    def get_guess(self):
        return "%s%s%s%s" % (self.sender, self.receiver, self.content, self.timestamp)

    def __str__(self):
        return (
            """
            SENDER:    {sender}
            RECEIVER:  {receiver}
            CONTENT:   {content}
            TIMESTAMP: {timestamp}
            """).format(
            sender=self.sender,
            receiver=self.receiver,
            content=self.content,
            timestamp=self.timestamp
        )

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    t = Transaction(sender="sender", receiver="receiver", content="blah-blah-blah")
    print(t)
