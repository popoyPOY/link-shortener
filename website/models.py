from . import db


class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(300))
    shorten_url = db.Column(db.String(300))