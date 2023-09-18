from app import db
from models.fabric import Fabric
from models.frame import Frame
from models.order import Order
import click

from flask.cli import with_appcontext

@click.command(name='seed')
@with_appcontext
def seed():
    db.drop_all()
    db.create_all()
    fabric1 = Fabric(pattern='Tartan', metres_in_stock=5)
    fabric2 = Fabric(pattern='Blue', metres_in_stock=4)
    fabric3 = Fabric(pattern='Paisley', metres_in_stock=3)
    frame1 = Frame(style='Short Round', size='M', stock_level=7)
    frame2 = Frame(style='Square', size='S', stock_level=4)
    frame3 = Frame(style='Cylinder', size='L', stock_level=3)

    db.session.add(fabric1)
    db.session.add(fabric2)
    db.session.add(fabric3)

    db.session.add(frame1)
    db.session.add(frame2)
    db.session.add(frame3)

    db.session.commit()