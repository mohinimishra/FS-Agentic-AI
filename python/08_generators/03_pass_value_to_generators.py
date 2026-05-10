def take_order():
    print(f"Welcome, what would you like to order?")
    order = yield # Program stops on first run as it waits for value to be sent 
    while True:
        print(f"Order is Preparing: {order}")
        order = yield # Stooping the loop wiats for value, once recived go through the loop 
 
order = take_order()
# print(next(order))
next(order) # to start the generator
order.send("Burger") # send value to generator
order.send("Dosa") # send value to generator



