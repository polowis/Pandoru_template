class MailError(Exception):
    def __init__(self, message=None):
        super().__init__(message)
    
    @property
    def message(self):
        if self.args:
            return self.args[0]