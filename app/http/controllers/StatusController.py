from app import app
from app.framework.controller import *
from flask_login import login_required, current_user
from app.model.status import *
from app.model.user import *
from app.framework.requests.request import request
from flask import jsonify, Response
import json
from sqlalchemy.ext.declarative import DeclarativeMeta
from flask import request as req
from werkzeug.utils import secure_filename
import datetime

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

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

class StatusController(Controller):
    route_prefix = '/api'

    def construct(cls):
        StatusController.register(app)

    @route('/status/create', methods=['POST'])
    @login_required
    def create(self):
        status = Status()
        data = request.get_json()
        status.content = data['content']
        status.creator = current_user.user_id
        try:
            status.save()
        except:
            return jsonify(message="Failure")
        data = json.dumps(status, cls=AlchemyEncoder)
        data = json.loads(data)
        data.update({'message': 'Success'})
        return Response(json.dumps(data), mimetype="application/json")
    
    @route('/status/<user_id>')
    def fetch(self, user_id):
        status_list = Status.query.filter_by(_creator=user_id).all()
        data = json.dumps(status_list, cls=AlchemyEncoder)
        return Response(data, mimetype='application/json')
    
    def allowed_file(self, filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    @route('/photo/create', methods=['POST'])
    @login_required
    def createPhoto(self):
        file = req.files['file']
        if file.filename == "": 
            return redirect(req.url)
        if self.allowed_file(file.filename):
            status = Status()
            status.content = request.get('content')
            filename = secure_filename(file.filename.rsplit('.', 1)[0].lower() + str(datetime.datetime.now()) + '.' + file.filename.rsplit('.', 1)[1].lower())
            file.save('app/static/uploads/' + filename)
            status.photo = filename
            status.creator = current_user.user_id
            try:
                status.save()
            except:
                return jsonify(message="Failure")
            data = json.dumps(status, cls=AlchemyEncoder)
            data = json.loads(data)
            data.update({'message': 'Success'})
            return Response(json.dumps(data), mimetype="application/json")
        return jsonify(message="Failure")
    
    @route('/status/delete/<item_id>', methods=['POST'])
    @login_required
    def delete(self, item_id):
        status = Status.query.filter_by(id=item_id).first()
        try:
            status.delete()
        except:
            return jsonify(message="Failure")
        return jsonify(message="Success")

    @route('/status/edit/<item_id>', methods=["POST"])
    @login_required
    def edit(self, item_id):
        status = Status.query.filter_by(id=item_id).first()
        status.content = request.get('content')
    
    @route('/users/fetch', methods=['GET'])
    @login_required
    def fecth_users(self):
        users = User.query.filter().all()   
        data = []
        for user in users:
            data.append({"username": user.username, "avatar": user.avatar, "user_id": user.user_id})
        
        return jsonify(data)
    
    

