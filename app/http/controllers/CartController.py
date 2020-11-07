from app.model.product import Product
from app.model.transaction import Transaction
from app.model.transactionItem import TransactionItem
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

class CartController(Controller):
    def construct(cls):
        CartController.register(app)
    
    @route('/cart', methods=['GET'])
    def view_cart(self):
        return view('/product/cart', user=json.dumps(self.get_current_user()))

    @route('/purchase', methods=['POST'])
    def purchase(self):
        transaction: Transaction = Transaction()
        transaction.address = request.get('address')
        transaction.zipcode = request.get('zipcode')
        transaction.country = request.get('country')
        try:
            transaction.save()
        except:
            return jsonify(message="Failure")
        
        products = request.get('products')
        print(producs)
        
    def get_current_user(self) -> dict:
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
        return user