from app import db
from sqlalchemy.sql import func
from app.framework.database.base_model import BaseModel

class Product(db.Model, BaseModel):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True)
    _product_id = db.Column(db.Integer)
    _price = db.Column(db.Float)
    _name = db.Column(db.String(128))
    _description = db.Column(db.String(128))
    _category = db.Column(db.String(128))
    _owner = db.Column(db.String(64), db.ForeignKey("company._company_id"))
    _tag = db.Column(db.String(128))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        self._price = price
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        self._description = description
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        self._category = category
    
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, owner):
        self._owner = owner
    
    @property
    def tag(self):
        return self._tag
    
    @tag.setter
    def tag(self, tag):
        self._tag = tag
