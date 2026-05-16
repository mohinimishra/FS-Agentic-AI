
class BaseClass:
    def __init__(self, color, size):
        self.color = color
        self.size = size
    
    

# to inherit the property of BaseClass
class InheritClass(BaseClass):
    def __init__(self, amount):
        self.amount= self.amount
    
class TwoWheeler:
    #Composition : Inherit all the propertyHolding a class in variable
    vehical_property = BaseClass
    
    def __init__(self):
        self.fromBase = self.vehical_property("Gray", "Medium")  # creating object and passing refrence to variable 
        print(self.fromBase.color)
        print(self.fromBase.size)
    



scooty = TwoWheeler()

class fourWheel(TwoWheeler):
    fromBase2 = BaseClass


newCar = fourWheel()

print(newCar.fromBase.color)
print(newCar.fromBase2.color)