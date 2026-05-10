# Comprehensions
Comprehension are a concise way to create - 
list 
sets
disctionaries 
or genrators in python using. single lien of code.

# Where they re used in real world: 
 - filter Items
 - transform items
 - create a new collection
 - flatten nested structure

# What Purpose they does?
 - Cleaner Code
 - Faster execution

# Types of Compehensions:
 - List
 - Set
 - Dictionary
 - Generator

# List Comprehensions
 List Comprehension is a way to create a new list with less syntax.
```python
new_list = [expression for item in iterable if condition == True]
```

# Set Comprehensions
Set comprehensions are similar to list comprehensions but create sets instead. They provide a concise way to create sets by iterating over an existing list, tuple, or range, and applying a condition. Here's the basic syntax:
```python
new_set = {expression for item in iterable if condition} 

# For example, to create a set of even numbers from 1 to 10, you can use a set comprehension:
even_numbers = {x for x in range(1, 11) if x % 2 == 0}
```

# Dictionary Comprehensions
Dictionary comprehensions provide a concise way to create dictionaries by iterating over an existing list, tuple, or range, and applying a transformation or condition. Here's the basic syntax:
```python
new_dict = {key: expression for item in iterable if condition == True}


# For example, to create a dictionary where the keys are numbers and the values are their squares, you can use a dictionary comprehension:
squares = {x: x * x for x in range(1, 6)}
```

# Generator Comprehensions
Generator comprehensions provide a concise way to create generators by iterating over an existing list, tuple, or range, and applying a condition. Here's the basic syntax: 
```python
new_generator = (expression for item in iterable if condition == True)
# For example, to create a generator of even numbers from 1 to 10, you can use a generator comprehension:
even_numbers = (x for x in range(1, 11) if x % 2 == 0)  
``` 



