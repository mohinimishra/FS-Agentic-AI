# Dictionary in python
# A dictionary is a collection of key-value pairs. It is unordered, mutable, and indexed.
# Dictionaries are defined using curly braces {} with key-value pairs separated by a colon :

person_details = dict(type="person", name="John", age=30, city="New York")
print(person_details)

# another way of creating a dictionary
another = {}
another["type"] = "person"
another["name"] = "Francis"
another["age"] = 25
another["city"] = "Los Angeles"
print(another)

#removing an element from the dictionary
del person_details["age"]
print(person_details)

#membership test

#check if a key is in the dictionary
print(f"Order details (keys): {person_details.keys()}") # Output: dict_keys(['type', 'name', 'city'])
print(f"Order details (values): {person_details.values()}") # Output: dict_values(['person', 'John', 'New York'])
print(f"Order details (items): {person_details.items()}") # Output: dict_items([('type', 'person'), ('name', 'John'), ('city', 'New York')])

last_item = person_details.popitem() #remove and return the last key-value pair from the dictionary
print(f"Last item removed: {last_item}") # Output: Last item removed: ('city', 'New York')

last = person_details.pop("type") #remove and return the value of the specified key from the dictionary. If the key is not found, it raises a KeyError.
print(f"Last item removed: {last}") # Output: Last item removed: person

#update
person_details.update({"age": 40, "city": "Newzeland"})
print(f"person_details: {person_details}") # Output: {'name': 'John', 'age': 40, 'city': 'Newzeland'}    

# safe way to get value from the dictionary
# instaed of giving error get method will return default value if key is not found in the dictionary
age = person_details.get("age", "Age not found")
print(f"Age: {age}") # Output: Age: 40