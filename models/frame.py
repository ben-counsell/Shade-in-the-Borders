from app import db

class Frame(db.Model):
    __tablename__ = 'frames'
    id = db.Column(db.Integer, primary_key = True)
    style = db.Column(db.String(64))
    size = db.Column(db.String(64))
    stock_level = db.Column(db.Integer)
    metres_required = db.Column(db.Float)

    orders = db.relationship('Order', backref='frame')

    def __repr__(self):
        return f'Style: {self.style}, Size: {self.size}, Stock level: {self.stock_level}'
