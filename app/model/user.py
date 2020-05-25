from app import db, login
from sqlalchemy.sql import func
import bcrypt, math, random
from app.framework.database.base_model import BaseModel
from flask_login import UserMixin



class User(UserMixin, db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    _username = db.Column(db.String(64), index=True, unique=True)
    _user_id = db.Column(db.String(128), unique=True)
    _email = db.Column(db.String(120), index=True, unique=True)
    _password = db.Column(db.String(128))
    _avatar = db.Column(db.String(128), default="/uploads/user.png")
    _place = db.Column(db.String(128), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    @property
    def user_id(self):
        return self._user_id
    
    @user_id.setter
    def user_id(self, length):
        user_unique_id = self.__generate_user_id()
        self._user_id = user_unique_id
    
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

    @property
    def avatar(self):
        return self._avatar
    
    @avatar.setter
    def avatar(self, avatar):
        """Set user avatar image"""
        self._avatar = avatar

    def set_password(self, password : str):
        """Set password for user"""
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    
    def has_correct_password(self, password: str):
        """Return true if password match"""
        return bcrypt.checkpw(password.encode(), self._password.encode())

    def __generate_user_id(self):
        """generate unique user_id"""
        length = 32
        character = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        character_length = len(character)
        randomID = ''
        for i in range(length):
            randomID += character[math.floor(random.random() * character_length)]
        if self.__user_id_exist(randomID) == False:
            return randomID
        else:
            return self.__generate_user_id()


    def __user_id_exist(self, id):
        """Return true if user_id exists"""
        user = User.query.filter_by(_user_id=id).first()
        if user is None:
            return False
        else: 
            return True
        
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

