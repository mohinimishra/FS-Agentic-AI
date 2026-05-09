# Tuples - () they are immutable (cannot be changed) and ordered (they have a defined order, and that order will not change)

spices = ("cinnamon", "nutmeg", "clove")
#Extracting values from a tuple into separate variables
(spice1, spice2, spice3) = spices
print(f"Spice 1: {spice1}")
print(f"Spice 2: {spice2}")
print(f"Spice 3: {spice3}")

#Indexing and slicing
# Tuples support indexing and slicing just like lists and strings
print(f"First spice: {spices[0]}") # cinnamon
print(f"Last spice: {spices[-1]}") # clove
print(f"First two spices: {spices[0:2]}") # ('cinnamon', 'nutmeg')

cinnamon_ratio, clove_ration =2, 1
print(f"Cinnamon Ratio: {cinnamon_ratio}")
print(f"Clove Ratio: {clove_ration}")

#Swaping of values
cinnamon_ratio, clove_ration = clove_ration, cinnamon_ratio
print(f"Cinnamon Ratio: {cinnamon_ratio}")
print(f"Clove Ratio: {clove_ration}")

# membership
# in works with tuples to check if an element exists in the tuple
print(f"is masala in spices? {'masala' in spices}") # False
print(f"is cinnamon in spices? {'cinnamon' in spices}") # True

# Tuple is case sensitive
print(f"is Cinnamon in spices? {'Cinnamon' in spices}") # False

add = spices.append("masala") # AttributeError: 'tuple' object has no attribute 'append'