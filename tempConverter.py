num1 = float(input("Temperature Value: "))
unit = input("Temperature Value (C or F): ")

#Process
if unit.upper() == "C": 
    result = (num1 * 9/5) + 32
elif unit.upper () == "F":
    result = (num1 - 32) * 9/5
else:
    result = "Invalid output"

print(f"Result: {result}")
