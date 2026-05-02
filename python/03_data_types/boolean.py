# True is treated as 1 and False is treated as 0 in arithmetic operations

is_boolien = True
count =5
print(is_boolien)
print(type(is_boolien))
print(f"Id of is_boolien: {id(is_boolien)}") 
total = count +is_boolien
print(f"Total: {total}")
print(f"Id of total: {id(total)}") 

is_boolien = False
print(f"Id of is_booliean: {id(is_boolien)}")

name = 'mohini'
print(f"Total: {total}")

#Logical operations
print(f"True and False: {True and False}")
isWeekend = True
isHoliday = False
can_relax = isWeekend and isHoliday
print(f"Can relax: {can_relax}")