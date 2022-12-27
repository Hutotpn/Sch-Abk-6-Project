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


# Welcome Mesage
print("Welcome to the calculator!")
time.sleep(1)
while True:
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    # Ask for operation
    time.sleep(1)
    choice = input("Enter choice(1/2/3/4): ")

    # Ask for number
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Caculate
    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid input")

    # Try again?
    time.sleep(1)
    print("Do you want to try again?(y/n): ")
    # Ask for input
    tryagain = input("Enter y/n: ")
    # If yes, do it again
    if tryagain == 'y':
        print("Reloading!")
        time.sleep(0.5)
        print("Reloaded!")

    # If no, exit
    else:
        print("Goodbye!")
        time.sleep(3)
        break
