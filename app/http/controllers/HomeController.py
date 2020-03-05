from app import app
from app.framework.controller import *

class HomeController(Controller):

    def construct(cls):
        HomeController.register(app)

    @route('/test', methods=["GET"])
    def test(self):
        return view('test')

    @route('/', methods=["GET"])
    def home(self):
        return view('index')

