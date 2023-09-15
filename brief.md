# Lampshade Order System

You've been tasked with making an order management system for a local business which makes lampshades. 

## MVP

Customers should be able to select a 'Frame' and 'Pattern' for their lampshade, and add these to an 'Order'. The 'Frame' should have a syle, a size, and a stock level. The 'Pattern' should have a name. The frames and patterns will have a many-to-many relationship, which will be connected by the 'Orders' table.

The customer should be able to access a page which displays all their 'Order's, and click through to edit or remove orders.

## Extensions 

- The frames and patterns should have images which show what they look like.

- The patterns should have a metres_in_stock property. The frames should have a metres_required property which is sensitive to the size of the frame. When the customer places an order, the pattern's metres_in_stock property should reduce by the correct amount. 

- On placing an order, the customer should be prompted to confirm their order. On this page, it should be possible to edit or cancel the order (the edit/remove page from the MVP can be repurposed for this). Once they have confirmed their order, it should no longer be possible for them to alter it.

- Add a price to frames, and a price_per_metre to the patterns. Add a column in 'Orders' which totals the price of each order.

- Make it so that more than one lampshade can be ordered at a time.