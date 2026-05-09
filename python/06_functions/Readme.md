# Functions

This folder contains various function-related scripts that cover different aspects of function programming in Python. Each file in this folder provides examples and explanations of different concepts related to functions.

## Understanding the Purpose and Benefits of Using Functions

Functions are reusable blocks of code that perform a specific task. They provide several benefits, including:

- **Modularity**: Functions allow you to break down complex tasks into smaller, manageable pieces. This makes your code more organized and easier to understand.

- **Code Reusability**: Functions can be called multiple times with different inputs, allowing you to reuse code and avoid duplication.

- **Improved Maintainability**: Functions encapsulate code logic, making it easier to maintain and update. Changes made to a function can be applied across multiple parts of your codebase.

- **Improved Readability**: Functions provide a clear and concise way to describe what a piece of code does. They make your code more readable and easier to understand.

## Creating Reusable and Modular Code Using "def"

Functions are defined using the `def` keyword in Python. Here's an example of how to define a function:

```python
def add(a, b):
    return a + b

# Call the function
result = add(3, 5)
print(result)  # Output: 8
```

## Scopes and Name Resolution

Python has different scopes for variables, including:

- Local Scope: Variables defined inside a function belong to the local scope of that function.
```python
def my_function():
    x = 10
    print(x)
```
- Enclosing Scope: Variables defined in a nested function belong to the local scope of the enclosing function.
```python
def outer_function():
    x = 10

    def inner_function():
        print(x)

    inner_function()
```
- Global Scope: Variables defined at the top level of a module or script belong to the global scope.
```python
```python
x = 10
print(x)  # Output: 10
```
```
- Built-in Scope: Variables defined in the built-in module `__builtins__` belong to the built-in scope.

- nonlocal scope: variables defined in a nested function can be accessed from the parent function using the `nonlocal` keyword.
```python
def outer_function():
    x = 10

    def inner_function():
        nonlocal x
        x = 20  # Update the value of x in the enclosing scope  

    inner_function()
    print(x)  # Output: 20
```
- global scope: variables defined at the top level of a module or script can be accessed from anywhere in the module using the `global` keyword.
```python
x = 10

def my_function():  
    global x    
    x = 20  # Update the value of x in the global scope

my_function()   
print(x)  # Output: 20
```
## Handling Argument and returns value

Functions can accept arguments and return values. Here's an example:

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8
```

## Return Multiple Values

Functions can return multiple values using a tuple. Here's an example:

```python
def calculate(a, b):
    sum = a + b
    difference = a - b
    return sum, difference  

result = calculate(3, 5)
print(result)  # Output: (8, -2)    
```

## Pass by Value and Pass by Reference

Functions can accept arguments by value and by reference. Here's an example:

```python
def modify_list(lst):
    lst.append(4)   

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]
``` 

## Lambda Functions

Lambda functions are anonymous functions that can be defined using the `lambda` keyword. They are useful when you need to create small, one-time functions. Here's an example:

```python
add = lambda a, b: a + b
result = add(3, 5)
print(result)  # Output: 8
```
# Recursive Functions

Recursive functions are functions that call themselves. They are useful when you need to solve a problem that can be broken down into smaller subproblems. Here's an example:

```python    
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result)  # Output: 120
```

## Use of *args and **kwargs

*args and **kwargs are used to pass a variable number of arguments to a function. Here's an example:

```python
def print_args(*args):
    for arg in args:
        print(arg)

print_args(1, 2, 3)  # Output: 1 2 3
```

## Use of map, filter and reduce

map, filter and reduce are higher-order functions that allow you to apply a function to a sequence of elements. Here's an example:

```python
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```

## Import and Export Functions

Functions can be imported and exported using the `import` and `export` keywords. Here's an example:

```python
def add(a, b):
    return a + b

# Import the function
from my_module import add

# Export the function
from my_module import add
```




