from functools import wraps
def requireAdmin(func):
    @wraps(func)
    def wrapper(role):
        if role != "admin":
            print("Acess Denied")
            return None # it always best to return,let it  do explicit return 
        else:
            return func(role)
    return wrapper

@requireAdmin
def get_accesto_inventory(role):
    print("Acess Granted")
    
get_accesto_inventory("user")
get_accesto_inventory("admin")

    