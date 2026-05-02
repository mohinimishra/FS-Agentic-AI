# Yo run a program which take input amount
# if amount is greatr than 300 then free delivery fee 
# otherwise it costs 30rs.
# Tasks:
    # input : 'order_amount'
    # use teranry operator to decide delivery fee

order_amount = int(input("Enter the amount : ")) # always return string so needs to convert

delivery_fee = 0 if order_amount>300 else 30

print(f"Delivery Fee is : {delivery_fee}")