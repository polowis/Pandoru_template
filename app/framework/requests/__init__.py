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

    def is_validated(self):
        """Check if all rules are validated"""
        for index, value in self.validate_list.items():
            result = req.form.get(index)
            if result is not None:
                self.__validate(result, value)

        self.__return_after_validation()

    def __validate(self, response: str, types: str) -> bool:
        """Validate request"""
        for i in FormRequest.TYPE:
            if types == i:
                return self.__validate_with(response, types)
        

    def __validate_with(self, response: str, types: str) -> bool:
        """Check for type and validate"""
        if types == 'integer':
            return self.validated.append(Validator.validate_integer(response))
        if types == 'alphanumeric':
            return self.validated.append(Validator.validate_alphanumeric(response))
    
    def __return_after_validation(self) -> bool:
        """Return after validate"""
        for condition in self.validated:
            if condition == False:
                return False
        return True