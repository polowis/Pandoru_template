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
    @login_required
    def home(self):
        user = {
            "id": current_user.id,
            "name": current_user.username, 
            "email": current_user.email,
            "user_id": current_user.user_id,
            "avatar": current_user.avatar,
            "background": current_user.background,
            "place": current_user.place, 
            "job": current_user.job,
            "job_place": current_user.job_place
           
        }
        return view('dashboard', user=json.dumps(user))

