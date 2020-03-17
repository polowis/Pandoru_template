from app import db
from sqlalchemy.sql import func


class todolist(db.Model):
    __tablename__ = "todolist"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column("title", db.String(128))
    description = db.Column(db.String(128))
    progess = db.Column(db.String(128))
    creator = db.Column(db.String(64), db.ForeignKey("user.username"))
    deleted = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())