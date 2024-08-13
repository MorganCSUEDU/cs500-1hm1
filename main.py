def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

print("Part 1: Addition and Subtraction")
num1 = get_valid_number("Enter number 1: ")
num2 = get_valid_number("Enter number 2: ")

addition_result = num1 + num2
subtraction_result = num1 - num2

print(f"Addition result: {addition_result}")
print(f"Subtraction result: {subtraction_result}")

print("\nPart 2: Multiplication and Division")
num3 = get_valid_number("Enter number 1: ")
num4 = get_valid_number("Enter number 2: ")

multiplication_result = num3 * num4
print(f"Multiplication result: {multiplication_result}")

if num4 != 0:
    division_result = num3 / num4
    print(f"Division result: {division_result}")
else:
    print("Cannot divide by zero.")
