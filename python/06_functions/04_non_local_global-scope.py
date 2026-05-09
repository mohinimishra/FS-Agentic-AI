# NonLocal -
def update_order():
    flavour= "ginger"
    def kitchen_update():
        # nonlocal flavour # only check for outer functions, dosent make it global
        # flavour = "mint"
        def  printUpdate():
            nonlocal flavour # only check for outer functions, dosent make it global
            flavour = "mint"
        printUpdate()
    kitchen_update()
    print(f"Order after kitchen update:{flavour}") # mint 
update_order()

# Global - can call anywhere

status = "order taken"

def update_status():
    def kitchen_update():
        global status
        status = "cooked"
    kitchen_update()
update_status()
print(f"Updated status:{status}")
