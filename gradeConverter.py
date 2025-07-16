num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

#process

Average = (num1 + num2 + num3) / 3
print(f"Average Score: {Average}")

if 89.5 < Average < 100:
  grade = "A"
elif 79.5 < Average < 89.4: 
  grade = "B"
elif 69.5 < Average < 79.4:
  grade = "C"
elif 49.5 < Average < 60.4:
  grade = "D"
elif 0 < Average  < 49.4:
  grade = "E"
  
#output 

print(f"Average Score: {Average:.2f}, Grade letter: {grade} ")
