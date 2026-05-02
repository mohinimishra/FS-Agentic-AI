# List is Mutable (array)
ingredients = ["flour", "sugar", "salt", "milk"]
#extracting an element from the list
print(ingredients[0])  # Output: flour
print(ingredients[1])  # Output: sugar

#Adding an element to the list
ingredients.append("cocoa powder")
print(ingredients)

#Removing an element from the list
ingredients.remove("salt")
print(ingredients)

sweets = ["chocolate", "candy", "ice cream"]
snacks = ["chips", "popcorn", "pretzels"]
#Extending two lists
snacks.extend(sweets)
print(snacks)  # Output: ['chips', 'popcorn', 'pretzels', 'chocolate', 'candy', 'ice cream']

snacks.insert(2,"cookies")
print(snacks)  # Output: ['chips', 'popcorn', 'cookies', '

#remove last element from the list
snacks.pop()
print(snacks)  # Output: ['chips', 'popcorn', 'cookies', '

#reverse the list
snacks.reverse()
print(snacks)  # Output: ['ice cream', 'candy', 'chocolate', 'cookies', 'popcorn', 'chips']

#short the list
snacks.sort()
print(snacks)  # Output: ['candy', 'chips', 'chocolate', 'cookies', 'ice cream', 'popcorn']

#get the max and min element from the list
numbers = [5, 2, 9, 1, 5, 6]
print(max(numbers))  # Output: 9
print(min(numbers))  # Output: 1

#operator overlaoding
#adding element
array1= [1, 2, 3]   
array2= [4, 5, 6]
result = array1 + array2
print(result)  # Output: [1, 2, 3, 4, 5, 6]

print(f"result: {result *3}")  # Output: result: [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]

bytes = bytearray("Hello, World!", "utf-8")
print(f"{bytes}")  # Output: bytearray(b'Hello, World!')

replaced_bytes = bytes.replace(b"World", b"Python")
print(f"{replaced_bytes}")  # Output: bytearray(b'Hello, Python!')  