from app import db
from models.frame import Frame

class Fabric(db.Model):
    __tablename__ = 'fabrics'

    id = db.Column(db.Integer, primary_key = True)
    pattern = db.Column(db.String(64))
    metres_in_stock = db.Column(db.Float)

    orders = db.relationship('Order', backref='fabric')
    # for setting up the delete cascade
    # orders = db.relationship('Order', backref='fabric',cascade='all, delete-orphan')

    def __repr__(self):
        return f'pattern: {self.pattern}, metres in stock: {self.metres_in_stock}'
    
    def reduce_stock_by_frame_size(id, frame):
        pass
