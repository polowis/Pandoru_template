import math
import random

class Faker:
    """A package that generate fake data"""
    def __init__(self, lang=None):
        self.lang = lang

    @property
    def alphanumeric(self):
        """generate random alphanumeric_string"""
        length = 20
        result = ''
        characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        characters_length = len(characters)
        for i in range(length):
            result += characters[math.floor(random.random() * characters_length)]
        return result

    @property
    def alpha(self):
        length = 20
        result = ''
        characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        characters_length = len(characters)
        for i in range(length):
            result += characters[math.floor(random.random() * characters_length)]
        return result
