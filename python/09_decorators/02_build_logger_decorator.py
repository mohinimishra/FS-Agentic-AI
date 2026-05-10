from functools import wraps

def logActivity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling Fucntion {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finshed Fucntion {func.__name__}")
        return result
    return wrapper

@logActivity
def brew_coffee(type, milk="no"):
    print(f"Brewing Tea {type} and {milk} milk available")
brew_coffee("mocha")


