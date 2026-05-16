class Car:
    origin="India"
    
print(Car.origin)

Car.color = "red" # adding property

print(Car.color)

# create object
carDetails = Car()
print(f"Origin {carDetails.origin} Color: {carDetails.color}")
