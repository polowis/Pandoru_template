import re

def match(pattern: str, string: str) -> bool:
    """Try to apply the pattern at the start of the string, 
    Return boolean."""
    if re.match(pattern, string):
        return True
    else:
        return False

class Validator:
    @staticmethod
    def validate_integer(value):
        """Validate integer"""
        return match("^[0-9]+$", value)
            
    
    @staticmethod
    def validate_alphanumeric(value):
        """Validate alphanumeric"""
        return match("^[a-zA-Z0-9_]*$", value)