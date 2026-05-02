# A local Cafe wants a program that suggest snack. 
# If a customer ask for "cookies" or "smaosa", it confirms the order otherwise
    # says it's not available.
    # Tasks:
    # Taks snack input 
    # check if "cookies" or "samosa", confirm order
    # else return it's not available.

snack = input("Enter your preferd snack: ").lower()
print(f"User Enter :{snack}");

if snack == "cookies" or snack == "samosa":
    print(f"Great Chocie! We will serve {snack}")
else:
    print(f"it's not available")