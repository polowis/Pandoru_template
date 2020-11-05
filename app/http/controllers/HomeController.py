from app import app
from app.framework.controller import *
from flask_login import login_required, current_user
from app.framework.requests.request import request
import json


class HomeController(Controller):

    def construct(cls):
        HomeController.register(app)


    @route('/todolist', methods=["GET"])
    @login_required
    def test(self):
        user = {
            "id": current_user.id,
            "name": current_user.username, 
            "email": current_user.email,
            "user_id": current_user.user_id
            
        }
        return view('test', user=json.dumps(user))

    @route('/', methods=["GET"])
    def home(self):
        if current_user.is_authenticated:
            user = {
                "active": 1,
                "id": current_user.id,
                "user_id": current_user.company_id,
                "name": current_user.company_name, 
                "email": current_user.mailing_address,
            }
        else:
            user = {
                "active": 0,
                "id": 0,
                "user_id": 0,
                "name": 0, 
                "email": 0,
            }
        return view('index', user=json.dumps(user))

    @route('/about', methods=["GET"])
    def about(self):
        return view('about')
