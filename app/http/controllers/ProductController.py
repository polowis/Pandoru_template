from app.model.product import Product
from app import app
from app.framework.controller import *
from app.framework.requests.request import request
from flask_login import login_required, current_user
import json
from flask import jsonify, Response

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

class ProductController(Controller):
    def construct(cls):
        ProductController.register(app)
    
    @route('/api/products/create', methods=['POST'])
    @login_required
    def create(self):
        product = Product()
        data = request.get_json()
        
        product.name = data['name']
        product.price = data['price']
        product.description = data['description']
        product.category = data['category']
        product.tag = data['tag']
        product.owner = current_user.company_id
        try:
            product.save()
        except:
            return jsonify(message="Failure")
        return jsonify(message="Success")
    
    @route('/api/product/<owner_id>')
    def fetch_product(owner_id):
        product = Product.query.filter_by(_owner=owner_id).first()
        data = json.dumps(product, cls=AlchemyEncoder)
        return Response(data, mimetype='application/json')