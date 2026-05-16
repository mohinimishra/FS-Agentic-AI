class Vehical:
    name = "Royal Enfiled"
    wheel= 2
    color="black"
    
vehical_details = Vehical()
print(f"Vehical Details {vehical_details.color}")

vehical_details.power = "350 CC"
print(f"Vehical Details After Adding new atribute {vehical_details.power}")

del vehical_details.power
# print(f"After Remove power attribute", vehical_details.power) # give error as its been deleted


vehical_details.color = "Gray"
# print(f"Vehical Details After Updating an atribute {vehical_details.color}")

del vehical_details.color
print(f"delting class property ", vehical_details.color) # it give class atribute value not dlete it Shadowing
