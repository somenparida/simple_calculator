def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        return "Error, Division by zero is not permitted."
    else:
        return result

while True:
    print("\nCalculator")
    try:
        num1 = input("Enter the first number (or 'q' to quit): ")
        if num1.lower() == 'q':
            break
        num1 = float(num1)
        
        num2 = float(input("Enter the second number: "))

        print("Choose an operation:")
        print("1) Add")
        print("2) Subtract")
        print("3) Multiply")
        print("4) Divide")
        print("5) Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Exiting calculator.")
            break
        else:
            print("Invalid input! Please enter a valid choice (1-5).")

    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except Exception as e:
        print("An error occurred:", e)
