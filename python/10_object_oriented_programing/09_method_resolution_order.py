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
