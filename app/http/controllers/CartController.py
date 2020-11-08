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
            return jsonify(message="Failure", info="There was an error with purchase transaction")

        products = request.get('products')
        for product in products:
            productTransaction: TransactionItem = TransactionItem()
            productTransaction.product_id = product['productID']
            productTransaction.transaction_id = transaction.transaction_id
            productTransaction.quantity = product['productQuantity']
            try:
                productTransaction.save()
            except:
                return jsonify(message="Failure", info="There was an error with purchase transaction")
        return jsonify(message="Success", info=f"Your transaction ID is: {transaction.transaction_id}. Please keep this number to track your products. You can safely clear your carts")
        
    @route('/transaction/<transaction_id>')
    def get_transaction_by_id(self, transaction_id):
        transaction: Transaction = Transaction.query.filter_by(_transaction_id=transaction_id).first()
        transactionItem: TransactionItem = TransactionItem.query.filter_by(_transaction_id=transaction_id).all()

        _data = {
            "transaction_id": transaction.transaction_id,
            "products": transactionItem
        }
        data = json.dumps(_data, cls=AlchemyEncoder)
        return Response(data, mimetype='application/json')

    @route('/transaction/all')
    def all_transactions(self):
        transaction: Transaction = Transaction.query.all()
        data = json.dumps(transaction, cls=AlchemyEncoder)
        return Response(data, mimetype='application/json')

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