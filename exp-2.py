# Experiment 2: Simple Calculator

try:
    # 1. Read two numbers from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # 2. Display menu
    print("\nSelect Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # 3. User choice
    choice = int(input("Enter your choice (1-4): "))

    # 4. Perform operation
    if choice == 1:
        print("Result:", num1 + num2)

    elif choice == 2:
        print("Result:", num1 - num2)

    elif choice == 3:
        print("Result:", num1 * num2)

    elif choice == 4:
        if num2 == 0:
            print("Error: Division by zero is not allowed")
        else:
            print("Result:", num1 / num2)

    else:
        print("Invalid choice! Please select between 1 and 4.")

except ValueError:
    print("Error: Please enter valid numeric inputs.")
