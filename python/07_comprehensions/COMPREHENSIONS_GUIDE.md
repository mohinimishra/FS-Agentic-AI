# Comprehensions in Python

## Understanding List Comprehension

### Creating Lists with Filtering

```python
# [expression for item in iterable if condition]

menu = ["Masala Tea", "Ginger Tea", "Iced Lemon Tea", "Iced Peach Tea", "Green Tea"]
comp = [tea for tea in menu if "Iced" in tea]
print(comp) #['Iced Lemon Tea', 'Iced Peach Tea']
```

**Simply Explained:**
List comprehension is a concise way to create a new list by iterating over an existing list and applying a condition. Here's what happens behind the scenes:

1. **Syntax**: `[expression for item in iterable if condition]`
   - `expression`: What to add to the new list (usually the item or a transformation of it)
   - `for item in iterable`: Loop through each item in the list
   - `if condition`: Optional filter to include only items that meet the condition

2. **Execution Flow**:
   - Python loops through each tea in the `menu` list
   - For each tea, it checks if "Iced" is in the tea's name
   - If true, it adds that tea to the new list
   - Result: `['Iced Lemon Tea', 'Iced Peach Tea']`

3. **Comparison to Traditional Loop**:
   - Without comprehension: 
     ```python
     comp = []
     for tea in menu:
         if "Iced" in tea:
             comp.append(tea)
     ```
   - With comprehension: One readable line instead of four

4. **Benefits**:
   - **Cleaner code**: More concise and readable than traditional loops
   - **Faster execution**: List comprehensions are optimized and run faster than loops
   - **Functional style**: More declarative (what you want, not how to get it)

---

## Creating Sets with Comprehension

### Removing Duplicates and Flattening Nested Structures

```python
# {expression f0o item in itterable if condition}

bucket =["Apple", "mango", "banana", "grapes", "mango", "banana"]

uniqueFruits = {ingredients for ingredients in bucket}
print(uniqueFruits)

recepies ={
    "panner":["panner", "onion", "tomato"],
    "dosha":["batter", "ghee"]
    }
getIngredients = {ingredient for recepie in recepies.values() for ingredient in recepie}
print(getIngredients)
```

**Simply Explained:**
Set comprehension creates a set (collection of unique items) using a similar syntax to list comprehension. Here's what happens:

1. **Basic Set Comprehension**:
   - `{ingredients for ingredients in bucket}` iterates through the bucket list
   - Sets automatically remove duplicates
   - Input: `["Apple", "mango", "banana", "grapes", "mango", "banana"]`
   - Output: `{"Apple", "mango", "banana", "grapes"}` (unique items only)

2. **Nested Iteration (Flattening)**:
   - `{ingredient for recepie in recepies.values() for ingredient in recepie}`
   - This syntax has TWO `for` clauses (nested loops)
   - First `for`: Iterate through recipe values (lists)
   - Second `for`: For each list, iterate through individual ingredients
   - Flattens the nested structure: `[["panner", "onion", "tomato"], ["batter", "ghee"]]` becomes `{"panner", "onion", "tomato", "batter", "ghee"}`

3. **Syntax**: `{expression for item in iterable if condition}`
   - Curly braces `{}` create a set (not a dictionary)
   - Otherwise similar to list comprehension

4. **When to Use Sets**:
   - When you need unique items
   - When you don't care about order
   - For faster membership testing (`if x in set` is faster than `if x in list`)

---

## Creating Dictionaries with Comprehension

### Transforming Key-Value Pairs

```python
# {key:value for key,value in iterables.items()}

menu_in_inr = {
    "tea": 20,
    "cold drink":40
    }
menu_in_usd = {item:price/90 for item,price in menu_in_inr.items()}
print(menu_in_usd) #{'tea': 0.2222222222222222, 'cold drink': 0.4444444444444444}
```

**Simply Explained:**
Dictionary comprehension creates a new dictionary by transforming an existing dictionary or iterable. Here's what happens:

1. **Syntax**: `{key:value for key,value in iterables.items()}`
   - `key:value`: What the new key and value should be
   - `for key,value in iterables.items()`: Iterate through the original dictionary's items
   - `.items()` gives you key-value pairs to unpack

2. **Execution Flow**:
   - `menu_in_inr.items()` returns pairs: `("tea", 20)`, `("cold drink", 40)`
   - Each pair is unpacked into `item` and `price`
   - The new dictionary keeps the same keys but transforms the values: `price/90`
   - Result: Currency conversion from INR to USD

3. **Other Use Cases**:
   - **Swapping keys and values**: `{v:k for k,v in original.items()}`
   - **Filtering**: `{k:v for k,v in dict.items() if v > 30}`
   - **Transforming keys**: `{k.upper():v for k,v in dict.items()}`

4. **Benefits**:
   - Transform dictionary values or keys consistently
   - Create derived dictionaries without modifying the original
   - More readable than loop-based approaches

---

## Using Generator Comprehension

### Memory-Efficient Lazy Evaluation

```python
# (expression for item in iterable if condition)

menu = [100,200, 200, 100,400, 500 ]
# comp = (item for item in menu if item>200)
# print(comp)
 # ➜  07_comprehensions git:(master) ✗ python3 04_generator_comprehension.py <generator object <genexpr> at 0x101b83660>
# as this is kind of streaming insted of adding whole data to mer

comp = sum (item for item in menu if item>200)
print(comp)
```

**Simply Explained:**
Generator comprehension uses parentheses instead of square brackets and creates a generator (not a list). Here's what happens:

1. **Syntax**: `(expression for item in iterable if condition)`
   - Looks like list comprehension but uses `()` instead of `[]`
   - Creates a generator object, not a concrete list

2. **Why Use Parentheses**:
   - If you print `(item for item in menu if item>200)` directly, you get: `<generator object <genexpr> at 0x101b83660>`
   - This is a generator object that produces values on-demand, not a list of values
   - It doesn't store all items in memory at once (unlike list comprehension)

3. **Memory Efficiency**:
   - **List comprehension**: Creates entire list in memory: `[300, 400, 500]`
   - **Generator comprehension**: Produces values one at a time as needed
   - For large datasets, generators use far less memory

4. **How It Works with Functions**:
   - `sum(item for item in menu if item>200)` works perfectly with generator comprehension
   - `sum()` iterates through the generator, asking for one value at a time
   - As it gets each value, it adds it: 300 + 400 + 500 = 1200
   - Memory efficient because not all items exist simultaneously

5. **When to Use**:
   - Processing large files or datasets
   - Chaining multiple operations without storing intermediate results
   - When you only need to iterate once (generators can't be reused)
   - Performance is critical and memory is limited

6. **Trade-offs**:
   - **Pros**: Memory efficient, lazy evaluation, can be infinite
   - **Cons**: Can only iterate once, slightly slower than lists for small datasets, less flexible
