# Python Project (Aksep 19 6)
## Explain the code
### Calculator
#### Code
``` python
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

    # Calculate
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
```
#### Explain this code
It starts by importing the time module, which is used later in the program to delay the execution of certain parts of the code.

It then defines four functions: add, subtract, multiply, and divide, which take in two arguments (x and y) and perform the corresponding mathematical operation on them.

After that, the program displays a welcome message and then enters a while loop that continues until the user decides to exit the program. The loop starts by displaying a menu of operations (add, subtract, multiply, and divide), and then prompts the user to select one of the options by entering a number (1, 2, 3, or 4).

Once the user makes a selection, the program prompts the user to enter two numbers. It then uses an if-elif statement to check the user's choice and perform the corresponding operation using the two numbers entered by the user. The result is then printed to the screen.

If the user enters an invalid choice, the program will print "Invalid input".

Finally, after the operation is done, the program asks the user if they want to try again by entering 'y' or 'n'. If the user enters 'y', the program reloads and the loop starts again. If the user enters 'n', the program exits and displays a goodbye message.

The time.sleep() function is used to delay the execution of certain parts of the code, making the program more user-friendly and readable.
