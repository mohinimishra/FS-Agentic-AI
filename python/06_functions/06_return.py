# By default function returns None
# You can return return single values 
# multiple values

def test_no_return():
    print(f"This function return None")
    
print(f"Test no return {test_no_return()}") # None

def add(a,b):
    addition= a +b 
    return f"Addition of {a} and {b} is {addition}"
print(f" {add(2,3)}")

# Break Early 
def getStatus(status):
    if(status == "active"):
        return "Status is Active"
    return "Status is Deactivated"

print(f"{getStatus('active')}") #Status is Active
print(f"{getStatus('yes')}") #Status is Deactivated

# multiple values return
totalItem = 100
def inventary(sold):
    remainingItem = totalItem - sold
    return {sold}, remainingItem

sold, remainingItem = inventary(50)
print(f"Sold:{type(sold)}, {sold}") # set returns {50}
print(f"remaining:{remainingItem}")
