class Orders:
    
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
        
    @classmethod
    def disctionaryData(cls, oreder_disc):
        return cls(
                name = oreder_disc["name"],
                brand = oreder_disc["brand"]
            )
    @classmethod
    def stringData(cls, string):
        name, brand = string.split(',')
        return cls(name,brand)
    

order1= Orders.disctionaryData({"name":"coffee", "brand":"nescafe"})
print(order1.__dict__) # {'name': 'coffee', 'brand': 'nescafe'}
print(order1.name)

order2= Orders.stringData("tea, taj")
print(order2.__dict__) # {'name': 'coffee', 'brand': 'nescafe'}
print(order2.name) #{'name': 'tea', 'brand': ' taj'}
        
