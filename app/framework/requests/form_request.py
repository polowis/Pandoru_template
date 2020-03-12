from flask import request as req
from app.framework.requests.validate_request import Validator

def request(name):
    """request function"""
    return req.form.get(name)


class FormRequest:
    """Specify rule for input form. \n
    usage: \nform = FormRequest(dict) \n
    if form.is_validate():
        #code goes here
    """
    TYPE = ['integer', 'alpha', 'alphanumeric', 'email']
    def __init__(self, validate_list: list):
        self.validate_list = validate_list
        self.validated = []
        self.custom_error_message = {}

    def __message(self, custom_error_message : dict):
        self.custom_error_message = custom_error_message
    
    def __getMessage(self, key):
        for index, value in self.custom_error_message.items():
            if index == key:
                return value

    def is_validated(self):
        """Check if all rules are validated"""
        for index, value in self.validate_list.items():
            result = req.form.get(index)
            name_field = index
            if result is not None:
                self.__validate(result, value, name_field)

        return self.__return_after_validation()

    def __validate(self, response: str, types: str, name_field: str) -> bool:
        """Validate request"""
        for i in FormRequest.TYPE:
            if types == i:
                return self.__validate_with(response, types.lower(), name_field)
        

    def __validate_with(self, response: str, types: str, name_field: str) -> bool:
        """Check for type and validate"""
        if types == 'integer':
            return self.validated.append(Validator.validate_integer(response, name_field))
        if types == 'alphanumeric':
            return self.validated.append(Validator.validate_alphanumeric(response, name_field))
        if types == 'email':
            return self.validated.append(Validator.validate_email(response, name_field))

    def __return_after_validation(self) -> bool:
        """Return after validate"""
        
        for condition in self.validated:
            if condition == False:
                return False
        return True