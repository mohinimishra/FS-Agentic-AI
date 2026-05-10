# Generators 
-What are generators
_ Not for everything
- memory efficient
- yield keyword

- you save memory by using yield keyword
- lazy evaluation

# Generators

Generators are a powerful feature in Python that allow you to create iterable objects that can be used in loops. They provide a way to generate a sequence of values on-the-fly, saving memory and allowing for efficient processing of large datasets.

## What are generators?

Generators are defined using the `yield` keyword instead of the `return` keyword. When a generator is called, it returns an iterator object that can be used in loops. Each time the iterator is iterated over, the generator resumes execution from where it left off, generating the next value in the sequence.

Here's an example of a simple generator that generates the Fibonacci sequence:

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Usage
fib = fibonacci()
print(next(fib))  # Output: 0
print(next(fib))  # Output: 1
print(next(fib))  # Output: 1
print(next(fib))  # Output: 2
```

## Memory Efficiency
Generators are memory efficient because they generate values on-the-fly. They don't store the entire sequence in memory like a list or tuple would. This makes them particularly useful when dealing with large datasets that don't fit into memory.

For example, consider generating the Fibonacci sequence up to a certain number. Using a generator, you can generate the sequence as needed, saving memory:

def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

# Usage
fib = fibonacci(100)
print(list(fib))  # Output: [0, 1, 1, 2, 3, 5, 8]
``` 
# Lazy Evaluation
Generators provide lazy evaluation, meaning that values are generated only when needed. This can be useful when you want to process a large dataset incrementally, without loading the entire dataset into memory.

For example, consider reading a large file line by line using a generator:

```python
def read_lines(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Usage
lines = read_lines('large_file.txt')
for line in lines:
    print(line)
```
 By using a generator, you can process the file line by line, saving memory and improving performance.

By studying the files in this folder, you can gain a deeper understanding of how to use generators effectively in your code. Feel free to explore each file and experiment with the code to reinforce your understanding of these concepts.

## Infinite Generators
Generators can be infinite, meaning they can generate an infinite sequence of values. This can be useful when you need to generate a large number of values or when you want to create an infinite loop.

Here's an example of an infinite generator that generates even numbers:

```python
def even_numbers():
    i = 0
    while True:
        yield i
        i += 2
# Usage
evens = even_numbers()
print(next(evens))  # Output: 0
print(next(evens))  # Output: 2
print(next(evens))  # Output: 4
```

## Closing Generators
Generators can be closed using the close() method. This is useful when you want to stop the generator prematurely.

Here's an example of a generator that can be closed:

```python
def countdown():
    count = 10
    while count > 0:
        print(count)
        count = yield
    print("Done!")
# Usage
countdown_gen = countdown()
next(countdown_gen)  # Start the generator
countdown_gen.send(None)  # Send a value to the generator
countdown_gen.close()  # Close the generator
```
# The next() Function
The next() function can be used to retrieve the next value from a generator. It takes the generator object as an argument and returns the next value.


Here's an example of using next() with a generator:
```python
def countdown():
    count = 10
    while count > 0:
        print(count)
        count = yield
    print("Done!")

# Usage
countdown_gen = countdown()
next(countdown_gen)  # Start the generator
print(next(countdown_gen))  # Output: 10
```