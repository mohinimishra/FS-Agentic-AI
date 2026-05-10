# [expression for item in iterable if condition]

menu = ["Masala Tea", "Ginger Tea", "Iced Lemon Tea", "Iced Peach Tea", "Green Tea"]
comp = [tea for tea in menu if "Iced" in tea]
print(comp) #['Iced Lemon Tea', 'Iced Peach Tea']
