class Vehical:
    def __init__(self, price):
        self._price = price #
        
    @property
    def price(self):
        return self._price + 100
    
    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            raise ValueError("Price can not be less than 1")
        
cal = Vehical(5)
print (cal.price)