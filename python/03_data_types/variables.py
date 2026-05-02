# Immutable 
amount = 10
print(f"Amount: {amount}")
amount = 20
print(f"Amount: {amount}")
# its changing reference not actual memory
print(f"Id of 10:{id(10)}") #4301425232
print(f"Id of 20:{id(20)}") #4301425552

# Mutable (set)
spice_mix = set()
print(f"Spice mix: {spice_mix}")
spice_mix.add("cumin")
print(f"Spice mix: {spice_mix}", id(spice_mix)) # id:4482580032
spice_mix.add("coriander")
# its changing value but reference is same
print(f"Spice mix: {spice_mix}", id(spice_mix)) # id:4482580032