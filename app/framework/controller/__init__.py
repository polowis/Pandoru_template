import inspect
import re
from flask import render_template, flash, redirect

def route(rule, **options):
    """Route function"""
    def decorator(f):
        if not hasattr(f, '_rule') or f._rule is None:
            f._rule = {f.__name__: [(rule, options)]}

        return f

    return decorator

class Controller(object):

    """Base view for any class 
    """
    decorators = []
    route_prefix = None
    middleware = None
    trailing_slash = True

    

    @classmethod
    def register(cls, app, route_prefix=None, middleware=None):
        """Register app"""
        if cls is Controller:
            raise TypeError("cls must be a subclass of Controller, not Controller itself")
        
        if route_prefix:
            cls.route_prefix = route_prefix
        
        members = getMethodMembers(Controller, cls)
        for name, value in members:
            route_name = cls.build(name)
            view_method = cls.make_method(name)
            if hasattr(value, '_rule') and name in value._rule:
                for index, _rule in enumerate(value._rule[name]):
                    rule, options = _rule
                    location = cls.build_route(rule)
                    endpoint = route_name
                    
                    app.add_url_rule(str(location), endpoint, view_func=view_method , **options)

    @classmethod
    def build(cls, name):
        return cls.__name__ + ':' + name
    
    @classmethod
    def build_route(cls, rule, method=None):
        rule_parts = []
        if cls.route_prefix:
            rule_parts.append(cls.route_prefix)
        rule_parts.append(rule)
        result = "/%s" % "/".join(rule_parts)
        return re.sub(r'(/)\1+', r'\1', result)

    @classmethod
    def make_method(cls, name):
        proxy = cls()
        view = getattr(proxy, name)
        
        if cls.decorators:
            print(cls.decorators)
        
        return view
    @staticmethod
    def view(template_name, **option):
        """return view"""
        return render_template(template_name+'.html', **option)

    @staticmethod
    def flash_message(message, category="message"):
        """flash message"""
        return flash(message, category)
    @staticmethod
    def redirect_to(location, code=302, response=None):
        """redirect to location"""
        return redirect(location, code, response)

    

def getMethodMembers(base_class, cls):
    base_name = dir(base_class)
    predicate = inspect.isfunction
    all_members = inspect.getmembers(cls, predicate=predicate)
    return[member for member in all_members]

    





