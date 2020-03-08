from flask import get_flashed_messages

class ViewFunction:
    def __init__(self, app):
        self.app = app
        self.app.jinja_env.globals.update(error=self.__error)

    def __error(self, name_field):
        """Display error message"""
        messages = get_flashed_messages(with_categories=True)
        if len(messages) >= 1:
            for category, message in messages:
                if category == name_field:
                    return message
        else:
            return ''



def getMethodMembers(base_class, cls):
    base_name = dir(base_class)
    predicate = inspect.isfunction
    all_members = inspect.getmembers(cls, predicate=predicate)
    return[member for member in all_members]

