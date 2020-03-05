from app import app
from app.framework.controller import Controller, route

class HomeController(Controller):

    def construct(cls):
        HomeController.register(app)

    @route('/test', methods=["GET"])
    def test(self):
        return self.view('test')

    @route('/', methods=["GET"])
    def home(self):
        return self.view('index')

