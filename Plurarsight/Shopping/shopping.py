import Sales.shoppingCart, Sales.shoppingOrder

cart = Sales.shoppingCart.Cart()
order = Sales.shoppingOrder.Order()
order.getInput()

while not order.quit:
    cart.process(order)
    order = Sales.shoppingOrder.Order()
    order.getInput()

print(cart)
