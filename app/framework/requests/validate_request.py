import re
from flask import flash

rule_errors = {
    'alphanumeric': 'Input field must be alpha numeric',
    'email': 'Input field must be a valid email address',
    'integer': 'Input field must be an integer'
}

def return_error(key, custom_response=None):
    """Return error response"""
    if custom_response = None:
        return rule_errors.get(key)


def match(pattern: str, string: str, error: str, category: str) -> bool:
    """Try to apply the pattern at the start of the string, 
    Return boolean."""
    if re.match(pattern, string):
        return True
    else:
        flash(error, category)
        return False

def is_string(value: str):
    """Return true if given value is a string"""
    return isinstance(value, str)

def is_numeric(value: str):
    """Return True if given value is a number"""
    return value.isdigit()

class Validator:
    @staticmethod
    def validate_integer(value, category):
        """Validate integer"""
        return match("^[0-9]+$", value, 'Input field must be an integer', category)
            
    
    @staticmethod
    def validate_alphanumeric(value, category):
        """Validate that an attribute contains only alpha-numeric characters."""
        return match("^[a-zA-Z0-9_]*$", value, 'Input field must be alphanumeric', category)
    
    @staticmethod
    def validate_email(value, category):
        """Validate email"""
        return match(r'[\w\.-]+@[\w\.-]+(\.[\w]+)+', value, 'Input field must be a valid email address' , category)
    
    @staticmethod
    def validate_alpha(value, category):
        """Validate that an attribute contains only alphabetic characters."""
        return is_string(value) and match('/^[\pL\pM]+$/u', value)

    @staticmethod
    def validate_alpha_dash(value, category):
        """Validate that an attribute contains only alpha-numeric characters, dashes, and underscores."""
        if not is_string(value) and not is_numeric(value):
            flash(return_error('alpha_dash'))
            return False
        return match('/^[\pL\pM\pN]+$/u', value)
    


