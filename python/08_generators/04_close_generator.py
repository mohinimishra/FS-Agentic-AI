# from - used to get the yield values from functions
def local_tea() :
    yield "Masala Tea",
    yield "Ginger Tea"
    
def imported_tea():
    yield "Matcha"
    
def all_tea():
    yield from local_tea() 
    yield from imported_tea()
    
for tea in all_tea():
    print(tea)
    
# try, except block 

def stall():
    try:
        while True:
            order = yield
            print(f"Hey Stall is preparing your order {order}")
    except:
        print("Stall closed")

status = stall()
print(next(status))
status.send("Ginger")
status.close()