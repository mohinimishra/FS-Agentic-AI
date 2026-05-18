# Functions in Python

## Understanding Functions and DRY Principle

### Reducing Code Duplication and Splitting Complex Tasks

```python
#  Reduce Code Duplication
# You are managing a store 
# You recive many orders and you wnat to print the customer name along with type of item they orderd.
# Task
    # write a function print_order(name, item)
    # Call it multiple items for different Customers

customers=["alice", "lufi", "jen"]
items=["bread", "choclate", "milk"]

def print_order(name,item):
        print(f"{name} bought {item}")
        
print_order("alice", "bread")
print_order("lufi", "choclate")
print_order("jen", "milk")
        
for name, item in zip(customers, items):
        print_order(name, item) 

# Spliting a Complex Task
# You are creating monthly report for an resturant sales.
# Istaed of putting all logic in one place, break it down
# Task
    # fetch_sales()
    # filter valid_orders()
    # summarize_data()
    
def fetch_sales():
        print(f"Fetching Sales Data")
        
def valid_orders():
        print(f"Fetching Valid Orders")
        
def summarize_data():
        print(f"Orders Details")
        
def generate_data():
        fetch_sales()
        valid_orders()
        summarize_data()
        print(f"report is ready!")
generate_data()
        
# Hidiing Implementaion Details

    # You are building an app that registers usesrs
    # You want seprate concerns: getting input, validating and saving.
    # Task:
        #Writing register user() that calls
        # get_imput()
        # validate_input()
        # save_To_db()

def get_input():
    print(f"Getting the input")
    
def validate_input():
    print(f"Validating the input")

def save_To_db():
    print(f"Saving to DB")

def users():
    get_input()
    validate_input()
    save_To_db()
    print(f"User Registerd")
users()
```

**Simply Explained:**
Functions are reusable blocks of code that perform specific tasks. This example demonstrates three key principles:

