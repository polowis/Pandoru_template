from app import app
from app.framework.controller import *
from flask_login import login_required, current_user
import json


class HomeController(Controller):

    def construct(cls):
        HomeController.register(app)


    @route('/test', methods=["GET"])
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
        return view('index')

