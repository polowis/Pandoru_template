from app import db
from sqlalchemy.sql import func
from app.framework.database.base_model import BaseModel
import time, math, random
from werkzeug.utils import secure_filename
import datetime

current_time = lambda: int(round(time.time() * 1000))
def generate_transaction_id(length=25) -> str:
        """generate unique transaction_id"""
        character = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        character_length = len(character)
        randomID = ''
        for i in range(length):
            randomID += character[math.floor(random.random() * character_length)]
        return randomID + str(current_time())


class Transaction(db.Model, BaseModel):
    __tablename__ = "transaction"
    id = db.Column(db.Integer, primary_key=True)
    _transaction_id = db.Column(db.String(128), unique=True, default=generate_transaction_id())
    _zipcode = db.Column(db.String(128))
    _address = db.Column(db.String(128))
    _country = db.Column(db.String(128), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())


    @property
    def transaction_id(self):
        return self._transaction_id
    
    @transaction_id.setter
    def transaction_id(self, length):
        self._transaction_id = generate_transaction_id()
    
    @property
    def zipcode(self):
        return self._zipcode
    
    @zipcode.setter
    def zipcode(self, zipcode):
        self._zipcode = zipcode
    
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, address):
        self._address = address

    @property
    def country(self):
        return self._country
    
    @country.setter
    def country(self, country):
        self._country = country

    