1. **Reducing Code Duplication (DRY - Don't Repeat Yourself)**:
   - Without `print_order()`, you'd write `print(f"{name} bought {item}")` three times
   - With the function, you write it once and call it multiple times with different inputs
   - Calling the function in a loop shows how to apply it to many items efficiently

2. **Splitting Complex Tasks**:
   - Breaking a monthly report into smaller functions (`fetch_sales()`, `valid_orders()`, `summarize_data()`)
   - Makes the code modular and easier to understand
   - Each function has a single responsibility, making it easier to test and maintain

3. **Hiding Implementation Details**:
   - The `users()` function calls smaller helper functions internally
   - The caller doesn't need to know how registration works, just that it works
   - This encapsulation makes code cleaner and easier to change implementation later

---

## Using Return Values and Calculating Results

### Returning Values and Improving Traceability

```python
# Calculate the bill
# WAF that takes number of item per price , total item and return total bill

def calculate_bill(totalItem, pricePerItem):
    price = totalItem*pricePerItem
    return price

my_bill = calculate_bill(5, 10)

print(f"Order 1 {my_bill}")


# Improving Tracebiltiy
# A shop add 10% VAT on every order
# You wnat to be consistence and traceable 
# Task:
    # Write add_vat(price, vat_rate)
    # Use it to compute final pric for 3 orders
    
def add_vat(price, vat_rate):
    return price * (100 + vat_rate/100)

orders = [100,150,200]
for price in orders:
    p= add_vat(price, 10)
    print(f"Orignal price  {price} : Vat price :{p}")
```

**Simply Explained:**
Functions can return values that you can use elsewhere in your program. Here's what happens behind the scenes:

1. **Calculate Bill Function**:
   - Takes two parameters: `totalItem` and `pricePerItem`
   - Multiplies them together to get the price
   - `return price` sends the result back to the caller
   - The caller stores the result in `my_bill` and uses it

2. **Improving Traceability with VAT**:
   - `add_vat()` takes a price and VAT rate, calculates the final price with tax
   - The function consistently applies the same VAT calculation everywhere
   - If the tax law changes, you only need to update one function
   - This centralization makes the code traceable and maintainable
   - Looping through `orders` and calling the function for each ensures consistency

3. **Benefits of returning values**: Functions become reusable tools that compute and provide data to other parts of your program

---

## Understanding Variable Scope and Namespace

### Local, Enclosing, Global, and Built-in Scopes

```python
# Scopes and Name Resolution:

    # Local Scope - inside a function
    # Enclosing form outer function if nested
    # Global Scoping - Top level script
    # Build in 

def inside_scope():
    name = "Java" # inside scope
    print(f"Inside function scope : {name}")  
inside_scope()

name = "Python" # global scope
print(f"Outside scope : {name} ")
inside_scope()


# Enclosing

def outer_function():
    flavour = "ginger"
    def inner_function():
        flavour = "mint"
        print(f"Selected flavour : {flavour}") # mint
    inner_function()
    print(f"Selected Flavour : {flavour}") # ginger
    
outer_function()
```

**Simply Explained:**
Python uses a concept called LEGB (Local, Enclosing, Global, Built-in) to resolve variable names. Here's what happens behind the scenes:

1. **Local Scope**:
   - Variables created inside a function are local to that function
   - In `inside_scope()`, `name = "Java"` is only accessible within that function
   - When the function ends, local variables are destroyed

2. **Global Scope**:
   - Variables defined at the top level of a script are global
   - `name = "Python"` at the script level can be accessed anywhere (if not shadowed by local scope)
   - When `inside_scope()` runs, it has its own local `name` that shadows the global one

3. **Enclosing Scope**:
   - In nested functions, an inner function can access the outer function's variables
   - `outer_function()` defines `flavour = "ginger"`
   - `inner_function()` creates its own local `flavour = "mint"`
   - Each prints its own version of `flavour` (inner prints "mint", outer prints "ginger")
   - They don't interfere with each other because each has its own local scope

4. **Name Resolution Order**: Python searches for variables in this order: Local → Enclosing → Global → Built-in

---

## Using Nonlocal and Global Keywords

### Modifying Variables from Outer Scopes

```python
# NonLocal -
def update_order():
    flavour= "ginger"
    def kitchen_update():
        # nonlocal flavour # only check for outer functions, dosent make it global
        # flavour = "mint"
        def  printUpdate():
            nonlocal flavour # only check for outer functions, dosent make it global
            flavour = "mint"
        printUpdate()
    kitchen_update()
    print(f"Order after kitchen update:{flavour}") # mint 
update_order()

# Global - can call anywhere

status = "order taken"

def update_status():
    def kitchen_update():
        global status
        status = "cooked"
    kitchen_update()
update_status()
print(f"Updated status:{status}")
```

**Simply Explained:**
By default, assigning to a variable in a function creates a local variable. To modify variables from outer scopes, use `nonlocal` or `global` keywords. Here's what happens:

1. **Nonlocal Keyword**:
   - `nonlocal flavour` tells Python: "I'm referring to the `flavour` variable from an enclosing function, not creating a new local one"
   - In `printUpdate()`, `nonlocal flavour` lets it modify the `flavour` from `update_order()`
   - The assignment `flavour = "mint"` updates the outer function's variable, not a local one
   - `nonlocal` only searches enclosing functions, not the global scope

2. **Global Keyword**:
   - `global status` tells Python: "I'm referring to the global `status` variable"
   - Inside `kitchen_update()`, even though it's deeply nested, `global status` lets it reach the module-level variable
   - `status = "cooked"` modifies the global variable, affecting code outside any function
   - This change persists after the function ends

3. **Key difference**:
   - `nonlocal`: Modifies variables in the enclosing function
   - `global`: Modifies variables at the script/module level
   - Without these keywords, assignment creates a new local variable

---

## Handling Function Arguments

### Mutability, Default Arguments, and Flexible Parameters

```python
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
```

**Simply Explained:**
Functions handle arguments in different ways depending on mutability, default values, and parameter types. Here's what happens:

1. **Mutability and Pass-by-Reference**:
   - Lists are mutable (changeable), so when passed to a function, the function receives a reference to the same list
   - `update_order()` modifies the list directly: `flavour[1] = "tulsi"` changes the original list
   - The original `flavour` outside the function is affected
   - This is different from immutable types (like integers), which are "pass-by-value"

2. **Named Arguments (Keyword Arguments)**:
   - `generate_bill(name="MM", dish="Dosa", ammount=60)` passes arguments by name, not position
   - Order doesn't matter; Python matches names to parameters
   - This makes code more readable and less error-prone

3. **`*args` and `**kwargs`**:
   - `*details` captures all positional arguments into a tuple
   - `**moredetails` captures all keyword arguments into a dictionary
   - This allows functions to accept flexible numbers of arguments
   - Useful when you don't know how many arguments will be passed

4. **Default Arguments**:
   - `def defaultArg(name="mm")` sets a default value
   - If no argument is provided, `name` defaults to "mm"
   - Enables functions to work with or without arguments

5. **Default Argument Trap** (Common Gotcha):
   - `def defaultArgTrap(list=[])` uses a mutable default value
   - Python creates this empty list ONCE when the function is defined
   - Every call reuses the same list object, so `append()` keeps adding to it
   - First call: `[1]`, Second call: `[1,1]` (not `[1]` again!)
   - **Fix**: Use `list=None` and create a new list inside the function
   - This ensures each call gets a fresh list

---

## Understanding Return Values and Multiple Returns

### Returning Single, Multiple, and No Values

```python
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
```

**Simply Explained:**
Functions can return different types of values or nothing at all. Here's what happens:

1. **No Return Statement**:
   - Functions without a `return` statement implicitly return `None`
   - `test_no_return()` prints output but returns `None`

2. **Single Value Return**:
   - `add()` computes a result and returns it
   - The caller receives and uses that value

3. **Early Return for Logic Control**:
   - `getStatus()` checks a condition and returns early if it's true
   - If the condition is false, it skips to the next `return` statement
   - This pattern avoids deep nesting and makes code clearer

4. **Multiple Value Return**:
   - `return {sold}, remainingItem` returns two values
   - This creates a tuple: `({50}, 50)`
   - The caller can unpack it: `sold, remainingItem = inventary(50)`
   - Note: `{sold}` creates a set, not the integer itself (quirk in this example)

---

## Working with Lambda, Pure, and Recursive Functions

### Anonymous Functions, Side Effects, and Function Calling Itself

```python
# Types of Functions
# Pure vs Impure functions
# Recursive functions
# Lambdas (Annonymus function without name)

# Pure functions- which dosent manipulate the global variable
def pure_fucntions(value):
    return value * 2

# Not Recomended
# Impure functions- which manipulate the global variable
totalItem = 2;
def impure_fucntions(value):
    global totalItem
    totalItem += totalItem
    return totalItem

# Recursive Functions
total = 1
def factorial(n):
    global total
    if(n == 0):
        return total
    else:
        total = n*total
        
    return factorial(n-1)
        
print(f"{factorial(5)}")
print(f"{factorial(10)}")

# Upgraded 
def fac(n):
    if n==0 or n==1:
        return 1
    return n * fac(n-1)

# Lambdas
yearList = [100,200,500,200,300,200]
filterValue = list(filter(lambda yr: yr>100, yearList))
print(filterValue)
```

**Simply Explained:**
Functions come in different types with different characteristics and use cases. Here's what happens:

1. **Pure Functions**:
   - `pure_fucntions(value)` takes an input and returns an output based only on that input
   - It doesn't modify any global variables or cause side effects
   - Same input always produces same output (predictable)
   - **Benefits**: Easier to test, debug, and reason about

2. **Impure Functions** (Not Recommended):
   - `impure_fucntions()` modifies a global variable `totalItem`
   - Its output depends on external state, not just the parameter
   - Calling it twice with the same input produces different outputs
   - **Drawbacks**: Harder to predict, test, and debug; can cause unexpected side effects

3. **Recursive Functions**:
   - A function that calls itself to solve a problem by breaking it into smaller versions
   - The first `factorial()` function has a base case (`if n == 0`) and recursive case
   - The improved `fac()` is cleaner: it checks if `n` is 0 or 1 (base cases) and returns the result, otherwise calls itself with `n-1`
   - Each recursive call works on a smaller problem until reaching the base case
   - **Risk**: Stack overflow if recursion goes too deep

4. **Lambda Functions** (Anonymous Functions):
   - `lambda yr: yr>100` is an unnamed function that takes one parameter `yr` and returns whether it's greater than 100
   - Lambda syntax: `lambda arguments: expression`
   - Useful for short, one-time-use functions
   - Commonly used with `filter()`, `map()`, and `sorted()`
   - `filter(lambda yr: yr>100, yearList)` keeps only items where the lambda returns True
   - Result: `[200, 500, 300, 200]` (all items greater than 100)

---

## Using Built-in Functions and Documentation

### Accessing Function Metadata and Help

```python
# Built in functions - Python interpreters has number of functions and types built into it that are alwyas available.

# Function documentaion string( has to be very first line to be consider as doc in triple quotes)

def showStatus(status ="Active"):
    """
    This returns the status 
    : param status: your status
    """
    return status
print(showStatus())
print(showStatus.__doc__)
print(showStatus.__name__)

# help(len)
```

**Simply Explained:**
Functions have built-in metadata that you can access. Here's what happens:

1. **Documentation String (Docstring)**:
   - The triple-quoted string immediately after `def` is a docstring
   - It must be the very first statement in the function to be recognized as documentation
   - It explains what the function does, parameters, and return value
   - `showStatus()` has a docstring explaining its purpose

2. **Accessing Metadata**:
   - `showStatus.__doc__` returns the docstring
   - `showStatus.__name__` returns the function's name as a string ("showStatus")
   - `showStatus()` calls the function with default parameter, returns "Active"

3. **Built-in Functions**:
   - Python provides many pre-built functions like `len()`, `print()`, `sum()`, `max()`, etc.
   - `help(len)` displays documentation for any function
   - You can explore built-in functions to avoid reinventing the wheel

---

## Importing and Using Modules

### Organizing Code Across Multiple Files

```python
# Importing Objects/Functions
import sample_business.recepies.flavours as recepies # import all from module

print(f"{recepies.ginger_tea()}")
```

**Simply Explained:**
As your code grows, you can organize functions into separate files (modules) and import them. Here's what happens:

1. **Module Structure**:
   - `sample_business/` is a package (folder)
   - `recepies/` is a sub-package inside it
   - `flavours.py` is a module containing functions like `ginger_tea()` and `masla_tea()`

2. **Import Statement**:
   - `import sample_business.recepies.flavours as recepies`
   - Navigates the folder structure and imports the module
   - `as recepies` creates an alias for easier reference

3. **Usage**:
   - `recepies.ginger_tea()` calls the function from the imported module
   - Functions in separate files can be reused across projects
   - Keeps code organized and maintainable

4. **Module Initialization** (`__init__.py`):
   - The `__init__.py` file makes a folder a Python package
   - In Python 3.3+, it's optional (namespace packages), but still useful
   - Allows you to control what gets imported and add package-level code
