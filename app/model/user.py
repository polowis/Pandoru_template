from app import db, login
from sqlalchemy.sql import func
import bcrypt
from app.framework.database.base_model import BaseModel
from flask_login import UserMixin

class User(UserMixin, db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    _username = db.Column(db.String(64), index=True, unique=True)
    _email = db.Column(db.String(120), index=True, unique=True)
    _password = db.Column(db.String(128))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username: str):
        self._username = username
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email: str):
        self._email = email
    
    @property
    def password(self):
        return self.password
    
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

@login.user_loader
def load_user(id):
    return User.query.get(int(id))