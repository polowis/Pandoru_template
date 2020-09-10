from app import db
from sqlalchemy.sql import func
from app.framework.database.base_model import BaseModel
import bcrypt, math, random

class Company(db.Model, BaseModel):
    __tablename__ = "company"
    id = db.Column(db.Integer, primary_key=True)
    _company_id = db.Column(db.String(128))
    _company_name = db.Column(db.String(128))
    _contact_name = db.Column(db.String(128))
    _contact_title = db.Column(db.String(128))
    _contact_number = db.Column(db.String(128))
    _mailing_address = db.Column(db.String(128))
    _business_type = db.Column(db.String(128))
    _password = db.Column(db.String(128))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())


    # company name
    @property
    def company_name(self):
        return self._company_name
    
    @company_name.setter
    def company_name(self, company_name):
        self._company_name = company_name
    
    # contact number
    @property
    def contact_number(self):
        return self._contact_number
    
    @contact_number.setter
    def contact_number(self, contact_number):
        self._contact_number = contact_number
    
    # contact name
    @property
    def contact_name(self):
        return self.contact_name
    
    @contact_name.setter
    def contact_name(self, contact_name):
        self._contact_name = contact_name
    
    @property
    def contact_title(self):
        return self._contact_title
    
    @contact_title.setter
    def contact_title(self, contact_title):
        self._contact_title = contact_title
    
    @property
    def mailing_address(self):
        return self._mailing_address
    
    @mailing_address.setter
    def mailing_address(self, mailing_address):
        self.mailing_address = mailing_address
    
    @property
    def business_type(self):
        return _business_type
    
    @business_type.setter
    def business_type(self, business_type):
        self._business_type = business_type
    
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        if not bool(password):
            raise ValueError("no password given")

        self._password = self.set_password(password)
        
    def set_password(self, password : str):
        """Set password for user"""
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    
    def has_correct_password(self, password: str):
        """Return true if password match"""
        return bcrypt.checkpw(password.encode(), self._password.encode())
    
    


