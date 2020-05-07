from flask import request as req
from ..util import *
from .ip_trait import *
import requests, json

class Request:
    """Handle request, response"""
    def IP(self):
        return IP(self.ip())

    def input(self, name=None):
        """Get input form data"""
        if name is None:
            return req.form
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
        """Return request's IP address
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

    def location(self, **kwargs):
        """Return request's location (country name)
        If you want to get more details, use method chaining IP instead
        Eg: request.IP().state
        """
        url = 'http://www.geoplugin.net/json.gp?ip={}'.format(self.ip())
        r = requests.get(url)
        j = json.loads(r.text)
        locale = j["geoplugin_countryName"]
        return locale

request = Request()