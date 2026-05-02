# A tea stall offeres diff rice from diff cup sizes.
# Write a program that calculates the price based on size. 
    # Task:
    # Input small, "medium" ,"large"
    # Prices small = 10, medium=15, large=20
    # If invalid show "unknown cup size"

size = input("Choose your cup size (small/medium/large)").lower()

if size == "small":
    print(f"The price of {size} of cup is 10Rs")
elif size == "medium":
    print(f"The price of {size} of cup is 15Rs")
elif size=="large":
    print(f"The price of {size} of cup is 20Rs")
else:
    print(f"unknown cup size")
    
    
    