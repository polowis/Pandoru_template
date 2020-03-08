import re
from flask import flash

def match(pattern: str, string: str, error: str, category: str) -> bool:
    """Try to apply the pattern at the start of the string, 
    Return boolean."""
    if re.match(pattern, string):
        return True
    else:
        flash(error, category)
        return False

class Validator:
    @staticmethod
    def validate_integer(value, category):
        """Validate integer"""
        return match("^[0-9]+$", value, 'Input field must be an integer', category)
            
    
    @staticmethod
    def validate_alphanumeric(value, category):
        """Validate alphanumeric"""
        return match("^[a-zA-Z0-9_]*$", value, 'Input field must be alphanumeric', category)
    
    @staticmethod
    def validate_email(value, category):
        """Validate email"""
        return match(r'[\w\.-]+@[\w\.-]+(\.[\w]+)+', value, 'Input field must be a valid email address' , category)