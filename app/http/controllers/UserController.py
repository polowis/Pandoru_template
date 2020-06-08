from app import app
from app.framework.controller import *
from app.framework.requests.form_request import FormRequest
from app.framework.requests.request import request
from app.model.user import User
from flask_login import current_user, login_user, logout_user, login_required
from flask import session, abort
from app.framework.util import *
from flask import jsonify
import json
from flask import request as req
from werkzeug.utils import secure_filename



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
            return redirect('/')

        return view('auth/auth')

    @route('/login', methods=['POST'])
    def login_action(self):

        form = FormRequest({
            'email': 'email'
        })

        if form.is_validated():
            user = User.query.filter_by(_email=request.input('email')).first()
            if user is None or not user.has_correct_password(request.input('password')): 
                flash('Email or password is wrong')
                return redirect('/login')

            login_user(user)
            session['username'] = user.username
            return redirect('/')

        else:
            return redirect('/login')
        
    @route('/register', methods=['GET'])
    def register_view(self):
        if current_user.is_authenticated:
            return redirect('/')
        return view('auth/register')
    

    @route('/register', methods=['POST'])    
    def register_action(self):
        form = FormRequest({
            'email': 'email',
            'username': 'alphanumeric'
        })
        if form.is_validated():
            user = User()
            if(len(request.input('password')) < 8):
                flash('password length must be greater than 8')
                return redirect('/login')

            user.username = request.input('username')
            user.email = request.input('email')
            user.password = request.input('password')
            user.user_id = 32
            user.save()

            user_logged_in = User.query.filter_by(_email=request.input('email')).first()
            login_user(user_logged_in)
            session['user'] = user_logged_in.username
            
            
            return redirect_to('/')
        else:
            return redirect_to('/register')

    @route('/logout', methods=['POST'])
    def logout(self):
        logout_user()
        return redirect('/login')
    

    @route('/user/avatar/edit', methods=['POST'])
    @login_required
    def edit_avatar(self):
        user = User.query.filter_by(_user_id=current_user.user_id).first()
        file = req.files['file']
        filename = secure_filename(file.filename.rsplit('.', 1)[0].lower() + str(datetime.datetime.now()) + '.' + file.filename.rsplit('.', 1)[1].lower())
        file.save('app/static/uploads/' + filename)
        user.avatar = filename
        try:
            user.save()
        except:
            return jsonify(message="Failure")
        return jsonify(message="Success")
    

    @route('/user/background/edit', methods=['POST'])
    @login_required
    def edit_background(self):
        user = User.query.filter_by(_user_id=current_user.user_id).first()
        file = req.files['file']
        filename = secure_filename(file.filename.rsplit('.', 1)[0].lower() + str(datetime.datetime.now()))
        file.save('app/static/uploads/' + filename)
        user.background = filename
        try:
            user.save()
        except:
            return jsonify(message="Failure")
        return jsonify(message="Success")
    
    @route('/user/delete/<user_id>', methods=['GET'])
    @login_required
    def show_profile(self, user_id):
        if current_user.user_id == user_id:
            return redirect('/')
        else:
            _user = User.query.filter(id=user_id).first()
            user = {
            "id": _user.id,
            "name": _user.username, 
            "email": _user.email,
            "user_id": _user.user_id,
            "avatar": _user.avatar,
            "background": _user.background  
            }
            return view('dashboard', user=json.dumps(user))

    @route('/user/edit', methods=['POST'])
    @login_required
    def edit_user_place(self):
        data = request.get_json()
        user = User.query.filter_by(_user_id=current_user.user_id).first()
        user.place = data['place']
        user.job = data['job']
        user.job_place = data['jobPlace']
        try:
            user.save()
        except:
            return jsonify(message="Failure")
        return jsonify(message="Success", place=data['place'], job=data['job'], jobPlace=data['jobPlace'])
    

    @route('/user/<user_id>', methods=['GET'])
    @login_required
    def view_profile(self, user_id):
        user = User.query.filter_by(_user_id=user_id).first()
        if user is None:
            abort(404)
        if current_user.user_id == user_id:
            return redirect('/')
        user_details = {
            "id": user.id,
            "name": user.username, 
            "email": user.email,
            "user_id": user.user_id,
            "avatar": user.avatar,
            "background": user.background,
            "place": user.place, 
            "job": user.job,
            "job_place": user.job_place
        }
        return view('profile', user=json.dumps(user_details))