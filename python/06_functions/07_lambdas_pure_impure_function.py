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