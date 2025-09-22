# Description
print("Simple Calculator")
# Input Area
x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
# Menu
print("\nChoose operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
# User choice
choice = int(input("Enter your choice (1/2/3/4): "))
# Output Area
if choice == 1:
    print("Result:", x + y)
elif choice == 2:
    print("Result:", x - y)
elif choice == 3:
    print("Result:", x * y)
elif choice == 4:
    if y != 0:
        print("Result:", x / y)
    else:
        print("Error: Division by zero is not allowed")
else:
    print("Invalid choice")
