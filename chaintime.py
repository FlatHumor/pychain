from datetime import datetime

class chaintime(datetime):

    @classmethod
    def timestamp(cls, dttm=None):
        epoch = cls.utcfromtimestamp(0)
        current = dttm or cls.now()
        return (current - epoch).total_seconds() * 1000
