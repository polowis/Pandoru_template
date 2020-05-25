from app import db
from sqlalchemy.sql import func
from app.framework.database.base_model import BaseModel

class Status(db.Model, BaseModel):
    __tablename__ = "status"
    id = db.Column(db.Integer, primary_key=True)
    _content = db.Column(db.String(128))
    _creator = db.Column(db.String(64), db.ForeignKey("user._user_id"))
    _title = db.Column(db.String(128), nullable=True)
    _photo = db.Column(db.String(128), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    @property
    def content(self):
        return self._content
    
    @content.setter
    def content(self, content):
        self._content = content
    
    @property
    def creator(self):
        return self._creator
    
    @creator.setter
    def creator(self, creator):
        self._creator = creator
    
    @property
    def photo(self):
        return self._photo
    
    @photo.setter
    def photo(self, photo):
        self._photo = photo