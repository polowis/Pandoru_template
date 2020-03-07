from flask import request
from app.framework.requests.validate_request import Validator

def requests(name):
    """request function"""
    return request.form.get(name)


class FormRequest:
    TYPE = ['integer', 'alpha', 'alphanumeric', 'email']

    def register(cls, validation: dict):
        """Register FormRequest"""
        for index, value in validation:
            try:
                result = requests(index)
                self.validate(result, value)
            except:
                print(f'Not found {index}')
        
    def validate(self, index: str, value: str):
        """Validate request"""
        for i in FormRequest.TYPE:
            if value == FormRequest.TYPE:
                return self.validate_with(index, value)
        return True

    def validate_with(self, index: str, value: str):
        if value == 'integer':
            return Validator.validate_integer(value)
        if value == 'alphanumeric':
            return Validator.validate_alphanumeric(value)
    

    def is_validate(self):
        return True