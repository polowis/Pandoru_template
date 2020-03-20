from app import app
from app.framework.controller import *
from flask_login import login_required, current_user
from app.model.todolist import *
from app.framework.requests.request import request
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

class ToDoListController(Controller):
    route_prefix = '/api'

    def construct(cls):
        ToDoListController.register(app)
    

    @route('/create', methods=['POST'])
    @login_required
    def create(self):
        todolist = ToDoList()
        data = request.get_json()
        todolist.title = data['title']
        todolist.description = data['description']
        todolist.progress = data['progress']
        todolist.author = current_user.user_id
        todolist.save()

        data = json.dumps(todolist, cls=AlchemyEncoder)
        return Response(data, mimetype="application/json")
    

    @route('/todolist/<user_id>')
    def fetch(self, user_id):
        todolist = ToDoList.query.filter_by(_creator=user_id).all()
        data = json.dumps(todolist, cls=AlchemyEncoder)
        return Response(data, mimetype='application/json')


    @route('/done/<item_id>', methods=['POST'])
    def done(self, item_id):
        todolist = ToDoList.query.filter_by(id=item_id).first()
        todolist.done = True
        todolist.progress = False
        todolist.save()
        return jsonify(message="Success")
    
    @route('/undone/<item_id>', methods=['POST'])
    def done(self, item_id):
        todolist = ToDoList.query.filter_by(id=item_id).first()
        todolist.done = False
        todolist.progress = True
        todolist.save()
        return jsonify(message="Success")
        
    
    @route("/delete/<item_id>", methods=['POST'])
    def delete(self, item_id):
        todolist = ToDoList.query.filter_by(id=item_id).first()
        todolist.delete()
        return jsonify(message="Success")

    @route('item/<item_id>', methods=['GET'])
    def item(self,item_id):
        todolist = ToDoList.query.filter_by(id=item_).first()


    @route('<item_id>', methods=['POST'])
    def edit(self, item_id):
        data = request.get_json()
        todolist = ToDoList.query.filter_by(id=item_id).first()
        todolist.title = data['title']
        todolist.description = data['description']
        todolist.save()
        return jsonify(message="Success")