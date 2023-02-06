# Import & Settings
import time


# Operations
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


# Welcome Message
print("Welcome to the Calculator!")
time.sleep(1)
while True:
    print("Select operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Ask for operation
    time.sleep(1)
    choice = input("Enter the number of your choice (1, 2, 3, or 4): ")

    # Check if input is valid
    if choice not in ('1', '2', '3', '4'):
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
        continue

    # Ask for numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Calculate
    if choice == '1':
        result = add(num1, num2)
        operation = '+'
    elif choice == '2':
        result = subtract(num1, num2)
        operation = '-'
    elif choice == '3':
        result = multiply(num1, num2)
        operation = '*'
    else:
        result = divide(num1, num2)
        operation = '/'

    # Display result
    time.sleep(1)
    print(f"{num1} {operation} {num2} = {result}")

    # Ask to try again
    time.sleep(1)
    try_again = input("Do you want to perform another calculation? (y/n): ")

    if try_again.lower() != 'y':
        print("Goodbye!")
        time.sleep(1)
        break
