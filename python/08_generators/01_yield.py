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

    