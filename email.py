import re
def validate_email(email):
        while True:      
             email = input("Enter your email address: ")
             regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
             if re.match(regex, email):
                print("Valid email address.")
                return email
             else:
                print("Invalid email address. Please try again.")   
def validate_age(age):
        while True:
            try:
                age = int(input("Enter your age: "))
                if  0 <= age <= 120:
                    print(f"Your age is {age}.")
                    return age
                else:
                    print("Age must be between 0 and 120.")
            except ValueError:
                    print("Invalid input. Please enter a valid integer for your age.")
                    continue
def password_strength(password):
        while True:
            if pattern := re.compile(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'):
                if pattern.match(password):
                    print("Password is strong.")
                    return password
                else:
                    print("Password must be at least 8 characters long and contain both letters and numbers. Please try again.")
                    password = input("Enter a new password: ")
                
print("Welcome to the validation system!")
print("Email should have [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
print("Age should be between 0 and 120.")
print("Password should be at least 8 characters long and contain both letters and numbers.")

input_email = validate_email("Enter your email address: ")
input_age = validate_age("Enter your age: ")
input_password = password_strength("Enter your password: ") 