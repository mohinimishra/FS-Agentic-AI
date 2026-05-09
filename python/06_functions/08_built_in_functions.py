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

