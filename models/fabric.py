from app import db

class Fabric(db.Model):
    __tablename__ = 'fabrics'

    id = db.Column(db.Integer, primary_key = True)
    pattern = db.Column(db.String(64))
    metres_in_stock = db.Column(db.Integer)

    orders = db.relationship('Order', backref='fabric')

    def __repr__(self):
        return f'pattern: {self.pattern}, metres in stock: {self.metres_in_stock}'
