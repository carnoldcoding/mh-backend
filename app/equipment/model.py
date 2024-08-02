from app import db

class Weapon(db.Model):
    __tablename__ = "weapon"

    id = db.Column(db.Integer, primary_key=True)