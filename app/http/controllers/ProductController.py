from app.model.product import Product
from app import app
from app.framework.controller import *
from app.framework.requests.request import request
from flask_login import login_required, current_user
import json
from flask import jsonify, Response
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

class ProductController(Controller):
    def construct(cls):
        ProductController.register(app)
    

    @route('/products/create', methods=['GET'])
    @login_required
    def view_create(self):
        return view('product/create')

    @route('/api/products/create', methods=['POST'])
    @login_required
    def create(self):
        file = request.files('file')
        log(type(file))
        if file.filename == '':
            return redirect(req.url) 
        product: Product = Product()

        product.name = request.get('name')
        product.price = request.get('price')
        product.description = request.get('description')
        product.category = request.get('category')
        product.quantity = request.get('quantity')
        product.tag = request.get('tag')
        product.owner = current_user.company_id
        product.photo = file
        product.product_id = 16
        try:
            product.save()
        except:
            return jsonify(message="Failure")
        return jsonify(message="Success")

    @route('/api/product')
    def fetch_all(self):
        product = Product.query.all()
        data = json.dumps(product, cls=AlchemyEncoder)
        return Response(data, mimetype='application/json')
        
    @route('/api/product/owner/<owner_id>', methods=["GET"])
    def fetch_product(self, owner_id):
        product = Product.query.filter_by(_owner=owner_id).all()
        data = json.dumps(product, cls=AlchemyEncoder)
        return Response(data, mimetype='application/json')

    
    @route('/api/product/update/<product_id>', methods=['POST'])
    def update(self, product_id):
        product: Product = Product.query.filter_by(id=product_id).first()
        product.name = data['name']
        product.price = data['price']
        product.description = data['description']
        product.category = data['category']
        product.tag = data['tag']
        try:
            product.save()
        except:
            return jsonify(message="Failure")
        return jsonify(message="Success")
    
    @route('/product/<product_id>', methods=['GET'])
    def item(self, product_id):
        product = Product.query.filter_by(id=product_id).first()
        data = json.dumps(product, cls=AlchemyEncoder)
        return Response(data, mimetype='application/json')
