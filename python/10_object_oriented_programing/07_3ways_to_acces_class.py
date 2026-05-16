class ClothingStore:
    def __init__(self, size, brand):
        self.size = size
        self.brand = brand

# basic usecas => not recommended    
class Top(ClothingStore):
    def __init__(self, size, brand):
        self.size= size
        self.brand = brand
        self.name = "Crop Top"
        self.price = 1500
        
# Explicit Call => callsing base class
class Jeans(ClothingStore):
    def __init__(self, size, brand):
        ClothingStore.__init__(self, size, brand)
        self.name = "Denim Jeans"
        self.price = 3000
        
# Implict Call
class Jeans(ClothingStore):
    def __init__(self, size, brand):
        super().__init__(self, size, brand)
        self.name = "Denim Jeans"
        self.price = 3000
        
   
