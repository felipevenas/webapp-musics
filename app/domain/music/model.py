from sqlalchemy import Column, String, Integer

from app.db.config import db

class Music(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    artist = db.Column(db.String(50), nullable=False)
    genre = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' %self.name