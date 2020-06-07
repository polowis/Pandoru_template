from app import app
from app.framework.controller import *
from app.model.user import *
from flask_login import login_required, current_user
from app.framework.requests.request import request
import json

class FollowerController(Controller):
    def construct(cls):
        FollowerController.register(app)
    
    @route("/follow/<user_id>", methods=['POST'])
    @login_required
    def follow(user_id):
        user = User.query.filter(user_id=user_id).first()
        if user is None:
            return 
        if user == current_user:
            return
        current_user.follow(user)
        user.save()
        return jsonify(message="Success")
    
    @route("/unfollow/<user_id>", methods=['POST'])
    @login_required
    def unfollow(user_id):
        user = User.query.filter(user_id=user_id).first()
        current_user.unfollow(user)

