from app import app
from app.framework.controller import *
from app.framework.requests.form_request import FormRequest
from app.framework.requests.request import request
from app.model.user import User
from flask_login import current_user, login_user, logout_user, login_required
from flask import session
from app.framework.util import *
from flask import jsonify
import json



class UserController(Controller):
    def construct(cls):
        UserController.register(app)

    @route('/dashboard', methods=['GET'])
    @login_required
    def dashboard_view(self):
        user = {
            "id": current_user.id,
            "user_id": current_user.user_id,
            "name": current_user.username, 
            "email": current_user.email,
            
        }
        return jsonify(user)

    @route('/login', methods=['GET'])
    def login_view(self):
        if current_user.is_authenticated:
            return redirect('/dashboard')

        return view('auth/login')

    @route('/login', methods=['POST'])
    def login_action(self):

        form = FormRequest({
            'user_email': 'email'
        })

        if form.is_validated():
            user = User.query.filter_by(_email=request.input('user_email')).first()
            if user is None or not user.has_correct_password(request.input('pass')): 
                flash('Email or password is wrong')
                return redirect('/login')
            #log(user)
            login_user(user)
            session['username'] = user.username
            return redirect('/dashboard')

        else:
            return redirect('/login')
        
    @route('/register', methods=['GET'])
    def register_view(self):
        if current_user.is_authenticated:
            return redirect('/dashboard')
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
            user.user_id = 32
            user.save()

            user_logged_in = User.query.filter_by(_email=request.input('email')).first()
            login_user(user_logged_in)
            session['user'] = user_logged_in.username

            return redirect_to('/dashboard')
        else:
            return redirect_to('/register')

    @route('/logout', methods=['POST'])
    def logout(self):
        logout_user()
        return redirect('/login')
