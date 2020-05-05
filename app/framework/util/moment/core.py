from .moment import Moment

class moment:
    @staticmethod
    def date(*args):
        """Create a moment."""
        return Moment(*args)

    @staticmethod
    def now():
        """Create a date from the present time."""
        return Moment.now()

    @staticmethod
    def utc(*args):
        """Create a date using the UTC time zone."""
        return Moment.utc(*args)

    @staticmethod
    def utcnow():
        """UTC equivalent to `now` function."""
        return Moment.utcnow()

    @staticmethod
    def unix(timestamp, utc=False):
        """Create a date from a Unix timestamp."""
        return Moment.unix(timestamp, utc)