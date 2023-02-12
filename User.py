# User class to store user information
class User:
    def __init__(self, name, phone, email, address, password):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.password = password
        self.order_history = []

# Dictionary to store all registered users
registered_users = {}

# Function to register a user
def register():
    print("Enter your information for registration:")
    name = input("Full Name: ")
    phone = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")
    password = input("Password: ")
    
    # Create a new user object and add it to the registered users
    new_user = User(name, phone, email, address, password)
    registered_users[email] = new_user
    print("Registration Successful!")

# Function to log in to the application
def login():
    email = input("Email: ")
    password = input("Password: ")
    
    # Check if the email exists in the registered users
    if email in registered_users:
        user = registered_users[email]
        
        # Check if the password is correct
        if user.password == password:
            print("Login Successful!")
            while True:
                print("1. Place New Order")
                print("2. Order History")
                print("3. Update Profile")
                print("4. Logout")
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    place_new_order(user)
                elif choice == 2:
                    show_order_history(user)
                elif choice == 3:
                    update_profile(user)
                elif choice == 4:
                    # Logout code goes here
                    break
                else:
                    print("Invalid choice.")
        else:
            print("Incorrect Password!")
    else:
        print("Email not found. Please register first.")

def show_order_history(user):
    print("\nOrder History:")
    if len(user.order_history) == 0:
        print("No order history found.")
    else:
        for order in user.order_history:
            print("\nOrder Date: {}".format(order[0]))
            print("{:<20} {:<20} {:<20}".format("Food name", "Quantity", "Price"))
        for item in order[1]:
            print("{:<20} {:<20} {:<20}".format(item[0], item[1], item[2]))

import datetime

def place_order(user, items_selected, menu):
    total_bill = 0
    order_items = []

    print("\nSelected Items:")
    for item in items_selected:
        selected_item = menu[item - 1]
        print(f"{selected_item[0]} - Quantity: {selected_item[1]} - Price: {selected_item[2]}")
        total_bill += selected_item[2]
        order_items.append(selected_item)

    print(f"\nTotal Bill: {total_bill}")
    pay_amount = int(input("Enter the amount to be paid: "))
    if pay_amount >= total_bill:
        print("\nOrder Placed Successfully!")
        order_date = str(datetime.datetime.now().date())
        user.order_history.append((order_date, order_items))
    else:
        print("\nInsufficient Amount! Please try again.")

def place_new_order(user):
    menu = [("Tandoori Chicken", "4 pieces", 240),
            ("Vegan Burger", "1 Piece", 320),
            ("Truffle Cake", "500gm", 900)]

    print("\nMenu:")
    print("{:<20} {:<20} {:<20}".format("Food name", "Quantity", "Price"))
    for index, item in enumerate(menu):
        print("{}. {:<20} {:<20} {:<20}".format(index + 1, item[0], item[1], item[2]))

    items_selected = [int(x) for x in input("Enter the items to be ordered separated by space: ").strip().split()]
    place_order(user, items_selected, menu)


def update_profile(user):
    print("\nUpdate Profile:")
    print("1. Full Name")
    print("2. Phone Number")
    print("3. Email")
    print("4. Address")
    print("5. Password")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        user.name = input("Enter new full name: ")
    elif choice == 2:
        user.phone = input("Enter new phone number: ")
    elif choice == 3:
        user.email = input("Enter new phone email: ")
    elif choice == 4:
        user.address = input("Enter new address: ")
    elif choice == 5:
        user.password = input("Enter new password: ")
    else:
        print("Invalid choice. Please try again.")
    print("User details updated successfully!")

import datetime

def place_order(user, items_selected, menu):
    total_bill = 0
    order_items = []

    print("\nSelected Items:")
    for item in items_selected:
        selected_item = menu[item - 1]
        print(f"{selected_item[0]} - Quantity: {selected_item[1]} - Price: {selected_item[2]}")
        total_bill += selected_item[2]
        order_items.append(selected_item)

    print(f"\nTotal Bill: {total_bill}")
    pay_amount = int(input("Enter the amount to be paid: "))
    if pay_amount >= total_bill:
        print("\nOrder Placed Successfully!")
        order_date = str(datetime.datetime.now().date())
        user.order_history.append((order_date, order_items))
    else:
        print("\nInsufficient Amount! Please try again.")

def place_new_order(user):
    menu = [("Tandoori Chicken", "4 pieces", 240),
            ("Vegan Burger", "1 Piece", 320),
            ("Truffle Cake", "500gm", 900)]

    print("\nMenu:")
    print("{:<20} {:<20} {:<20}".format("Food name", "Quantity", "Price"))
    for index, item in enumerate(menu):
        print("{}. {:<20} {:<20} {:<20}".format(index + 1, item[0], item[1], item[2]))

    items_selected = [int(x) for x in input("Enter the item numbers to be ordered separated by space (1 2 3): ").strip().split()]
    place_order(user, items_selected, menu)

# Welcome message
print("Welcome to EDYODA Restaurant")

while True:
    print("Press 1 for Register")
    print("Press 2 for Log in")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        register()
    elif choice == 2:
        login()
    elif choice == 3:
        # Exit code goes here
        break
    else:
        print("Invalid choice.")