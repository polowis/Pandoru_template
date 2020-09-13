from app import app
from app.framework.controller import *
from app.framework.requests.form_request import FormRequest
from app.framework.requests.request import request
from app.model.user import User
from app.model.company import Company
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
            return redirect('/')

        return view('auth/login')

    @route('/api/login', methods=['POST'])
    def login_action(self):
        company = Company.query.filter_by(_mailing_address=data['email']).first()
        if company is None or not company.has_correct_password(data['password']):
            return redirect('/login')
        login_user(company)
        session['company'] = company.mailing_address
        return redirect('/')
        
        
    @route('/register', methods=['GET'])
    def register_view(self):
        if current_user.is_authenticated:
            return redirect('/')
        return view('auth/register')
    

    @route('/api/register', methods=['POST'])    
    def register_action(self):

        company = Company()
        data = request.get_json()
        
        company.company_name = data['companyName']
        company.contact_name = data['contactName']
        company.mailing_address = data['mailingAddress']
        company.contact_number = data['contactNumber']
        company.contact_title = data['contactTitle']
        company.password = data['password']
        company.business_type = data['businessType']

       
        try:
            company.save()
        except:
            return jsonify(message="Failure")

        logged_in = Company.query.filter_by(_mailing_address=data['mailingAddress']).first()
        login_user(logged_in)
        session['user'] = logged_in.mailing_address

        return jsonify(message="Success")


    @route('/logout', methods=['POST'])
    def logout(self):
        logout_user()
        return redirect('/login')
    
   


