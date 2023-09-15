from app import db

class Fabric(db.Model):
    __tablename__ = 'fabrics'

    id = db.Column(db.Integer, primary_key = True)
    pattern = db.Column(db.String(64))

    orders = db.relationship('Order', backref='fabric')

    def __repr__(self):
        return f'pattern: {self.pattern}'
