cart = []

# Function to add items to the cart
def add_items():
    while True:
        item = input("Enter an item to add (or type 'done' to stop): ")
        if item.lower() == 'done':
            break
        cart.append(item)
    print("Items added.\n")

# Function to remove a specific item
def remove_item():
    item = input("Enter the item to remove: ")
    if item in cart:
        cart.remove(item)
        print(f"'{item}' removed from the cart.\n")
    else:
        print(f"'{item}' not found in the cart.\n")

# Function to sort the cart
def sort_cart():
    cart.sort()
    print("Cart sorted.\n")

# Simple menu to test the functions
while True:
    print("Cart:", cart)
    print("Menu: [1] Add [2] Remove [3] Sort [4] Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        add_items()
    elif choice == '2':
        remove_item()
    elif choice == '3':
        sort_cart()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid option.\n")
