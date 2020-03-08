from app import app
from app.framework.controller import *
from app.framework.requests import FormRequest
from app.framework.requests.request import request



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

        form = FormRequest({
            'user_email': 'email'
        })

        if form.is_validated():
            user = {'username': request.input('user_email')}
            return view('dashboard', user=user)
        else:
            return redirect('/login')
