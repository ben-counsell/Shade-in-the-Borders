from app import db

class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))

    orders = db.relationship('Order', backref='customer')

    def __repr__(self):
        return f'Customer\'s name: {self.first_name} {self.last_name}'