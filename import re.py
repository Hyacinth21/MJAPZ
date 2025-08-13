import re

while True:
    username = input("Enter username: ")
    pattern = r"^[a-zA-Z0-9_]{0,9}+$"
    if re.match(pattern, username):
        while True:     
            password= input("Enter password: ")
            password_pattern = r"^[a-zA-Z0-9_]{8,}$"
            if re.match(password_pattern, password) and len(password) >= 8:
                print("Username and password are valid.")       
                print(f"Username: {username}, Password: {password}")
                break       
            else:
                print("Password must be at least 8 characters long and can only contain letters, numbers, and underscores. Please try again.")
                continue
        break
    else:
        print("Username must be up to 9 characters long and can only contain letters, numbers, and underscores.")
