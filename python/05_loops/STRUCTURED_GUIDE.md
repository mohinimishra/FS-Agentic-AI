# Python Loops - Comprehensive Learning Guide

---

## 01. For Loops with range()

### Generating Sequences with range()

```python
# A stall owner has digital token displa.
# For every customer in line, a token number is printedand order serverd.
# Tasks:
    # Use a 'for' loop to genarate token mumbers from 1 to 10 using range()
    # Print: "Serving Order To "token_number"

for token in range(1, 11):
    print(f"Serving Order To {token}")
```

**Simply Explained:**

A **for loop** repeats code for each item in a sequence. `range(1, 11)` generates numbers from 1 to 10 (the end is exclusive—11 is not included). Each iteration, `token` takes the next value, and the indented code executes. So this loop prints "Serving Order To 1", then 2, then 3, ... up to 10. `range(start, stop, step)` is flexible: `range(1, 11)` implies step=1, `range(0, 10, 2)` gives 0, 2, 4, 6, 8 (even numbers). For loops are ideal when you know how many times to repeat or need a specific sequence.

**Senior Tip:** Remember that `range(n)` ends before `n`. Use `range(1, 11)` to include 10, not `range(1, 10)`. For reverse order, use negative step: `range(10, 0, -1)` counts down from 10 to 1. Avoid off-by-one errors—test with print statements or a debugger if unsure.

---

### Iterating a Fixed Number of Times

```python
# A shop makes bread in batches every 15 min.
# You want to simulate 4 batches.
# Task:
    # use range() for simulate batch numbers
    # print: "Preparing order for batch numner : "batch_number"

for batch in range (1, 5):
    print(f"preparing order for batch number", {batch})
```

**Simply Explained:**

This loop uses `range(1, 5)` to generate 1, 2, 3, 4—four iterations representing four batches. Each iteration, `batch` holds the current batch number, and the print statement outputs it. This demonstrates that for loops are useful for repeating an action a fixed number of times without needing to write the code multiple times. The loop counter (`batch` here) can be incorporated into the logic or output.

**Senior Tip:** When you need a simple counter without using the value itself, use `range(4)` (or `range(n)`) instead of `range(1, 5)`. Use the counter when its value matters; otherwise, consider `for _ in range(n):` with an underscore to signal "I don't use this variable."

---

## 02. For Loops with Lists (Iteration)

### Looping Through List Elements

```python
# You receive list of names of oreders
# The goal is ot print out the oreder queue.
# Taks:
    # Use a list of name
    # print: order ready for [name]

names = ["Anna", "Alice", "Nataliya"]

for name in names :
    print (f"Order Ready for {name}")
```

**Simply Explained:**

For loops naturally iterate through lists. `for name in names:` means "for each item in the `names` list, assign it to the variable `name` and execute the loop body." Python handles the iteration automatically—you don't manage indices manually. Each iteration, `name` becomes the next element: "Anna", then "Alice", then "Nataliya". This is cleaner than index-based loops and less error-prone (no off-by-one errors). Use this pattern whenever you have a collection and want to process each element.

**Senior Tip:** This is the **Pythonic way**. Avoid:
```python
for i in range(len(names)):
    print(f"Order Ready for {names[i]}")
```
Unless you specifically need the index, iterate directly over elements. If you do need both index and value, use `enumerate()` (shown next).

---

## 03. Enumerate: Index and Value Together

### Getting Both Index and Value During Iteration

```python
# You are creating a menu board
# Each item must be numberd
# Task
# Use enumerate() to print menu items with nubers

menu = ["Green", "Lemon", "Spiced", "Mint"]

# enumerate returns a tuple conating count 

for idx, items in enumerate(menu, start=2): 
    print (f"{idx} : {items} chai") 

#output
    """
    2 : Green chai
    3 : Lemon chai
    4 : Spiced chai
    5 : Mint chai
    """
```

**Simply Explained:**

`enumerate()` provides both the **index** and the **value** for each element. It returns tuples: `(index, value)`. The for loop unpacks each tuple into `idx` and `items`. By default, `enumerate()` starts counting at 0, but `start=2` shifts it to begin at 2. This is useful for display purposes (e.g., menu numbering starting at 1 or 2 instead of 0) or when you need to know both the position and the item. Without enumerate, you'd use an index-based loop or manually track a counter.

**Senior Tip:** Use `enumerate()` when you need the index. It's cleaner than `range(len(...))` and safer. The index starts at 0 by default; adjust with `start=` if you want 1-based numbering. Enumerate is ideal for numbered lists, progress tracking, or when you need to skip/modify at specific positions.

