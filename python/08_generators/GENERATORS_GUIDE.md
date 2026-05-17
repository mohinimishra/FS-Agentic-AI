# Generators in Python

## Understanding Yield and Basic Generators

### Creating Simple Generators with Yield

```python
# how to define
def serve_tea():
    yield "Cup 1: Masala Tea"
    yield "Cup 2: Ginger Tea"
    yield "Cup 2: Elaichi Tea"

stall= serve_tea()  
# to call, get the value from stall we need to alway use Next(next())method
print(stall) #<generator object serve_tea at 0x1043126d0>
print(next(stall)) # First yield-> Cup 1: Masala Tea
print(next(stall)) # Second yield-> Cup 2: Ginger Tea
print(next(stall)) # Third yield-> Cup 3: Elaichi Tea
print(next(stall)) # Traceback (most recent call last): 
                    # File "/Users/mm/github/FS-Agentic-AI/python/08_generators/01_basics.py", line 12, in <module>
                   
                    # StopIteration



for tea in stall:
    print(f"tea:{tea}")
```

**Simply Explained:**
A generator is a function that uses `yield` instead of `return` to produce a sequence of values. Here's what happens behind the scenes:
1. When you call `serve_tea()`, it doesn't execute the function; it returns a generator object
2. Each time you call `next()` on the generator, it runs until it hits a `yield` statement
3. The value after `yield` is returned to you
4. The next `next()` call resumes from right after that `yield`, continuing until the next `yield`
5. When all `yield` statements are exhausted, calling `next()` raises `StopIteration`
6. You can also iterate over generators using a `for` loop, which automatically handles `next()` calls and `StopIteration`
7. Generators save memory because they don't store all values at once—they produce them on-the-fly

---

## Creating Infinite Generators

### Building Generators That Run Forever

```python
def sereve_infinite():
    count =1
    while True:
        yield f"Count: {count}"
        count += 1
    
serve = sereve_infinite()
serve2 = sereve_infinite()

for _ in range(5):
    print(next(serve))
    
for _ in range(2):
    print(next(serve2))
```

**Simply Explained:**
Infinite generators use a `while True` loop to produce an endless sequence of values. Key concepts:
- Each time you call `next()`, the generator increments the counter and yields the next value
- The generator never runs out of values (unlike finite generators that raise `StopIteration`)
- You control when to stop by limiting how many times you call `next()` (like with `range(5)`)
- Each generator instance maintains its own state—`serve` and `serve2` have separate counters
- Infinite generators are useful for creating counters, IDs, or endless sequences of data

---

## Passing Values to Generators

### Sending Data into Generators

```python
def take_order():
    print(f"Welcome, what would you like to order?")
    order = yield # Program stops on first run as it waits for value to be sent 
    while True:
        print(f"Order is Preparing: {order}")
        order = yield # Stooping the loop wiats for value, once recived go through the loop 
 
order = take_order()
# print(next(order))
next(order) # to start the generator
order.send("Burger") # send value to generator
order.send("Dosa") # send value to generator
```

**Simply Explained:**
Generators can receive values using the `.send()` method, creating two-way communication. Here's the flow:
1. `next(order)` starts the generator and runs until the first `yield`, printing "Welcome..."
2. The program pauses at `order = yield` waiting for a value
3. `order.send("Burger")` resumes the generator and assigns "Burger" to the `order` variable
4. The generator prints "Order is Preparing: Burger" and pauses at the next `yield`
5. `order.send("Dosa")` repeats the process with a new order
6. This pattern creates a generator that can receive input dynamically, useful for interactive or event-driven code

---

## Delegating to Other Generators

### Using yield from and Closing Generators

```python
# from - used to get the yield values from functions
def local_tea() :
    yield "Masala Tea",
    yield "Ginger Tea"
    
def imported_tea():
    yield "Matcha"
    
def all_tea():
    yield from local_tea() 
    yield from imported_tea()
    
for tea in all_tea():
    print(tea)
    
# try, except block 

def stall():
    try:
        while True:
            order = yield
            print(f"Hey Stall is preparing your order {order}")
    except:
        print("Stall closed")

status = stall()
print(next(status))
status.send("Ginger")
status.close()
```

**Simply Explained:**
This demonstrates two advanced generator concepts:

**`yield from` delegation:**
- `yield from local_tea()` delegates to another generator and yields all its values
- Instead of manually yielding each value from `local_tea()`, `yield from` automates this
- `all_tea()` acts as a pipeline that combines values from multiple generators
- This reduces boilerplate and makes code more readable when chaining generators

**Closing generators:**
- When you call `.close()` on a generator, it stops execution and raises `GeneratorExit` at the current `yield`
- The `try-except` block catches this exception and performs cleanup (printing "Stall closed")
- This pattern is useful for resource management—ensuring cleanup code runs when a generator is no longer needed
- Without `.close()`, the generator would continue indefinitely; with it, you explicitly terminate it
