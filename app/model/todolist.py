from app import db


class todolist(db.Model):
    __tablename__ = "todolist"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column("title", db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    creator = db.Column(db.String(64), db.ForeignKey("user.username"))
    task = db.relationship("Todo", backref="author", lazy="dynamic")