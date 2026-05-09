# Using Dictionaries Insted of Repaetd Cases:
users =[{"id":1, "total":100, "cupon":"p10"},{"id":2, "total":102, "cupon":"p20"},{"id":3, "total":101, "cupon":"p30"}]
discounts={
    "p10": (0.2, 0),
    "p20": (0.5, 4),
    "p30": (0.8, 7),
    }

for user in users:
    percent, fixed = discounts.get(user["cupon"], (0,0)) # 2nd argument if no value found then returns (0,0)
    discount = user["total"] * percent +fixed
    print(f"{user['id']} paid {user['total']} and got discount for next visit of rs {discount}")