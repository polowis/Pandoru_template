from app.framework.controller import Controller, route

class ExampleController(Controller):
    route_prefix = '/ddd'

    def index():
        pass

ExampleController.register()