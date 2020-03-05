from app import app
from importlib import import_module
from app.framework.routes.route_action import getFunction, getModule

class Route:
    def get(self, url, view_function, name=None, middleware=None):
        if isinstance(view_function, str):
            try:
                function = import_module(str(getModule(view_function)))
                res = getattr(function, str(getFunction(view_function)))()
            except:
                raise ImportError('Module:', view_function, 'not found')
        else:
            res = view_function
        
        middleware()
        app.add_url_rule(url, name, view_func=res, methods=['GET'])
        

    def post(self, url, view_function, name=None, middleware=None):
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