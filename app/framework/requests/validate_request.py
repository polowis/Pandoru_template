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

def in_array(key: str, array: list):
    """Return True if given key exists in given array"""
    if key in array:
        return True
    else:
        return False

def match(pattern: str, string: str, error_response: str, category: str) -> bool:
    """Try to apply the pattern at the start of the string, 
    Return boolean."""
    if re.match(pattern, string):
        return True
    else:
        flash(error_response, category)
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
    
    @staticmethod
    def validate_boolean(value, category):
        """Validate that an attribute is a boolean."""
        acceptable_values = [True, False, 0, 1, '0', '1']
        return in_array(value, acceptable_values)
    


