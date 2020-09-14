class MailError(Exception):
    """Base class for all mail exceptions"""
    def __init__(self, message=None):
        super().__init__(message)
    
    @property
    def message(self):
        if self.args:
            return self.args[0]

class InvalidBodyText(MailError):
    def __init__(self, message):
        MailError.__init__(self, message)