# mutability inside function:
flavour=['mint', 'ginegr']

def update_order(flavour):
    flavour[1] = "tulsi"
update_order(flavour)

print(f"flavour:{flavour}")


def generate_bill(name, ammount, dish):
    print(f"Dear {name}, Your total order for {dish} is {ammount}")
generate_bill(name="MM", dish="Dosa", ammount=60)

def orderDetails(*details, **moredetails):
    print(f"arg: {details}") # returns tupple arg
    print(f"kwarg-KeywordArg: {moredetails}") # return disctionary of keya\rg
    
orderDetails("Burger", "Noodles", name="MM", dish="Dosa", ammount=60)

# Default arg
def defaultArg(name="mm"):
    print(f"{name}")

defaultArg()

# Default arg trap

def defaultArgTrap(list=[]):
    list.append(1)
    print(f"list here is: {list}")

defaultArgTrap() #[1]
defaultArgTrap() #[1,1]

def defaultArgAssign(list=None):
    if list is None:
        list = []
    list.append(1)
    print(f"list here is: {list}")

defaultArgAssign() #[1]
defaultArgAssign() #[1]

