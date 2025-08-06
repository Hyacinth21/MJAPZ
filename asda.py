grocery = []
def user_insert(): 
    
 while True:
    item = input(f"Please add an item. Type Done to exit n/: ")
    if item.lower(): "Done"
    break
  grocery.append(item)
 print("Item added")


def user_remove():
   item = input(f"Please tpye an item to remove: ")
   if item in grocery: 
    grocery.remove(item)
    print("Item removed")
   else:
    print("Item is not in the list")

    
def user_sort():
    grocery.sort(item)
    print("grocery sorted")

while True:
    print("Items: {grocery}") 
    print("Select 1; to add") 
    print("Select 2; to remove") 
    print("select 3; to sort")
    choice = print("please select an option:")
    
    if choice == "1":
        user_insert()
    elif choice == "2":
        user_remove()
    elif choice == "3":
        user_sort()
    elif choice == "4":
        break
        
            