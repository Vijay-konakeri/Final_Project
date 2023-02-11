import json

restaurant_name = "EDYODA Restaurant"

admin_username = "admin"
admin_password = "secret"

food_id = 1
food_items = []

print("Welcome to", restaurant_name)
print("Admin Login")

username = input("Username is(admin): ")
password = input("Password is(secret): ")

if username == admin_username and password == admin_password:
    print("Login Successful")
else:
    print("Login failed")
    exit()

def save_to_file(food_items):
    with open("food_items.json", "w") as file:
        json.dump(food_items, file)

def load_from_file():
    try:
        with open("food_items.json", "r") as file:
            return json.load(file)
    except:
        return []

while True:
    print("\nEnter 1 to add a new food item")
    print("Enter 2 to view the food items")
    print("Enter 3 to edit a food item")
    print("Enter 4 to remove a food item")
    print("Enter 0 to exit")
    
    option = int(input("Enter your choice: "))
    
    if option == 1:
        name = input("Enter food name: ")
        quantity = input("Enter food quantity: ")
        price = float(input("Enter food price: "))
        discount = float(input("Enter food discount: "))
        stock = int(input("Enter food stock: "))
        
        food_items.append({
            "FoodID": food_id,
            "Name": name,
            "Quantity": quantity,
            "Price": price,
            "Discount": discount,
            "Stock": stock
        })
        
        food_id += 1
        
        save_to_file(food_items)
        
        print("Food item added successfully")
        
    elif option == 2:
        food_items = load_from_file()
        if len(food_items) == 0:
            print("No food items found")
        else:
            print("Food items:")
            print("ID\tName\tQuantity\tPrice\tDiscount\tStock")
            for food_item in food_items:
                print("{}\t{}\t\t{}\t\t{:.2f}\t\t{:.2f}\t\t{}".format(
                    food_item["FoodID"],
                    food_item["Name"],
                    food_item["Quantity"],
                    food_item["Price"],
                    food_item["Discount"],
                    food_item["Stock"]
                ))
                
    elif option == 3:
        food_id = int(input("Enter food ID to edit: "))
        food_items = load_from_file()
        food_item_found = False
        for index, food_item in enumerate(food_items):
            if food_item["FoodID"] == food_id:
                food_item_found = True
                name = input("Enter food name: ")
                quantity = input("Enter food quantity: ")
                price = float(input("Enter food price: "))
                discount = float(input("Enter food discount: "))
                stock = int(input("Enter food stock: "))
                
                food_items[index] = {
                    "FoodID": food_id,
                    "Name": name,
                    "Quantity": quantity,
                    "Price": price,
                    "Discount": discount,
                    "Stock": stock
                }
                
                save_to_file(food_items)
                
                print("Food item updated successfully")
                break
        
        if not food_item_found:
            print("Food item not found")

    elif option == 4:
        food_id = int(input("Enter food ID to remove: "))
        food_items = load_from_file()
        food_item_found = False
        for index, food_item in enumerate(food_items):
            if food_item["FoodID"] == food_id:
                food_item_found = True
                food_items.pop(index)
                save_to_file(food_items)
                print("Food item removed successfully")
                break
        if not food_item_found:
            print("Food item not found")
