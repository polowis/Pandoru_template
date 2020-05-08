from flask import request as req
from ..util import *
from .ip_trait import *
import requests, json

class Request:
    """Handle request, response"""
    def IP(self):
        """Return the IP instance of request"""
        return IP(self.__checkIP())

    def input(self, name=None):
        """Get input form data"""
        if req.is_json():
            return self.__find_with_json(name)
        else:
            if name is None:
                return req.form
            if isinstance(name, str):
                return req.form.get(name)
            raise ValueError("Argument must be a string")

    def __find_with_json(self, key: str):
        """ use "dot" notation to access the arrays"""
        data = self.get_json()
            if isinstance(key, str):
                return self.__find(key, data)


    def method(self, methodType: str):
        """Check for request method \n
        For eg: if request.method("GET"): 

        """
        if methodType.upper() == "GET":
            return req.method == "GET"

        elif methodType.upper() == "POST":
            return req.method == "POST"
   
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

   
    def cookie(self, name=None):
        """Get cookie value through request"""
        if name is None:
            return req.cookies
        if isinstance(name, str):
            return req.cookies.get(name)
        raise ValueError("Name must be a string")
    
    def get(self, name):
        """Retrieve value from request"""
        return req.values.get(name)
    
        
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

    def get_json(self):
        """Return json"""
        return req.get_json()
    

    def header(self, value=None):
        """Get header request"""
        if value is None:
            return req.headers
        return req.headers.get(value)


    def platform(self, **kwargs):
        """Return request's OS platform"""
        return req.user_agent.platform
    
    
    def browser(self, **kwargs):
        """Return request's browser"""
        return req.user_agent.browser
    

    def version(self, **kwargs):
        """Return browser version"""
        return req.user_agent.version


    def ip(self, deep_detect=True):
        """Return request's IP address \n
        If you want to get more details, use method chaining IP instead
        Eg: request.IP().state
        """

        ip = req.remote_addr
        if deep_detect:
            if(is_valid_ip(self.header("X-Forwarded-For"))):
                ip = self.header("X-Forwarded-For")

            if(is_valid_ip(self.header("X-Client-IP"))):
                ip = self.header("X-Client-IP")

        return ip


    def __checkIP(self):
        """Check for local ip"""
        ip = self.ip()

        # check for local ip
        if(ip == "127.0.0.1" or ip == "0.0.0.0"):
            ip = ""
        return ip


    def location(self, **kwargs):
        """Return request's location (country name)
        If you want to get more details, use method chaining IP instead
        Eg: request.IP().state
        """
        
        url = 'http://www.geoplugin.net/json.gp?ip={}'.format(self.__checkIP())
        r = requests.get(url)
        j = json.loads(r.text)
        locale = j["geoplugin_countryName"]
        return locale
    
    def locale(self):
        """return current locale of request"""
        return req.accept_languages
    

    def __find(self, element: str, json: dict):
        """Find by dot notation"""

        keys = element.split(".")
        rv = json
        for key in keys:
            rv = rv[key]
        return rv

request = Request()