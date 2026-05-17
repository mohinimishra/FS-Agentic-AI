employe = {"name":"Alice", "age":20}

try:
    print(f"{employe['name']} is {employe['age']} years old.")
    employe['gender']
except KeyError:
    print(f"{KeyError.__doc__}")
    

def showEmplyeDetail(name, age, gender):
    try:
        if not name or not age or not gender:
            raise ValueError("Please provide {name} {age} & {gender} value.")
    except ValueError as e:
        print (f"Error {e}")
    else:
        print(f"{name, age, gender}")
    finally:
        print(f"Thanks!")

showEmplyeDetail("alice" ,"20", "Male")
showEmplyeDetail("","","")
    
    
    