from app import db
from sqlalchemy.sql import func
from app.framework.database.base_model import BaseModel
import time, math, random
from werkzeug.utils import secure_filename
import datetime

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'} 
current_time = lambda: int(round(time.time() * 1000))

class Product(db.Model, BaseModel):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True)
    _product_id = db.Column(db.String(128), unique=True)
    _price = db.Column(db.Float)
    _name = db.Column(db.String(128))
    _description = db.Column(db.String(128), nullable=True)
    _category = db.Column(db.String(128))
    _owner = db.Column(db.String(64), db.ForeignKey("company._company_id"))
    _tag = db.Column(db.String(128), nullable=True)
    _quantity = db.Column(db.Integer)
    _photo = db.Column(db.String(128), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())


    @property
    def photo(self) -> str:
        return self._photo
    
    @photo.setter
    def photo(self, file):
        self._photo = self.hanlde_file(file)

    @property
    def product_id(self) -> str:
        return self._product_id
    
    @product_id.setter
    def product_id(self, length: int) -> str:
        self._product_id = self._generate_product_id(length)

    @property
    def price(self) -> float:
        return self._price
    
    @price.setter
    def price(self, price: float) -> float:
        self._price = price
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name: str) -> str:
        self._name = name
    
    @property
    def description(self) -> str:
        return self._description
    
    @description.setter
    def description(self, description) -> str:
        self._description = description
    
    @property
    def category(self) -> str:
        return self._category
    
    @category.setter
    def category(self, category) -> str:
        self._category = category
    
    @property
    def owner(self) -> str:
        return self._owner
    
    @owner.setter
    def owner(self, owner) -> str:
        self._owner = owner
    
    @property
    def tag(self) -> str:
        return self._tag
    
    @tag.setter
    def tag(self, tag):
        self._tag = tag

    def allowed_file(self, filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def hanlde_file(self, file):
        if self.allowed_file(file.filename):
            filename = secure_filename(file.filename.rsplit('.', 1)[0].lower() + str(datetime.datetime.now()) + '.' + file.filename.rsplit('.', 1)[1].lower())
            file.save('app/static/uploads/' + filename)

            return filename

    def _generate_product_id(self, length=16) -> str:
        """generate unique user_id"""
        character = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        character_length = len(character)
        randomID = ''
        for i in range(length):
            randomID += character[math.floor(random.random() * character_length)]
        return randomID + str(current_time())
