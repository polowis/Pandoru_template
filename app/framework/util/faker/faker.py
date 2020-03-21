import forgery_py

class Faker:
    """Class to generate random things"""
    def __init__(self, lang=None):
        self.lang = lang

    @property
    def email_address(self):
        return forgery_py.internet.email_address()
    
    @property
    def domain_name(self):
        return forgery_py.internet.domain_name()
    
    @property
    def full_name(self):
        return forgery_py.name.full_name()
    
    @property
    def username(self):
        return forgery_py.internet.user_name(True)