---

## 04. Zip: Pairing Elements from Multiple Lists

### Iterating Over Multiple Lists Simultaneously

```python
# You are preparing an order summary with customer name and total bill.
# Taks:
    # Use two lists: one for name another for bills
    # Print:[name] paid [bill]

names = ["Alice", "Alex", "Crystan", "Sam"]
bills = [50, 10, 100, 500]

for name, bill  in zip(names, bills):
    print(f"{name} paid {bill}rs.")
```

**Simply Explained:**

`zip()` combines elements from multiple sequences. `zip(names, bills)` pairs the first name with the first bill, the second name with the second bill, and so on. It returns tuples: `("Alice", 50)`, `("Alex", 10)`, etc. The for loop unpacks each tuple into `name` and `bill`. This is perfect for parallel data—instead of using indices to manually pair elements, `zip()` does it automatically. If lists are different lengths, `zip()` stops at the shortest list (no error about mismatched lengths).

**Senior Tip:** `zip()` is powerful for parallel iteration. It naturally communicates intent: "these sequences are related and should be processed together." Use it instead of index-based loops with multiple lists. For unequal-length sequences where you want to process all elements, use `itertools.zip_longest()` with a fill value.

---

## 05. While Loops: Condition-Based Repetition

### Looping While a Condition is True

```python
# You want to simulate coffe hearing
# It starts at 40C and stops at 100C
# Task
# use a while loop
# increase temp by 15 until it reaches or exceed 100
# print each temp step

temp=34;

while temp < 100:
    print(f"Temprature {temp}")
    temp += 15
    print(f"Temprature {temp}")
    
print(f"Coffee is ready")
```

**Simply Explained:**

A **while loop** repeats code **while a condition is true**. Unlike for loops (which iterate a fixed number of times), while loops continue indefinitely until the condition becomes false. Here, `while temp < 100:` means "keep running as long as temp is less than 100." Inside the loop, `temp += 15` increases the temperature. Each iteration prints the temperature. When `temp >= 100`, the condition is false, and the loop exits. This is useful when you don't know in advance how many iterations you need—only that some condition must be satisfied.

**Senior Tip:** Be careful with while loops—**infinite loops** are a common bug. Always ensure the loop variable is modified so the condition eventually becomes false. Use a counter or exit condition. If debugging a while loop, add a maximum iteration limit or print statements to trace execution. For well-defined counts, prefer for loops; use while when the termination condition is complex or data-driven.

---

## 06. Break and Continue: Loop Control

### Exiting Loops Early and Skipping Iterations

```python
# Some ingredients are out of Stock
# You want to skip those and stop entierly if someone requests a restricted ingredient
# Task:
    # Skip if ingredeiant is "out of stock" 
    # Break if flavour is "Discountinued"

flavours = ["ginger", "out of stock", "discontinued",  "mint" ]

for flavour in flavours :
    if flavour == "out of stock":
        continue
    elif flavour == "discontinued":
        print(f"Discounted Item found")
        break
    
    print(f"Item found : {flavour}")

print(f"out of the loop")
```

**Simply Explained:**

**`continue`** skips the current iteration and jumps to the next one. When `flavour == "out of stock"`, the loop skips the `print(f"Item found...")` and moves to the next flavour. **`break`** exits the loop entirely. When `flavour == "discontinued"`, the loop prints "Discounted Item found", then breaks—no more iterations happen, and execution jumps to the code after the loop ("out of the loop"). These are useful for filtering (skip unwanted items) or stopping early (emergency exit).

**Senior Tip:** Use `break` and `continue` sparingly—they can make loop logic harder to follow. Often, you can refactor using conditionals or filter functions (`filter()`) to be clearer. However, sometimes they're the most readable solution, especially for guarding against invalid states or early termination.

---

### Using Else with Loops (Loop Fallback)

```python
employeDetails = [("Alice", 18), ("Brandee", 20), ("Charlee", 13)]

for name, age in employeDetails:
    if age <= 18:
        print(f"{name} is eligble fo this Job")
        break
        
else:
    print(f"No one is elible for this Job")
```

**Simply Explained:**

Python has a unique feature: **loop-else**. The `else` block runs **only if the loop completes normally** (without breaking). Here, if any employee is `<= 18`, they're eligible and the loop breaks. If we break, the `else` is skipped—we found someone eligible. But if all employees are > 18, the loop finishes without breaking, and the `else` runs: "No one is eligible for this Job." This elegantly handles the "nothing found" case without extra flags.

