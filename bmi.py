#Insert mo pangalan mo pre
name = input("Please enter your name: ")
weight = float(input("Please enter your weight in kg: "))
height = float(input("Please enter your height in meters: "))
bmi = weight / height ** 2
UNDER_WEIGHT =  bmi < 18.5
HEALTHY_WEIGHT = bmi >= 18.5 and bmi < 24.9
OVER_WEIGHT = bmi >= 25 and bmi < 29.9
OBESE = bmi >= 30

while True:
    # Insert mo body weight at height mo pre
    try:
       if UNDER_WEIGHT:
            print(f"{name}, your BMI is {bmi:.2f}. You are underweight.")
            break
       elif HEALTHY_WEIGHT:
            print(f"{name}, your BMI is {bmi:.2f}. You have a healthy weight.")
            break
       elif OVER_WEIGHT:
            print(f"{name}, your BMI is {bmi:.2f}. You are overweight.")
            break
       elif OBESE:
            print(f"{name}, your BMI is {bmi:.2f}. You are obese.")
            break
    except ValueError:
        print("Invalid input. Please enter a valid number for your body weight and height.")
        
        
        
        
        
        
# while True:
#     try: 
#         height = float(input("Please enter your height in meters: "))
#         if height <= 0:
#             print("Height must be a positive number.")
#             continue
#         bmi = body_weight / (height ** 2)
        
#         print(f"Your BMI is: {bmi:.2f}")
#         break
#     except ValueError:
#         print("Invalid input. Please enter a valid number for your height.")