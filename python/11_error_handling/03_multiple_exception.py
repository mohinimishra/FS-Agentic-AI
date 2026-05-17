def process_order(item, tax):
    try:
        price = {"latte":30.0, "mocha":60.0}[item]
        cost = price*tax
        print(f"Order Served : ${cost:.2f}")
    except KeyError:
        print(f"Sorry that item is not available")
    except TypeError:
        print(f"Amount should be number")
    
process_order("mocha", "two") #Amount should be number
process_order("", 20) # Sorry that item is not available
process_order("mocha", {20}) # Amount should be number






        
        
        