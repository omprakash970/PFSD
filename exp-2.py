try:
    a=float(input("Enter the number"))
    b=float(input("Enter the number"))
    print("\nSelect Operation")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    choice=int(input("Enter the choice"))
    if choice==1:
        print("Result: ", a+b)
    if choice==2:
        print("Result:", a-b)
    if choice==3:
        print("Result: ", a*b)
    elif choice ==4:
        if b==0:
            print("Error: Division by zero is not allowed")
        else:
             print("Result:", a / b)
except ValueError:
    print("Error: value input!! please enter the number numbers only ")

