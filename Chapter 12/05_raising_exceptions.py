a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

if (b == 0):
    raise ValueError("Division by zero is not allowed.")
else:
    print(f"The division is: {a / b}")