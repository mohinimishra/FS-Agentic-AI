# Some ingredients are out of Stock
# You want to skip those and stop entierly if someone requests a restricted ingredient
# Task:
    # Skip if ingredeiant is "out of stock" 
    # Break if flavour is "Discountinued"

flavours = ["ginger", "out of stock", "discontinued",  "mint" ]

for flavour in flavours :
    if flavour == "out of stock":
        continue
    elif flavour == "discontinued":
        print(f"Discounted Item found")
        break
    
    print(f"Item found : {flavour}")

print(f"out of the loop")

employeDetails = [("Alice", 18), ("Brandee", 20), ("Charlee", 13)]

for name, age in employeDetails:
    if age <= 18:
        print(f"{name} is eligble fo this Job")
        break
        
else:
    print(f"No one is elible for this Job")