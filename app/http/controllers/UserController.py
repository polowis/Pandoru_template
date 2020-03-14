from app import app
from app.framework.controller import *
from app.framework.requests import FormRequest
from app.framework.requests.request import request
from app.model.user import User



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
            user = User.query.filter_by(email=request.input('email')).first()
            if user is None or user.has_correct_password(request.input('password')):
               return redirect('/login')
            return 'logged in'

        else:
            return redirect('/login')
        
    @route('/register', methods=['GET'])
    def register_view(self):
        return view('auth/register')
    

    @route('/register', methods=['POST'])    
    def register_action(self):
        form = FormRequest({
            'email': 'email',
            'username': 'alphanumeric'
        })
        if form.is_validated():
            user = User()
            user.username = request.input('username')
            user.email = request.input('email')
            user.password = request.input('password')
            user.save()
            return 'logged in'
        
