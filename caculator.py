str4 = "welcome to calculator"
print(str4.center(40))   # Fixed: no space between str and 4

input("Press the Enter key to continue...")

print("Ready to perform calculation")

a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
operator = input("Enter an operator: ")

if operator == "+":
    result = a + b
elif operator == "-":
    result = a - b
elif operator == "*":
    result = a * b
elif operator == "/":
    if b != 0:   # Fixed: use 'b', not 'b'
        result = a / b
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator!"

print("Result:", result)

