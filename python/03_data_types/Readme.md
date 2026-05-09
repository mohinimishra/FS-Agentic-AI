# Object

### Everuthing is python is object 
    - identity 
    - type
    - value
### Object mutability
    -mutable = its changing value (on actual memory) but reference is same
    -immutable = when changing refrence not actual meemory.
    - property "identitiy" verify that object is mutable or not 

IS it Mutable or Not ?
```py
varA = 2
print(varA) // 2
print(varA) // 3
varA = 3
```
- Note: Numbers are immutable but here the output is updated value,because its changing refrence not actual memory. 2 is still present it just created another variable with same name and pointing its reference 

# Sets() 
Sets in python is a collection of unique elements. 
It is unordered and mutable.
Sets are defined using curly braces {} or the set() function.
```py
spice_mix = set()
spice_mix.add("salt")
spice_mix.add("pepper")
print(spice_mix)
```

#Dictionaries
A dictionary is a collection of key-value pairs. It is unordered, mutable, and indexed.
Dictionaries are defined using curly braces {} with key-value pairs separated by a colon :

