from flask import Blueprint, render_template, request, redirect
from models.fabric import Fabric
from models.order import Order
from services.frabic_services import get_orders_by_fabric
from app import db

fabric_blueprint = Blueprint('fabric', __name__)
# you should try and follow the RESTful routing conventions naming your endpoints. here is a nice guide on the matter : https://restfulapi.net/resource-naming/
# basically having it a systematic way helps with naming our routes and helps developers at a glace understand what a route's purpose is.
# so this route would be "/fabrics"
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
# we can consider extracting out logic and extra verbosity from our controller functions, we care more about _what_ are code is doing as opposed to _how_ its doing it. 
# see below for example
# this has the following benefits ..

# 1. Separation of concerns
# One of the core principles of software engineering is the separation of concerns. By moving business logic out of controllers and into separate components, you ensure that each component has a single responsibility. Controllers should primarily handle user input and orchestrate the flow of data, while logic related to data manipulation, validation, and business rules should be handled by other parts of the application.
# 2. Code Reusability (keeps us DRY)
# Extracting logic into separate modules or classes makes it more reusable. You can use the same logic in multiple controllers or even in different parts of your application. This reduces code duplication and leads to a more maintainable codebase.
# 3. Scalable 
# As your application grows, you may need to change or extend its functionality, if we have to do the same action several times, it helps if we have the logic to do that action central to one place if we suddenly need to change how we are doing that action we now need to just change the code in one place as apposed to every place we where doing that action.
# 4. Readability 
# Controllers are typically responsible for managing the flow of requests and responses. When logic is mixed with controller code, it can make controllers bulky and less readable. Extracting logic into separate files/folders leads to cleaner, more focused, and more readable code. This improves the overall maintainability of the application. 

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
        # can do this refactor, it makes a bit more sense imo
        # Fabric.query.get(id=id).delete()

        Fabric.query.filter_by(id=id).delete()
        db.session.commit()
        return redirect('/edit_stock')
###########################
# Example of extracting out code refactor 
########################### 
# replaces logic with very human readable code, if people want to look at the implementation they can look at the 'get_orders_by_fabric' function.
@fabric_blueprint.route('/fabric/delete/<int:id>', methods=['POST'])
def remove_frame(id):
    fabric = Fabric.query.get(id)

    orders_to_be_deleted = get_orders_by_fabric(id)

    if len(orders_to_be_deleted) > 0:
        return render_template('/confirm_delete.jinja', orders=orders_to_be_deleted, object=fabric, object_type='fabric')
    else:
        Fabric.query.filter_by(id=id).delete()
        db.session.commit()
        return redirect('/edit_stock')