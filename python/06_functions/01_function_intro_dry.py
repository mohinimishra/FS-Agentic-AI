#  Reduce Code Duplication
# You are managing a store 
# You recive many orders and you wnat to print the customer name along with type of item they orderd.
# Task
    # write a function print_order(name, item)
    # Call it multiple items for different Customers

customers=["alice", "lufi", "jen"]
items=["bread", "choclate", "milk"]

def print_order(name,item):
        print(f"{name} bought {item}")
        
print_order("alice", "bread")
print_order("lufi", "choclate")
print_order("jen", "milk")
        
for name, item in zip(customers, items):
        print_order(name, item) 

# Spliting a Complex Task
# You are creating monthly report for an resturant sales.
# Istaed of putting all logic in one place, break it down
# Task
    # fetch_sales()
    # filter valid_orders()
    # summarize_data()
    
def fetch_sales():
        print(f"Fetching Sales Data")
        
def valid_orders():
        print(f"Fetching Valid Orders")
        
def summarize_data():
        print(f"Orders Details")
        
def generate_data():
        fetch_sales()
        valid_orders()
        summarize_data()
        print(f"report is ready!")
generate_data()
        
# Hidiing Implementaion Details

    # You are building an app that registers usesrs
    # You want seprate concerns: getting input, validating and saving.
    # Task:
        #Writing register user() that calls
        # get_imput()
        # validate_input()
        # save_To_db()

def get_input():
    print(f"Getting the input")
    
def validate_input():
    print(f"Validating the input")

def save_To_db():
    print(f"Saving to DB")

def users():
    get_input()
    validate_input()
    save_To_db()
    print(f"User Registerd")
users()





