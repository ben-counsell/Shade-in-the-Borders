from app import db
from models.fabric import Fabric
from models.frame import Frame
from models.customer import Customer
from models.order import Order
import click

from flask.cli import with_appcontext

@click.command(name='seed')
@with_appcontext
def seed():
    db.drop_all()
    db.create_all()
    fabric1 = Fabric(pattern='Tartan', metres_in_stock=5.0)
    fabric2 = Fabric(pattern='Blue Stripes', metres_in_stock=4.0)
    fabric3 = Fabric(pattern='Paisley', metres_in_stock=3.0)
    fabric4 = Fabric(pattern='Checkerboard', metres_in_stock=2.0)
    frame1 = Frame(style='Short Round', size='S', stock_level=7, metres_required=0.4)
    frame2 = Frame(style='Short Round', size='M', stock_level=7, metres_required=0.6)
    frame3 = Frame(style='Short Round', size='L', stock_level=7, metres_required=0.8)
    frame4 = Frame(style='Square', size='S', stock_level=4, metres_required=0.4)
    frame5 = Frame(style='Square', size='M', stock_level=4, metres_required=0.6)
    frame6 = Frame(style='Square', size='L', stock_level=4, metres_required=0.8)
    frame7 = Frame(style='Cylinder', size='S', stock_level=3, metres_required=0.5)
    frame8 = Frame(style='Cylinder', size='M', stock_level=3, metres_required=0.7)
    frame9 = Frame(style='Cylinder', size='L', stock_level=3, metres_required=0.9)
    frame10 = Frame(style='Cone', size='S', stock_level=3, metres_required=0.4)
    frame11 = Frame(style='Cone', size='M', stock_level=5, metres_required=0.6)
    frame12 = Frame(style='Cone', size='L', stock_level=2, metres_required=0.8)
    customer1 = Customer(first_name='Ben', last_name='Counsell')
    customer2 = Customer(first_name='Johnny', last_name='Johnson')
    order1 = Order(fabric=fabric1, frame=frame2, customer=customer1)
    order2 = Order(fabric=fabric1, frame=frame11, customer=customer1)


    db.session.add(fabric1)
    db.session.add(fabric2)
    db.session.add(fabric3)
    db.session.add(fabric4)

    db.session.add(frame1)
    db.session.add(frame2)
    db.session.add(frame3)
    db.session.add(frame4)
    db.session.add(frame5)
    db.session.add(frame6)
    db.session.add(frame7)
    db.session.add(frame8)
    db.session.add(frame9)
    db.session.add(frame10)
    db.session.add(frame11)
    db.session.add(frame12)

    db.session.add(customer1)
    db.session.add(customer2)

    db.session.add(order1)
    db.session.add(order2)

    db.session.commit()