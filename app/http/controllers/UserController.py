from app import app
from app.framework.controller import *
from app.framework.requests.form_request import FormRequest
from app.framework.requests.request import request
from app.model.user import User
from app.model.company import Company
from flask_login import current_user, login_user, logout_user, login_required
from flask import session
from app.framework.util import *
from flask import jsonify, Response
import json
from sqlalchemy.ext.declarative import DeclarativeMeta

class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)


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
            return jsonify(message="Password or email is incorrect")
        login_user(company)
        session['company'] = company.mailing_address
        return jsonify(message="Success")
        
        
    @route('/register', methods=['GET'])
    def register_view(self):
        if current_user.is_authenticated:
            return redirect('/')
        return view('auth/register')
    
    @route('/api/company', methods=['GET'])
    @login_required
    def company(self):
        companies = Company.query.all()
        data = json.dumps(companies, cls=AlchemyEncoder)
        return Response(data, mimetype='application/json')

    @route('/api/register', methods=['POST'])    
    def register_action(self):

        company = Company()
        
        company.company_name = request.get('companyName')
        company.contact_name = request.get('contactName')
        company.mailing_address = request.get('mailingAddress')
        company.contact_number = request.get('contactNumber')
        company.contact_title = request.get('contactTitle')
        company.password = request.get('password')
        company.business_type = request.get('businessType')
        company.company_id = 16

       
        try:
            company.save()
        except:
            return jsonify(message="Failure")

        logged_in = Company.query.filter_by(_mailing_address=request.get('mailingAddress')).first()
        login_user(logged_in)
        session['user'] = logged_in.mailing_address

        return jsonify(message="Success")


    @route('/logout', methods=['POST'])
    def logout(self):
        logout_user()
        return redirect('/login')
    
   


