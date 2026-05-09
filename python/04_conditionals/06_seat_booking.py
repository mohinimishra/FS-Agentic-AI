# Yoy are building a tickect info system for railway app.
#Based on type show the feature:
# Input : 'sleeper', AC, 'General', Luxury
# Output: 
    # sleeper : 20% discount, No AC
    # AC : 40% discount, 
    # General : 10% discount
# Match using match-case
# Unknown - show "Invalid seat type"

seat_type = input("Enter the seat type (sleeper/AC/General/Luxury)").lower()

match seat_type:
    case "sleeper":
        print(" No AC Bed Available")
    case "AC":
        print("AC Bed Available")
    case "General":
        print("Cheapest option Available")
    case "Luxury":
        print("AC Premium saet availabe and meal.")
    case _:
        print("Invalid seat type", seat_type)
    