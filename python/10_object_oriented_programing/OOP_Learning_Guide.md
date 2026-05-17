# Object-Oriented Programming in Python - Learning Guide

## 1. Class and Objects

### Defining a Class and Creating Objects

```python
#define
class Car:
    pass

print(type(Car)) # <class 'type'> Internaly its object 

car = Car() # creating an object
print(type(car))
```

### Simply Explained

In Python, a **class** is like a blueprint or template used to create objects. When you define `class Car:`, you're creating a class. The `print(type(Car))` shows that the class itself is an object of type `'type'`.

When you create `car = Car()`, you're creating an instance (or object) of that class. This is like building a house from the blueprint. The class is the blueprint, and the car is the actual house. Both the class and the object are internally Python objects.

---

## 2. Namespace and Class Properties

### Adding Class Properties and Creating Instances

```python
class Car:
    origin="India"
    
print(Car.origin)

Car.color = "red" # adding property

print(Car.color)

# create object
carDetails = Car()
print(f"Origin {carDetails.origin} Color: {carDetails.color}")
```

### Simply Explained

A **namespace** is like a container that holds variables and properties. When you define `origin="India"` inside the class, it becomes a class property that belongs to the entire class, not to any single object.

You can access class properties directly using the class name: `Car.origin`. You can also add new properties on-the-fly: `Car.color = "red"`.

When you create an object (`carDetails = Car()`), that object can also access all class properties. So `carDetails.origin` and `carDetails.color` both work because the object inherits the class properties.

---

## 3. Attribute Shadowing

### Adding, Modifying, and Deleting Object Attributes

```python
class Vehical:
    name = "Royal Enfiled"
    wheel= 2
    color="black"
    
vehical_details = Vehical()
print(f"Vehical Details {vehical_details.color}")

vehical_details.power = "350 CC"
print(f"Vehical Details After Adding new atribute {vehical_details.power}")

del vehical_details.power
# print(f"After Remove power attribute", vehical_details.power) # give error as its been deleted


vehical_details.color = "Gray"
# print(f"Vehical Details After Updating an atribute {vehical_details.color}")

del vehical_details.color
print(f"delting class property ", vehical_details.color) # it give class atribute value not dlete it Shadowing
```

### Simply Explained

**Attribute shadowing** happens when an object's own property hides (or shadows) the class property with the same name.

- When you add `vehical_details.power = "350 CC"`, you're adding a new property to just that object instance.
- When you delete it with `del vehical_details.power`, the property is removed from that object.
- When you change `vehical_details.color = "Gray"`, the object creates its own `color` property, shadowing the class's `color` property.
- When you delete `vehical_details.color`, it removes the object's shadowing property, but the class still has its original `color="black"`. So accessing `vehical_details.color` now returns the class property's value.

---

## 4. The `self` Argument

### Understanding `self` in Methods

```python
class Vehical:
    color="gray"
    power="450cc"
    
    def showDetail(self):
        return(f"The color of the bike is {self.color} and power is {self.power}")

veical_detail = Vehical()
print({veical_detail.showDetail()}) 

print(Vehical.showDetail(veical_detail))
```

### Simply Explained

**`self`** is a special parameter that represents the object itself. When you define a method (a function inside a class), the first parameter should always be `self`.

When you call `veical_detail.showDetail()`, Python automatically passes the object (`veical_detail`) as the `self` argument. Inside the method, `self.color` refers to that specific object's color property.

Alternatively, you can call the method directly on the class and pass the object manually: `Vehical.showDetail(veical_detail)`. Both approaches do the same thing, but the first one is more common and convenient.

---

## 5. The `__init__` Constructor

### Initializing Objects with Constructor

```python
class Vehical:
    def __init__(self, name_, color):
        self.name = name_
        self.color = color
        
vehicalDetai = Vehical('Royal Enfield', "Black")

print(vehicalDetai.name)
print(vehicalDetai.color)
```

### Simply Explained

The **`__init__` method** is a special constructor that runs automatically whenever you create a new object. It's used to initialize (set up) the object's properties.

When you write `Vehical('Royal Enfield', "Black")`, Python automatically calls `__init__` with those arguments. The constructor sets `self.name` and `self.color` to the values you provided.

This is much better than manually setting properties after creating an object because you can ensure every object is properly initialized from the start.

---

## 6. Inheritance and Composition

### Using Inheritance and Composition

```python

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
```

### Simply Explained

There are two main ways to reuse code in OOP:

1. **Inheritance**: When a class inherits from another class using `class InheritClass(BaseClass):`, it automatically gets all the properties and methods of the parent class. The child class can add its own properties too.

2. **Composition**: Instead of inheriting, you can hold another class as a property. In `TwoWheeler`, the `vehical_property = BaseClass` stores a reference to the `BaseClass`. Then in `__init__`, you create an object of that class and store it: `self.fromBase = self.vehical_property(...)`.

