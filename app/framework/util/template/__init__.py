from flask import get_flashed_messages
import base64
import os
from math import floor
from ..moment.core import *

class ViewFunction:
    """Custom view function"""
    def __init__(self, app):
        self.app = app
        self.app.jinja_env.globals.update(
            error_message=self.__error_message, 
            error=self.__error,
            nonce=self.__nonce,
            moment=moment
        )
        

    def __error(self, name_field):
        """Check if error exists"""
        messages = get_flashed_messages(with_categories=True)
        if len(messages) >= 1:
            return True

    def __error_message(self, name_field):
        """Display error message"""
        messages = get_flashed_messages(with_categories=True)
        if len(messages) >= 1:
            for category, message in messages:
                if category == name_field:
                    return message
        else:
            return ''
    
    def __nonce(self):
        length = 32
        if length < 1:
            return ''
        string=base64.b64encode(os.urandom(length),altchars=b'-_')
        b64len=4*floor(length)
        if length%3 == 1:
            b64len+=2
        elif length%3 == 2:
            b64len+=3
        return string[0:b64len].decode()



def getMethodMembers(base_class, cls):
    base_name = dir(base_class)
    predicate = inspect.isfunction
    all_members = inspect.getmembers(cls, predicate=predicate)
    return[member for member in all_members]

