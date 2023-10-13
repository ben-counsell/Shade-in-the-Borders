from app import db
from models.fabric import Fabric
from models.frame import Frame
from models.customer import Customer

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key = True)
    fabric_id = db.Column(db.Integer, db.ForeignKey('fabrics.id'))
    frame_id = db.Column(db.Integer, db.ForeignKey('frames.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))

    def __repr__(self):
        fabric = Fabric.query.get(self.fabric_id)
        frame = Frame.query.get(self.frame_id)
        customer = Customer.query.get(self.customer_id)
        return f'Frame style: {frame.style}, Fabric pattern: {fabric.pattern}, Customer: {customer.first_name} {customer.last_name}'