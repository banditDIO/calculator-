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


def exponent(x, y):
    A = x ** y
    print(f"{x} to the power of {y} is: {A}")


def squareRoot(x):
    A = x ** 0.5
    print(f"The Square root of {x} is: {A}")


def modulo(x, y):
    A = x % y
    print(f"The remainder of {x} divided by {y} is: {A}")


def factorial(x):
    while x < 0:
        print("Factorial cant be a negative number! Please enter a positive number.")
        x = int(input("Enter a non-negative number: "))
    result = 1
    for i in range(1, x + 1):
        result *= i
    print(f"The Factorial of {x} is: {result}")



while True:
    try:
        print("\n=== SIMPLE CALCULATOR ===")  # Main Menu
        print("Choose an operation:")
        print("1 ➝ Addition (+)")
        print("2 ➝ Subtraction (-)")
        print("3 ➝ Division (/)")
        print("4 ➝ Multiplication (×)")
        print("5 ➝ Exponent")
        print("6 ➝ Square root")
        print("7 ➝ Modulo")
        print("8 ➝ Factorial")
        print("9 ➝ Exit")
        
        x = int(input("\nEnter your choice (1-9): "))

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
            num1 = float(input("Enter your number: "))
            num2 = float(input("Enter your exponent: "))
            exponent(num1, num2)
            input("Press Enter to continue!  ")


        elif x == 6:
            num1 = float(input("Enter your number: "))
            squareRoot(num1)           
            input("Press Enter to continue!  ")


        elif x ==7:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            if num2 == 0:
                 print("Cannot divide by 0! Please try again.")
                 continue 
            modulo(num1, num2)
            input("Press Enter to continue! ")
        

        elif x == 8:
            num1 = int(input("Enter your first number: "))
            factorial(num1)
            input("Press Enter to continue! ")


        elif x == 9:
            print("\nGoodbye! 👋 Exiting calculator...")
            break
        
        else:
            print("⚠️ Invalid choice! Please enter a number between 1 and 9.")

    except ValueError:
        print("⚠️ Invalid input! Please enter a NUMBER between 1 and 9.")


#add more operations
#plans: Add more functionality, instead of pressing enter to continue everytime, maybe add a way to use the same operation