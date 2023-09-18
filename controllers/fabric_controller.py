from flask import Blueprint, render_template, request, redirect
from models.fabric import Fabric
from models.frame import Frame
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
    return redirect('/add_stock')

@fabric_blueprint.route('/update_fabric_stock/<int:id>', methods=['POST'])
def update_fabric_stock(id):
    new_stock_level = request.form['update_fabric_stock']
    fabric_to_edit = Fabric.query.get(id)
    fabric_to_edit.metres_in_stock = new_stock_level
    db.session.commit()
    return redirect('/add_stock')