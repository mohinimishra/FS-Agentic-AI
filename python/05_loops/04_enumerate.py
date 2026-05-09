# You are creating a menu board
# Each item must be numberd
# Task
# Use enumerate() to print menu items with nubers

menu = ["Green", "Lemon", "Spiced", "Mint"]

# enumerate returns a tuple conating count 

for idx, items in enumerate(menu, start=2): 
    print (f"{idx} : {items} chai") 

#output
    """
    2 : Green chai
    3 : Lemon chai
    4 : Spiced chai
    5 : Mint chai
    """