**Senior Tip:** Loop-else is a gem in Python but often overlooked. Use it for "search and not found" patterns—when you want to execute fallback code only if no `break` occurred. It's cleaner than maintaining a `found` flag.

---

## 07. Walrus Operator (:=) in Loops

### Assigning and Checking in One Expression

```python
value=13
remainder = value % 5

if(remainder):
    print(f"Remainder is {remainder}")

# Using Walrus Operator (:=)

if(remainder := value % 5):
     print(f"Remainder is {remainder}")
     
sizes = ["small", "medium", "large"]
if (req_size := input("Please enter your size")) in sizes:
     print(f"Order size is {req_size}")    
else:
     print(f"Not found the {req_size} size")

flavours = ["ginger", "mint", "green"]

while (flavour := input("Enter your flavour")) not in flavours:
     print(f"Flavour {flavour} is not Available")
     
print(f"Flavour {flavour} is available")
```

**Simply Explained:**

The **walrus operator** (`:=`) assigns a value **and** returns it in one expression—it's an assignment expression. Traditional code requires two lines: assign, then use. The walrus operator combines them. `if (remainder := value % 5):` assigns `value % 5` to `remainder` and immediately checks if it's truthy. Similarly, `if (req_size := input(...)) in sizes:` gets user input, assigns it to `req_size`, and checks if it's in sizes—all in one line.

This is especially useful in while loops where you need to prompt repeatedly until a condition is met. Without the walrus operator, you'd need to duplicate the input line: once before the loop and once inside it.

**Senior Tip:** The walrus operator improves readability when used judiciously—it eliminates redundant code. However, overusing it can make code cryptic. Use it for "initialize and check" patterns, especially in loops. In complex expressions, break it into separate lines for clarity—readability trumps conciseness.

---

## 08. Dictionaries: Replacing Repeated Conditionals

### Using Dictionaries to Replace Many If-Elif Branches

```python
# Using Dictionaries Insted of Repaetd Cases:
users =[{"id":1, "total":100, "cupon":"p10"},{"id":2, "total":102, "cupon":"p20"},{"id":3, "total":101, "cupon":"p30"}]
discounts={
    "p10": (0.2, 0),
    "p20": (0.5, 4),
    "p30": (0.8, 7),
    }

for user in users:
    percent, fixed = discounts.get(user["cupon"], (0,0)) # 2nd argument if no value found then returns (0,0)
    discount = user["total"] * percent +fixed
    print(f"{user['id']} paid {user['total']} and got discount for next visit of rs {discount}")
```

**Simply Explained:**

Instead of multiple if-elif blocks checking `if cupon == "p10"` ... `elif cupon == "p20"` ... you can use a **dictionary for lookup**. The `discounts` dictionary maps coupon codes to tuples of `(percent, fixed)` values. `discounts.get(user["cupon"], (0,0))` looks up the coupon; if found, it returns the tuple; if not found, it returns the default `(0,0)`. This scales much better—adding a new coupon requires one dictionary entry, not a new elif branch. It's also faster for many cases (O(1) lookup vs. O(n) for many elifs).

**Senior Tip:** This is a powerful **dispatch pattern**. When you have many conditionals checking a single value against many options, reach for a dictionary or switch structure (match-case). It's more maintainable, scalable, and often faster. This pattern is used extensively in production code for configuration, state machines, and event handlers.

---

## Key Takeaways for Loops

1. **For loops for known iterations**: Use `range()`, lists, or iterables when you know or can determine the count.
2. **While loops for condition-based repetition**: Use when termination depends on a condition, not a count.
3. **Enumerate for index + value**: Use when you need both position and element.
4. **Zip for parallel iteration**: Use when processing related sequences together.
5. **Break to exit early**: Use for search or emergency conditions.
6. **Continue to skip iteration**: Use to filter unwanted elements.
7. **Loop-else for "not found" handling**: Use when you need fallback logic if no break occurred.
8. **Walrus operator for initialization + check**: Use in while loops to eliminate redundant code.
9. **Dictionary dispatch replaces many elifs**: Use for multi-way branching based on a key.
10. **Avoid infinite loops**: Always ensure while loops have a termination condition and update the exit variable.
11. **Prefer direct iteration**: Use `for item in list`, not `for i in range(len(list))`.
12. **Test edge cases**: Empty sequences, single elements, and boundary conditions often reveal bugs.

