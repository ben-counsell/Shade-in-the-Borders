from flask import Blueprint, render_template, request, redirect
from models.fabric import Fabric
from models.frame import Frame
from models.customer import Customer
from models.order import Order
from app import db

order_blueprint = Blueprint('order', __name__)

@order_blueprint.route('/view_orders')
def list_all_orders():
    orders = Order.query.all() 
    return render_template('admin_view_orders.jinja', orders=orders)

@order_blueprint.route('/my_orders/2')
def list_my_orders():
    orders = Order.query.filter_by(customer_id=2)
    return render_template('my_orders.jinja', orders=orders)

@order_blueprint.route('/make_new_order')
def go_to_new_order_page():
    frames = Frame.query.all()
    fabrics = Fabric.query.all()
    return render_template('make_new_order.jinja', frames=frames, fabrics=fabrics)

@order_blueprint.route('/make_new_order', methods=['POST'])
def make_new_order():
    frame_style = request.form['frame_style']
    frame_size = request.form['frame_size']
    frames = Frame.query.all()
    for frame in frames:
        if frame.style == frame_style and frame.size == frame_size:
            frame = Frame.query.filter(Frame.size == frame_size, Frame.style == frame_style).one()
            fabric = request.form['fabric_pattern']

            new_order = Order(frame_id=frame.id, fabric_id=fabric, customer_id=2)
            db.session.add(new_order)

            fabric_to_reduce = Fabric.query.get(fabric)
            frame.stock_level -= 1
            fabric_to_reduce.metres_in_stock -= frame.metres_required
            
            db.session.commit()
            return redirect('/my_orders/2')
    fabrics = Fabric.query.all()
    return render_template('make_new_order.jinja', frames=frames, fabrics=fabrics, out_of_stock=True)

@order_blueprint.route('/<object>_delete_order/<int:id>', methods=['POST'])
def delete_order(object, id):
    if object == 'order':
        Order.query.filter_by(id=id).delete()
        return redirect('/view_orders')
    
    orders = Order.query.all()
    orders_to_be_deleted = []

    for order in orders:
        if object == 'frame' and order.frame_id == id:
            orders_to_be_deleted.append(order)
        elif object == 'fabric' and order.fabric_id == id:
            orders_to_be_deleted.append(order)

    for order in orders_to_be_deleted:
        order_to_delete = Order.query.get(order.id)
        db.session.delete(order_to_delete)
        
    db.session.commit()
    
    if object == 'frame':
        Frame.query.filter_by(id=id).delete()
    if object == 'fabric':
        Fabric.query.filter_by(id=id).delete()
    db.session.commit()
    
    return redirect('/add_stock')

@order_blueprint.route('/admin')
def log_in_as_admin():
    return render_template('/admin_home.jinja')

@order_blueprint.route('/add_stock')
def add_stock():
    frames = Frame.query.all()
    fabrics = Fabric.query.all()
    return render_template('/admin_add_stock.jinja', frames=frames, fabrics=fabrics)