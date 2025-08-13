while True:
        try:
            age = int(input("Please enter your age: "))
            if 0 <= age <= 120:
                print(f"Your age is {age}.")
                break
            else:
                print("Age must be between 0 and 120. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for your age.")
            continue
            
            