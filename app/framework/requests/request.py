from flask import request as req

class Request:
    """Handle request, response"""
    def input(self, name):
        """Get input form data"""
        if isinstance(name, str):
            return req.form.get(name)
        raise ValueError("Argument must be a string")

   
    def query(self, name=None):
        """Get query string"""
        if name is None:
            return req.args
        return req.args.get(name)
    
    def has(self,name):
        """Check is value is present on the request"""
        if isinstance(name, list):
            for param in name:
                if req.args.get(param) is None:
                    return False
            return True

        elif isinstance(name, str):
            if req.values.get(name) is not None:
                return True
            return False
        return False
    
    def filled(self,name):
        """Check is value is not empty"""
        response = req.values.get(name)
        if response is not None and response != '':
            return True
        return False

   
    def cookie(self, name):
        """Get cookie value through request"""
        return req.cookies.get(name)
    
    
    def only(self, name: list):
        """Get only value from request"""
        if isinstance(name, list):
            response = {}
            for param in name:
                if param in req.values:
                    value = req.values.get(param)
                    response.update({param: value})
            return response
        else:
            raise ValueError('Argument must be a list')

request = Request()