from app import app
from importlib import import_module
from app.framework.routes.route_action import getFunction, getModule
from flask import request
from ..controller import Controller

def next():
    """Redirect user to the next page"""
    return request.args.get('next')

def back():
    """Redirect user back to previous page"""
    return request.referrer

class Route:
    def get(self, url, view_class, func_name=None):
        if isinstance(view_class, Controller):
            view_function = getattr(view_class(), func_name)
        else:
            view_function = view_class
        app.add_url_rule(url, func_name, view_func=view_function, methods=['GET'])
        

    def post(self, url, view_function, name=None):
        if isinstance(view_function, str):
            try:
                function = import_module(str(getModule(view_function)))
                res = getattr(function, str(getFunction(view_function)))()
            except:
                raise ImportError('Module:', view_function, 'not found')
        else:
            res = view_function
        app.add_url_rule(url, name, view_func=res, methods=['POST'])
        
route = Route()