Both approaches allow code reuse, but composition is sometimes more flexible because an object can have multiple other objects, whereas inheritance creates a fixed hierarchy.

---

## 7. Three Ways to Access Parent Class Properties

### Super() and Inheritance Methods

```python
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
```

### Simply Explained

When a child class inherits from a parent class, there are three ways to use the parent's properties:

1. **Basic Case (Not Recommended)**: Repeat the parent's code in the child class. This causes code duplication and is hard to maintain.

2. **Explicit Call**: Call the parent class's method directly: `ClothingStore.__init__(self, size, brand)`. This works but is less elegant.

3. **Implicit Call (Recommended)**: Use `super().__init__(size, brand)`. This automatically calls the parent class's method. It's cleaner and more maintainable because if the parent class changes, this automatically adapts.

The `super()` method is the modern Python way and is recommended for inheritance.

---

## 8. Method Resolution Order (MRO)

### Understanding Inheritance Hierarchy

```python
# MRO

class A:
    label = f"A: Label A"
    
class B(A):
    label = f"B: Label B"
    
class C(A):
    label = f"C: Label C"
    
class D(B,C):
    pass

testingB= B()
print(testingB.label) #B: Label B

testingD = D()
print(testingD.label) #B: Label B => it's take first given/pass class wher (B,C) 

class E(C,B):
    pass

testingE = E()
print(testingE.label) #B: Label C => it's take first given/pass class wher (C,B) 

print (D.__mro__) # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>
print (E.__mro__) # (<class '__main__.E'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
```

### Simply Explained

**Method Resolution Order (MRO)** is the order in which Python looks for properties and methods when you have multiple inheritance (inheriting from multiple classes).

When `class D(B,C):` inherits from both B and C, Python searches for properties in this order:
1. First in D itself
2. Then in B (the first parent listed)
3. Then in C (the second parent listed)
4. Then in A (the grandparent)
5. Finally in the base `object` class

So when you access `testingD.label`, Python finds B's label first and returns it. If you change the order to `class E(C,B):`, then C comes first in the search order, so `testingE.label` returns C's label.

You can see the exact order using `D.__mro__`. This ensures Python doesn't search randomly and prevents confusion in complex inheritance scenarios.

---

## 9. Static Methods

### Creating Methods That Don't Need an Object

```python
class Vehical:
    @staticmethod
    def showText(text):
        return [item.strip() for item in text.split(",")]
    
raw = "Hey this is me ,    i am learning, this static method usecase "

# static method directly you can be directly called wihtout initalization
res = Vehical.showText(raw)
print(res)
    
response = Vehical()
```

### Simply Explained

A **static method** is a method that belongs to the class but doesn't need an object to run. Unlike regular methods that use `self`, static methods use the `@staticmethod` decorator and don't receive `self` as a parameter.

You can call static methods directly on the class without creating an object: `Vehical.showText(raw)`. This is useful when you have utility functions that logically belong to a class but don't need to access any object's properties.

In this example, `showText()` is just splitting and cleaning text—it doesn't need any vehicle data, so it's a perfect candidate for a static method.

---

## 10. Class Methods

### Using Class Methods as Alternative Constructors

```python
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
```

### Simply Explained

A **class method** is a method that receives the class itself (not an object) as its first parameter, which is conventionally named `cls`. Class methods use the `@classmethod` decorator.

Class methods are useful as **alternative constructors**—different ways to create objects. Instead of always using `Orders(name, brand)`, you can create an object from a dictionary: `Orders.disctionaryData({...})` or from a string: `Orders.stringData("tea, taj")`.

Each class method takes different input formats, parses them, and then creates and returns a new object using `cls(...)`. This gives you flexibility in how you initialize objects depending on your data source.

---

## 11. Setter and Getter Decorators (Properties)

### Using @property for Controlled Access

```python
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
```

### Simply Explained

**Properties** allow you to add logic when getting or setting object attributes. The `@property` decorator creates a getter—when you access `cal.price`, it actually calls the `price()` method, which returns `self._price + 100` (adding 100 to the actual price).

The `@price.setter` decorator creates a setter—when you try to set `cal.price = 50`, it validates that the price is positive before setting it. If the price is invalid, it raises a `ValueError`.

Notice the internal property is `_price` (with underscore), which signals "this is private, don't access directly." By using properties, you can add validation, transformation, and encapsulation—keeping your data clean and controlled.

---

## Summary

This learning progression covers:
1. **Basics**: Classes, objects, and namespaces
2. **Attributes**: Adding, modifying, and shadowing properties
3. **Methods**: Using `self` and constructors
4. **Inheritance**: Different ways to reuse code
5. **Advanced Topics**: MRO, static methods, class methods, and properties

Master these concepts to write well-organized, maintainable Python code!
