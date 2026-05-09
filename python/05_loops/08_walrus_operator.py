value=13
remainder = value % 5

if(remainder):
    print(f"Remainder is {remainder}")

# Using Walrus Operator (:=)

if(remainder := value % 5):
     print(f"Remainder is {remainder}")
     
sizes = ["small", "medium", "large"]
if (req_size := input("Please enter your size")) in sizes:
     print(f"Order size is {req_size}")    
else:
     print(f"Not found the {req_size} size")


flavours = ["ginger", "mint", "green"]

while (flavour := input("Enter your flavour")) not in flavours:
     print(f"Flavour {flavour} is not Available")
     
print(f"Flavour {flavour} is available")