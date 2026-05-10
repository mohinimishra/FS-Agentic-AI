# (expression for item in iterable if condition)

menu = [100,200, 200, 100,400, 500 ]
# comp = (item for item in menu if item>200)
# print(comp)
 # ➜  07_comprehensions git:(master) ✗ python3 04_generator_comprehension.py <generator object <genexpr> at 0x101b83660>
# as this is kind of streaming insted of adding whole data to mer

comp = sum (item for item in menu if item>200)
print(comp)

