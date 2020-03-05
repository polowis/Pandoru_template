from app import app
from app.framework.controller import *


class UserController(Controller):
    def construct(cls):
        UserController.register(app)

    @route('/dashboard', methods=['GET'])
    def dashboard_view(self):
        return view('dashboard')

    @route('/login', methods=['GET'])
    def login_view(self):
        return view('auth/login')

    @route('/login', methods=['POST'])
    def login_action(self):
        user = {'username': requests('username')}
        return view('dashboard', user=user)
