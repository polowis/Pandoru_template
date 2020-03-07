from flask import request

class Request:
    @staticmethod
    def input(name):
        """Get input form data"""
        if isinstance(name, str):
            return request.form.get(name)
        raise ValueError("Argument must be a string")

    @staticmethod
    def query(name=None):
        """Get query string"""
        if name is None:
            return request.args
        return request.args.get(name)
    
    @staticmethod
    def has(name):
        """Check is value is present on the request"""
        if isinstance(name, list):
            for param in name:
                if request.args.get(param) is None:
                    return False
            return True

        elif isinstance(name, str):
            if request.values.get(name) is not None:
                return True
            return False
        return False
    
    @staticmethod
    def filled(name):
        """Check is value is not empty"""
        response = request.values.get(name)
        if response is not None and response != '':
            return True
        return False

    @staticmethod
    def cookie(name):
        """Get cookie value through request"""
        return request.cookies.get(name)
    
    @staticmethod
    def only(name: list):
        """Get only value from request"""
        if isinstance(name, list):
            response = {}
            for param in name:
                if param in request.values:
                    value = request.values.get(param)
                    response.update({param: value})
            return response
        else:
            raise ValueError('Argument must be a list')

