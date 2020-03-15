from flask import request as req
from flask import redirect
from app.framework.routes import *
from app.framework.requests.validate_request import Validator
from app.framework.util import *
from app.framework.controller import *

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
    def __init__(self, validate_list: list, new_request=False):
        self.validate_list = validate_list
        self.validated = []
        self.custom_error_message = {}
        if new_request == True:
            self.__validate_request()

    def __message(self, custom_error_message : dict):
        self.custom_error_message = custom_error_message
    

    def __getMessage(self, key):
        for index, value in self.custom_error_message.items():
            if index == key:
                return value

    def __validate_request(self):
        """Replace is_validated method"""
        for index, value in self.validate_list.items():
            result = req.form.get(index)
            name_field = index
            if result is not None:
                self.__validate_type(result, value, name_field)
    

    def __validate_type(self, response: str, types: str, name_field: str) -> bool:
        """Validate request type"""
        for i in FormRequest.TYPE:
            if types == i:
                self.__validate_method(response, types.lower(), name_field)


    def __validate_method(self, response: str, types: str, name_field: str) -> bool:
        """Check for type and validate"""
        if types == 'integer':
            if Validator.validate_integer(response, name_field) == False:
                return redirect_to(back())
            
        if types == 'alphanumeric':
            if Validator.validate_alphanumeric(response, name_field) == False:
                return redirect_to('/')
            
        if types == 'email':
            if Validator.validate_email(response, name_field) == False:
                return redirect_to(back())
            

    def is_validated(self):
        """Check if all rules are validated. Will be deprecated"""
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
            if Validator.validate_email(response, name_field) == False:
                return redirect(back())
            return self.validated.append(Validator.validate_email(response, name_field))

    def __return_after_validation(self) -> bool:
        """Return after validate"""
        
        for condition in self.validated:
            if condition == False:
                return False
        return True