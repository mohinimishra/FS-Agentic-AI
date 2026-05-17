# Error Handling in Python

## Understanding Error Handling Basics

### What is Error Handling and Exception Handling?

```python
# what is error handling
# exception handling 

# keyError
# ZeroDivisionError
# TypeError
# NameError

list= ["Apple", "Mango", "Banana"]
list[2] # throw index error
```

**Simply Explained:**
Error handling is a mechanism in Python that allows you to anticipate and manage problems that occur during program execution. When Python encounters an issue (like accessing an invalid list index), it raises an exception. The common exceptions shown here are:
- **KeyError**: Raised when accessing a non-existent dictionary key
- **ZeroDivisionError**: Raised when dividing by zero
- **TypeError**: Raised when an operation is applied to an incompatible data type
- **NameError**: Raised when a variable name is not defined
- **IndexError**: Raised when accessing an index outside the list range (as shown in line 8)

---

## Try-Except-Else-Finally Structure

### Handling Specific Exceptions with Try-Except

```python
employe = {"name":"Alice", "age":20}

try:
    print(f"{employe['name']} is {employe['age']} years old.")
    employe['gender']
except KeyError:
    print(f"{KeyError.__doc__}")
```

**Simply Explained:**
The `try` block contains code that might cause an error. If accessing `employe['gender']` fails (because the key doesn't exist), the `except KeyError` block catches that specific error and executes instead. The `KeyError.__doc__` displays documentation about the error type.

### Using Try-Except-Else-Finally with Custom Functions

```python
def showEmplyeDetail(name, age, gender):
    try:
        if not name or not age or not gender:
            raise ValueError("Please provide {name} {age} & {gender} value.")
    except ValueError as e:
        print (f"Error {e}")
    else:
        print(f"{name, age, gender}")
    finally:
        print(f"Thanks!")

showEmplyeDetail("alice" ,"20", "Male")
showEmplyeDetail("","","")
```

**Simply Explained:**
- **try**: Attempts to validate that all parameters have values
- **raise ValueError**: Manually triggers an error if validation fails
- **except ValueError as e**: Catches the ValueError and stores it in variable `e` for printing
- **else**: Executes only if no exception was raised (validation passed)
- **finally**: Always executes regardless of whether an exception occurred, useful for cleanup operations

---

## Handling Multiple Exceptions

### Catching Different Exception Types

```python
def process_order(item, tax):
    try:
        price = {"latte":30.0, "mocha":60.0}[item]
        cost = price*tax
        print(f"Order Served : ${cost:.2f}")
    except KeyError:
        print(f"Sorry that item is not available")
    except TypeError:
        print(f"Amount should be number")
    
process_order("mocha", "two") #Amount should be number
process_order("", 20) # Sorry that item is not available
process_order("mocha", {20}) # Amount should be number
```

**Simply Explained:**
When multiple exceptions can occur in a `try` block, you can use multiple `except` blocks to handle each type differently. In this example:
- If `item` is not in the dictionary, `KeyError` is caught
- If `tax` is not a number (like the string "two"), `TypeError` is caught during multiplication
- Each exception type gets its own specific error message

---

## Creating Custom Exceptions

### Defining and Using Custom Exception Classes

```python
def coffee(flavour):
    
    if flavour not in ['masala', 'ginger']:
        raise ValueError (f'This flavour {flavour }is not available')
    
coffee("") # ValueError: This flavour is not available

class FlavourOutageErr(Exception):
    pass

def mocha(flavour):
    if flavour not in ['masala', 'ginger']:
        raise FlavourOutageErr("flavour is not available")
```

**Simply Explained:**
Beyond using built-in exceptions like `ValueError`, you can create your own custom exception classes by inheriting from the `Exception` base class. The first function uses a built-in `ValueError`. The second creates a custom `FlavourOutageErr` exception class and raises it when the flavour is invalid. Custom exceptions allow you to create domain-specific error types that make your code more readable and maintainable.

---

## Mini Project: Coffee Bill Calculator with Error Handling

### Building a Complete Error Handling System

```python
class InvalidError(Exception):
    pass

def bill(flavour, cups):
    menu = {"mocha":130.99, "capacin":440.89}
    try:
        if flavour not in menu:
            raise InvalidError("Flavour is not Available")
        if not isinstance(cups, int):
            raise TypeError("cups value should eb an integer")
        total = menu[flavour] * cups
        print({total}) 
    except Exception as e:
        print(e)
    finally:
        print("Thanksyou for Ordering")

bill("mocha", "10") #cups value should eb an integer
bill("", "10") # flavour is not Available
```

**Simply Explained:**
This mini project combines multiple error handling concepts:
- **Custom Exception**: `InvalidError` is created for invalid flavour selections
- **Validation Checks**: The function checks if the flavour exists in the menu and if cups is an integer
- **Generic Exception Catching**: `except Exception as e` catches any exception type (both custom and built-in)
- **Finally Block**: Executes after the order is processed, whether successful or not, to provide user feedback
- The function demonstrates real-world error handling for a simple billing system

---

## File Handling with Error Handling

### Working with Files Using Context Managers

```python
# file = open("file.txt", "w")
# try:
#     file.write("Hey This is file")
# finally:
#     file.close()

# another way of writing to file "with"

with open("file.txt", "w") as file:
    file.write("Hey I am writing this file using 'with'")

with open("file.txt", "r") as readFile: # behind the seen __enter__() and __exit__() these two call itself
    file.read()
```

**Simply Explained:**
The first commented approach manually opens and closes a file with try-finally to ensure closure. The `with` statement (context manager) is the preferred modern approach because it automatically handles file opening and closing, even if an error occurs. Behind the scenes, `with` calls `__enter__()` when entering the block and `__exit__()` when leaving it, ensuring the file is always properly closed. This prevents file handle leaks and is safer than manual file handling.
