from app.db.config import db

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(70), nullable=False)
    login = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return '<Name %r>' %self.name