from flask import request
from app.framework.requests.validate_request import Validator

def requests(name):
    """request function"""
    return request.form.get(name)


class Request:
    TYPE = ['integer', 'alpha', 'alphanumeric', 'email']

    def register(cls, validation: list):
        for index, value in validation:
            try:
                result = requests(index)
                self.validate(result, value)
            except:
                print(f'Not found {index}')
        
    def validate(self, index: str, value: str):
        for i in Request.TYPE:
            if value == Request.TYPE:
                return self.validate_with(index, value)
    
    def validate_with(self, index: str, value: str):
        if value == 'integer':
            return Validator.validate_integer(value)
        if value == 'alphanumeric':
            return Validator.validate_alphanumeric(value)
    

    def is_validate(self):
        return True