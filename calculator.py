def addition(x, y):
    A = x + y
    print(f"{x} plus {y} is: {A}")

def subtraction(x, y):
    A = x - y
    print(f"{x} minus {y} is: {A}")

def division(x, y):
    A = x / y                                     #functions for operations.
    print(f"{x} divided by {y} is: {A}")

def multiplication(x, y):
    A = x * y
    print(f"{x} times {y} is: {A}")


while True:
    try:
        print("\n=== SIMPLE CALCULATOR ===")  # Main Menu
        print("Choose an operation:")
        print("1 ➝ Addition (+)")
        print("2 ➝ Subtraction (-)")
        print("3 ➝ Division (/)")
        print("4 ➝ Multiplication (×)")
        print("5 ➝ Exit")
        
        x = int(input("\nEnter your choice (1-5): "))

        if x == 1:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            addition(num1, num2)
            input("Press Enter to continue!  ")
        elif x == 2:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            subtraction(num1, num2)
            input("Press Enter to continue!  ")
        elif x == 3:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            if num2 == 0:
                print("Cannot divide by 0! Please try again.")
                continue  
            division(num1, num2)
            input("Press Enter to continue!  ")
        elif x == 4:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            multiplication(num1, num2)
            input("Press Enter to continue!  ")
        elif x == 5:
            print("\nGoodbye! 👋 Exiting calculator...")
            break

        else:
            print("⚠️ Invalid choice! Please enter a number between 1 and 5.")

    except ValueError:
        print("⚠️ Invalid input! Please enter a NUMBER between 1 and 5.")
