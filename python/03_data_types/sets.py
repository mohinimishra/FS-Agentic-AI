# Set in python is a collection of unique elements. 
# It is unordered and mutable. 
# Sets are defined using curly braces {} or the set() function.

# Creating a set
essential_spices = {"cumin", "coriander", "turmeric"}
optional_spices = {"cardamom", "clove", "cinnamon", "turmeric"}

spice = {"pepper"}

# Union of two sets
all_spices = essential_spices | optional_spices # union of two sets
print(f"All spices: {all_spices}") # Output: All spices: {'cumin', 'coriander', 'turmeric', 'cardamom', 'clove', 'cinnamon'}

# Intersection of two sets
comman_spices = essential_spices & optional_spices # intersection of two sets
print(f"Common spices: {comman_spices}") # Output: Common spices: {'turmeric'}  

comman_spices = essential_spices & spice # intersection of two sets
print(f"Common spices with pepper: {comman_spices}") # Output: Common spices with pepper: set()

# Difference of two sets
unique_essential_spices = essential_spices - optional_spices # difference of two sets
print(f"Unique essential spices: {unique_essential_spices}") # Output: Unique essential spices: {'cumin', 'coriander'}

print(f"is cumin in essential spices ? : {'cumin' in essential_spices}") # Output: is cumin in essential spices ? : True

#Frozenset is an immutable version of set. It is defined using the frozenset() function.
frozen_spices = frozenset(essential_spices)
print(f"Frozen spices: {frozen_spices}") # Output: Frozen spices: frozenset({'cumin', 'coriander', 'turmeric'})