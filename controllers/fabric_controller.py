from flask import Blueprint, render_template, request, redirect
from models.fabric import Fabric
from models.order import Order
from app import db

fabric_blueprint = Blueprint('fabric', __name__)

@fabric_blueprint.route('/add_fabric', methods=['POST'])
def add_fabric():
    pattern = request.form['fabric_pattern']
    metres_in_stock = request.form['metres_in_stock']
    new_fabric = Fabric(pattern=pattern, metres_in_stock=metres_in_stock)
    db.session.add(new_fabric)
    db.session.commit()
    return redirect('/edit_stock')

@fabric_blueprint.route('/update_fabric_stock/<int:id>', methods=['POST'])
def update_fabric_stock(id):
    new_stock_level = request.form['update_fabric_stock']
    fabric_to_edit = Fabric.query.get(id)
    fabric_to_edit.metres_in_stock = new_stock_level
    db.session.commit()
    return redirect('/edit_stock')

@fabric_blueprint.route('/fabric/delete/<int:id>', methods=['POST'])
def remove_frame(id):
    fabric = Fabric.query.get(id)
    orders = Order.query.all()

    fabric_included_in_open_order = False
    orders_to_be_deleted = []

    for order in orders:
        if order.fabric_id == id:
            fabric_included_in_open_order = True
            orders_to_be_deleted.append(order)

    if fabric_included_in_open_order == True:
        return render_template('/confirm_delete.jinja', orders=orders_to_be_deleted, object=fabric, object_type='fabric')
    else:
        Fabric.query.filter_by(id=id).delete()
        db.session.commit()
        return redirect('/edit_stock')