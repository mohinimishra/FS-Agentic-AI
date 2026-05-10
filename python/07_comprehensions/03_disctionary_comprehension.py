# {key:value for key,value in iterables.items()}

menu_in_inr = {
    "tea": 20,
    "cold drink":40
    }
menu_in_usd = {item:price/90 for item,price in menu_in_inr.items()}
print(menu_in_usd) #{'tea': 0.2222222222222222, 'cold drink': 0.4444444444444444}