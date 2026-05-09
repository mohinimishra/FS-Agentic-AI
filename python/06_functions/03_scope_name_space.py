# Scopes and Name Resolution:

    # Local Scope - inside a function
    # Enclosing form outer function if nested
    # Global Scoping - Top level script
    # Build in 

def inside_scope():
    name = "Java" # inside scope
    print(f"Inside function scope : {name}")  
inside_scope()

name = "Python" # global scope
print(f"Outside scope : {name} ")
inside_scope()


# Enclosing

def outer_function():
    flavour = "ginger"
    def inner_function():
        flavour = "mint"
        print(f"Selected flavour : {flavour}") # mint
    inner_function()
    print(f"Selected Flavour : {flavour}") # ginger
    
outer_function()



