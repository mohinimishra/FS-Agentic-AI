# define decorator function

from functools import wraps
def decorator_function(func):
    @wraps(func)
    def wrapper():
        print("Before the wrapper function runs")
        func()
        print("After the wrapper function runs")
    return wrapper

@decorator_function # use this keyword to define the function below this is decorator function
def greet():
    print (f"Welcome")
greet()
print(greet.__name__) # wrapper

print(greet.__name__) # greet if use imported wrap 
