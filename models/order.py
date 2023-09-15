from app import db
from models.fabric import Fabric
from models.frame import Frame

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key = True)
    fabric_id = db.Column(db.Integer, db.ForeignKey('fabrics.id'))
    frame_id = db.Column(db.Integer, db.ForeignKey('frames.id'))

    # CHECK IF THIS WORKS AT SOME POINT:
    def __repr__(self):
        fabric = Fabric.query.get(self.fabric_id)
        frame = Frame.query.get(self.frame_id)
        return f'Frame style: {frame.style}, Fabric pattern: {fabric.pattern}'