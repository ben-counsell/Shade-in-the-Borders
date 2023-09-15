from flask import Blueprint, render_template, request, redirect
from models.fabric import Fabric
from models.frame import Frame
from models.order import Order
from app import db

fabric_blueprint = Blueprint('fabric', __name__)
frame_blueprint = Blueprint('frame', __name__)
order_blueprint = Blueprint('order', __name__)

@order_blueprint.route('/my_orders/2')
def list_my_orders():
    orders = Order.query.all() # this will need to be changed but it will do for now
    return render_template('my_orders.jinja', orders=orders)

@order_blueprint.route('/make_new_order')
def go_to_new_order_page():
    return render_template('make_new_order.jinja')