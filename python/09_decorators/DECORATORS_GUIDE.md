# Decorators in Python

## Understanding Basic Decorators

### Creating and Using Decorator Functions

```python
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
```

**Simply Explained:**
A decorator is a function that modifies or enhances another function or class without permanently changing its source code. Here's what happens behind the scenes:

1. `decorator_function` takes a function (`func`) as an argument
2. Inside it, a `wrapper()` function is defined that:
   - Runs code before calling the original function ("Before...")
   - Calls the original function with `func()`
   - Runs code after the function completes ("After...")
3. The `@decorator_function` syntax is shorthand for `greet = decorator_function(greet)`
4. When you call `greet()`, you're actually calling the `wrapper()` function
5. `@wraps(func)` from `functools` preserves the original function's metadata (like `__name__`)
   - Without `@wraps`, `greet.__name__` would be "wrapper" (the inner function's name)
   - With `@wraps`, `greet.__name__` remains "greet" (the original function's name)
6. Decorators are useful for adding functionality like logging, authentication, or timing without modifying the original function

---

## Building a Logger Decorator

### Creating Reusable Decorators with *args and **kwargs

```python
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
```

**Simply Explained:**
This decorator logs when a function starts and finishes executing. Key concepts:

1. **`*args` and `**kwargs`**: These allow the wrapper to accept any number of positional and keyword arguments
   - `*args` captures all positional arguments as a tuple
   - `**kwargs` captures all keyword arguments as a dictionary
   - This makes the decorator work with any function signature

2. **Execution flow**:
   - When `brew_coffee("mocha")` is called, the wrapper runs first
   - It prints "Calling Function brew_coffee"
   - It calls the original `brew_coffee()` with the same arguments
   - The original function prints "Brewing Tea mocha and no milk available"
   - The wrapper prints "Finished Function brew_coffee" and returns the result

3. **Why return `result`**: 
   - The decorator captures the return value from the original function and passes it back
   - This ensures the decorator doesn't break functions that return values

4. **Benefits**: This logging decorator can be applied to any function to track when it's called and when it completes, without modifying the function's code

---

## Implementing Authorization with Decorators

### Using Decorators for Access Control

```python
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
```

**Simply Explained:**
This decorator acts as a security gate, restricting function access based on a permission level. Here's what happens:

1. **Permission check**: 
   - The wrapper checks if the `role` parameter equals "admin"
   - If `role != "admin"`, it prints "Access Denied" and returns `None` without executing the original function
   - If `role == "admin"`, it calls the original function

2. **Execution flow**:
   - When `get_accesto_inventory("user")` is called:
     - The wrapper checks: is "user" == "admin"? No
     - It prints "Access Denied" and returns `None`
     - The original function never executes
   - When `get_accesto_inventory("admin")` is called:
     - The wrapper checks: is "admin" == "admin"? Yes
     - It calls the original function, which prints "Access Granted"

3. **Why explicit return**:
   - Returning `None` explicitly makes it clear that access was denied
   - This prevents the original function from running and allows calling code to handle the denial gracefully

4. **Real-world use**: This pattern protects sensitive functions by ensuring they only run when the caller has proper permissions, commonly used in web applications and APIs
