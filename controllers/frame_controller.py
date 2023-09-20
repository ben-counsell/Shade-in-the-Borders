from flask import Blueprint, render_template, request, redirect
from models.fabric import Fabric
from models.frame import Frame
from models.customer import Customer
from models.order import Order
from app import db

frame_blueprint = Blueprint('frame', __name__)

@frame_blueprint.route('/add_frame', methods=['POST'])
def add_frame():
    style = request.form['frame_style']
    size = request.form['frame_size']
    stock = request.form['frame_stock']
    new_frame = Frame(style=style, size=size, stock_level=stock)
    db.session.add(new_frame)
    db.session.commit()
    return redirect('/add_stock')

@frame_blueprint.route('/update_frame_stock/<int:id>', methods=['POST'])
def update_frame_stock(id):
    new_stock_level = request.form['update_frame_stock']
    frame_to_edit = Frame.query.get(id)
    frame_to_edit.stock_level = new_stock_level
    db.session.commit()
    return redirect('/add_stock')

@frame_blueprint.route('/frame/delete/<int:id>', methods=['POST'])
def remove_frame(id):
    frame = Frame.query.get(id)
    orders = Order.query.all()

    frame_included_in_open_order = False
    orders_to_be_deleted = []

    for order in orders:
        if order.frame_id == id:
            frame_included_in_open_order = True
            orders_to_be_deleted.append(order)

    if frame_included_in_open_order == True:
        return render_template('/confirm_delete.jinja', orders=orders_to_be_deleted, frame=frame, object='frame')
    else:
        Frame.query.filter_by(id=id).delete()
        db.session.commit()
        return redirect('/add_stock')