from app import app
from app.framework.controller import Controller, route
from app.framework.requests import requests

class UserController(Controller):
    def construct(cls):
        UserController.register(app)

    @route('/dashboard', methods=['GET'])
    def dashboard_view(self):
        return self.view('dashboard')

    @route('/login', methods=['GET'])
    def login_view(self):
        return self.view('auth/login')

    @route('/login', methods=['POST'])
    def login_action(self):
        user = {'username': requests('username')}
        return self.view('dashboard', user=user)
