class InvalidError(Exception):
    pass

def bill(flavour, cups):
    menu = {"mocha":130.99, "capacin":440.89}
    try:
        if flavour not in menu:
            raise InvalidError("Flavour is not Available")
        if not isinstance(cups, int):
            raise TypeError("cups value should eb an integer")
        total = menu[flavour] * cups
        print({total}) 
    except Exception as e:
        print(e)
    finally:
        print("Thanksyou for Ordering")

bill("mocha", "10") #cups value should eb an integer
bill("", "10") # flavour is not Available
