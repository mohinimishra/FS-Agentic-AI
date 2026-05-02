# Numbers in Python
    # Immutable data type
    # int, float, complex
# addition
num1 = 10
num2 = 20
result = num1 + num2
print(f"Addition: {result}", id(result))  

#subtraction
result = num1 - num2
print(f"Subtraction: {result}", id(result))

#multiplication
result = num1 * num2
print(f"Multiplication: {result}", id(result)) 

#division
result = num1 /num2
print(f"Division: {result}", id(result))  # 0.5

# floor division
result = num1 // num2
print(f"Floor Division: {result}", id(result)) # 0

# modulus (remainder)
result = num1 % num2
print(f"Modulus: {result}", id(result)) # 10

# exponentiation
result= num1 ** num2
print(f"Exponentiation: {result}", id(result)) # 10 to the power of 20

#another way of assinging number
var = 1_000_000
print(f"Var: {var}", id(var)) # 1000000

# Real number
import sys
ideal_temp = 95
current_temp = 95.68990000404089998
print(ideal_temp)
print(current_temp)
print(type(ideal_temp))# <class 'int'>
print(type(current_temp)) # <class 'float'>

print(sys.float_info) 
