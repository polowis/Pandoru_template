from app import db
from sqlalchemy.sql import func
from app.framework.database.base_model import BaseModel
import time, math, random
from werkzeug.utils import secure_filename
import datetime

class TransactionItem(db.Model, BaseModel):
    __tablename__ = "transaction_item"
    id = db.Column(db.Integer, primary_key=True)
    _quantity = db.Column(db.Integer)
    _transaction_id = db.Column(db.String(64), db.ForeignKey("transaction._transaction_id"))
    _product_id = db.Column(db.String(128), db.ForeignKey('product._product_id'))
    _product = db.relationship("Product", backref=db.backref("product", uselist=False))

    @property
    def product_id(self):
        return self._product_id
    
    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    
    @property
    def transaction_id(self):
        return self._transaction_id
    
    @transaction_id.setter
    def transaction_id(self, value):
        self._transaction_id = value
    
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    
    @property
    def product(self):
        return self._product
    

