# Calculate the bill
# WAF that takes number of item per price , total item and return total bill

def calculate_bill(totalItem, pricePerItem):
    price = totalItem*pricePerItem
    return price

my_bill = calculate_bill(5, 10)

print(f"Order 1 {my_bill}")


# Improving Tracebiltiy
# A shop add 10% VAT on every order
# You wnat to be consistence and traceable 
# Task:
    # Write add_vat(price, vat_rate)
    # Use it to compute final pric for 3 orders
    
def add_vat(price, vat_rate):
    return price * (100 + vat_rate/100)

orders = [100,150,200]
for price in orders:
    p= add_vat(price, 10)
    print(f"Orignal price  {price} : Vat price :{p}")

