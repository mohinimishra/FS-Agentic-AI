# You are preparing an order summary with customer name and total bill.
# Taks:
    # Use two lists: one for name another for bills
    # Print:[name] paid [bill]


names = ["Alice", "Alex", "Crystan", "Sam"]
bills = [50, 10, 100, 500]

for name, bill  in zip(names, bills):
    print(f"{name} paid {bill}rs.")