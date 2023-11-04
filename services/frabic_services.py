

def get_orders_by_fabric(fabric_id):
    orders = Order.query.all()

    orders_with_fabric = []

    for order in orders:
        if order.fabric_id == id:
            orders_with_fabric.append(order)


# we can set up our tables to delete any children of a parent when deleted, so when we have a one to many, if we delete the 'one' in your code 'Fabric'  it will delete the 'many' e.g it will delete all the orders that have that fabric associated with them. I have shown the syntax in your models.