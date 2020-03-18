from app import db
from sqlalchemy.sql import func
from app.framework.database.base_model import BaseModel


class ToDoList(db.Model, BaseModel):
    __tablename__ = "todolist"
    id = db.Column(db.Integer, primary_key=True)
    _title = db.Column(db.String(128))
    _description = db.Column(db.String(128))
    _progress = db.Column(db.String(128))
    _creator = db.Column(db.String(64), db.ForeignKey("user._user_id"))
    _done = db.Column(db.Boolean(), default=False)
    deleted = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        self._description = description
    
    @property
    def progress(self):
        return self._progress
    
    @progress.setter
    def progress(self, progress):
        self._progress = progress
    
    @property
    def author(self):
        return self._creator
    
    @author.setter
    def author(self, author):
        self._creator = author