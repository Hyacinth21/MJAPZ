num1 = float(input("Temperature Value: "))
unit = (input("Temperature Unit (C or F): "))

#Process
if unit.upper() == "C": 
    result = (num1 * 5/9) - 32
    print(f"Result: {result}°F")
elif unit.upper () == "F":
    result = (num1 * 9/5) + 32
    print(f"Result: {result}°C")
else:
    result = "Invalid output"
